from django.contrib import admin
from .models import ClinicInfo, Department, Doctor, Testimonial, Appointment

admin.site.register(ClinicInfo)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Testimonial)
admin.site.register(Appointment)
