from django.db import models

class ClinicInfo(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='departments/')

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/')
    bio = models.TextField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    patient_name = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return f"Feedback from {self.patient_name}"

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment with {self.name} on {self.date}"
