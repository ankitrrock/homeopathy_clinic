from django.shortcuts import render, redirect
from .models import ClinicInfo, Department, Doctor, Testimonial
from .forms import AppointmentForm
from django.contrib import messages


def index(request):
    clinic = ClinicInfo.objects.first()
    departments = Department.objects.all()
    doctors = Doctor.objects.all()
    testimonials = Testimonial.objects.all()
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your appointment has been booked!")
            return redirect('/')  # after success

    return render(request, 'index.html', {
        'clinic': clinic,
        'departments': departments,
        'doctors': doctors,
        'testimonials': testimonials,
        'form': form
    })
