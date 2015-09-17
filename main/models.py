from django.db import models


class Surgery(models.Model):
    full_name = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    addr1 = models.CharField(max_length=45, blank=True)
    addr2 = models.CharField(max_length=45, blank=True)
    town = models.CharField(max_length=45, blank=True)
    county = models.CharField(max_length=45, blank=True)
    postcode = models.CharField(max_length=45, blank=True)
    telephone = models.CharField(max_length=12, blank=True)
    admin_contact_name = models.CharField(max_length=45, blank=True)
    admin_contact_number = models.CharField(max_length=45, blank=True)
    hscic_code = models.CharField(max_length=45, blank=True)
    area = models.CharField(max_length=45, blank=True)
    modified_by = models.CharField(max_length=45, blank=True)
    modified = models.DateTimeField(blank=True, null=True)
    surgeriescol = models.CharField(max_length=45, blank=True)
    
    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Surgery'
        verbose_name_plural = 'Surgeries'

class Volunteer(models.Model):
    
    sex_types = (
        ('M', 'M'),
        ('F', 'F'),
    )
    title_types = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof'),
    )
    boolean_choices = (
        (1, 'True'),
        (2, 'False'),
        (3, 'None'),
    )
    surname = models.CharField(max_length=45)
    forenames = models.CharField(max_length=45)
    initials = models.CharField(max_length=5, blank=True)
    dob = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=12, blank=True, choices=title_types)
    sex = models.CharField(max_length=1, blank=True, choices=sex_types)
    addr1 = models.CharField(max_length=45, blank=True)
    addr2 = models.CharField(max_length=45, blank=True)
    town = models.CharField(max_length=45, blank=True)
    county = models.CharField(max_length=45, blank=True)
    postcode = models.CharField(max_length=45, blank=True)
    home_tel = models.CharField(max_length=45, blank=True)
    work_tel = models.CharField(max_length=45, blank=True)
    mobile = models.CharField(max_length=45, blank=True)
    email = models.CharField(max_length=100, blank=True)
    nhs_no = models.CharField(max_length=45, blank=True)
    moved_away = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    diabetes_diagnosed = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    modified_by = models.CharField(max_length=45, blank=True)
    reason = models.IntegerField(blank=True, null=True)
    phase1_comment = models.TextField(blank=True)
    phase2_comment = models.TextField(blank=True)
    modified = models.DateTimeField(blank=True, null=True)
    surgeries = models.ForeignKey(Surgery, blank=True, null=True)
    
    def __unicode__(self):
        return "%s, %s" % (self.surname, self.forenames)


class Appointment(models.Model):
    repeat = models.IntegerField(blank=True, null=True)
    studyphase = models.IntegerField(blank=True, null=True)
    appt_date = models.DateField(blank=True, null=True, help_text="Format: YYYY-MM-DD")
    appt_time = models.TimeField(blank=True, null=True, help_text="Format: HH:MM:SS")
    test_site = models.CharField(max_length=10, blank=True)
    modified_by = models.CharField(max_length=45, blank=True)
    modified = models.DateTimeField(blank=True, null=True)
    volunteers = models.ForeignKey(Volunteer)
