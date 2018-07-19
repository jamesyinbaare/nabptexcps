from django.db import models




class School(models.Model):
    REGION = (
        ('UW','Upper West Region'),
        ('UE','Upper East Region'),
        ('N','Northern Region'),
        ('BA','Brong Ahafo Region'),
        ('A','Ashanti Region'),
        ('E','Eastern Region'),
        ('W','Western Region'),
        ('V','Volta Region'),
        ('GA','Greater Accra Region'),
        ('C','Upper West Region')
    )
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=2,choices=REGION)
    def __str__(self):
        return self.name


class Student(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    o_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField()
    admin_date = models.DateField()
    grad_date = models.DateField()
    sch = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return "{0}, {1} {2}".format(self.f_name, self.l_name,self.o_name)
        



