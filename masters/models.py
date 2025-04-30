from django.db import models

# Create your models here.
class Religion(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Citizen(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    meta = models.JSONField(default=dict)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Regency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    meta = models.JSONField(default=dict)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Subdistrict(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    regency = models.ForeignKey(Regency, on_delete=models.CASCADE)
    meta = models.JSONField(default=dict)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Village(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    subdistrict = models.ForeignKey(Subdistrict, on_delete=models.CASCADE)
    meta = models.JSONField(default=dict)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class RegistrationPath(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class StudyProgram(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class RegistrationPeriod(models.Model):
    period = models.CharField(max_length=9, )

    class Meta:
        ordering = ['period']

    def __str__(self):
        return self.period

class School(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Income(models.Model):
    amount = models.CharField(max_length=50)

    class Meta:
        ordering = ['amount']
        
    def __str__(self):
        return f"Rp {self.amount}"