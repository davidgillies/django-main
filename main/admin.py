from django.contrib import admin
from models import Surgery, Volunteer, Appointment
import arrow

def have_moved(modeladmin, request, queryset):
    queryset.update(moved_away=1)

class SurgeryAdmin(admin.ModelAdmin):
    pass
    
    
admin.site.register(Surgery, SurgeryAdmin)

class AppointmentInline(admin.TabularInline):
    model = Appointment
    fields = ('appt_date', 'appt_time', 'test_site')
    extra = 0


class VolunteerAdmin(admin.ModelAdmin):
    inlines = [AppointmentInline,]
    list_display = ('surname', 'forenames', 'town', 'postcode', 'surgeries')
    list_filter = ('town', 'surgeries')
    search_fields = ('surname', 'forenames', 'town', 'postcode', 'surgeries__full_name')
    date_hierarchy = 'dob'
    actions = [have_moved,]
    
    fieldsets = (
        (None, {'fields': (('surname', 'forenames'),
                            ('initials', 'dob'),
                            ('title', 'sex'))}),
        ('Address', {'classes': ('collapse',), 
                     'fields': (('addr1', 'home_tel'),
                                ('addr2', 'work_tel'),
                                ('town', 'mobile'),
                                ('county', 'email'),
                                ('postcode', ))}),
        ('Details', {'classes': ('collapse', 'extrapretty'),
                     'description': 'Extra <b>details</b>',
                     'fields': (('nhs_no', 'surgeries'),
                                ('modified', 'modified_by'),
                                ('diabetes_diagnosed', 'moved_away'),)}),
    )
    readonly_fields = ('modified', 'modified_by')
    
    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user.get_username()
        obj.modified = str(arrow.now()).replace('+01:00', '')
        obj.save()

admin.site.register(Volunteer, VolunteerAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    pass
    
    
admin.site.register(Appointment, AppointmentAdmin)
