from django.shortcuts import render,redirect, get_object_or_404
from .models import Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm, AppointmentForm



def home(request):
    patient_count = Patient.objects.count()
    doctor_count = Doctor.objects.count()
    appointment_count = Appointment.objects.count()

    context = {
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'appointment_count': appointment_count,
    }

    return render(request, 'home.html', context)


def patient_list(request):
    search = request.GET.get('search')

    if search:
        patients = Patient.objects.filter(name__icontains=search)
    else:
        patients = Patient.objects.all()

    return render(request, 'patient_list.html', {'patients': patients})
    
def doctor_list(request):
    search = request.GET.get('search')

    if search:
        doctors = Doctor.objects.filter(name__icontains=search)
    else:
        doctors = Doctor.objects.all()

    return render(request, 'doctor_list.html', {'doctors': doctors})


def appointment_list(request):
    search = request.GET.get('search')

    if search:
        appointments = Appointment.objects.filter(
            patient__name__icontains=search
        )
    else:
        appointments = Appointment.objects.all()

    return render(
        request,
        'appointment_list.html',
        {'appointments': appointments}
    )

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
    

        if form.is_valid():
            form.save()
            return redirect('patient_list')

    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form': form})
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')
             

    else:
        form = DoctorForm()

    return render(request, 'add_doctor.html', {'form': form})
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('appointment_list')

    else:
        form = AppointmentForm()

    return render(request, 'add_appointment.html', {'form': form})
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect('patient_list')

    else:
        form = PatientForm(instance=patient)

    return render(request, 'edit_patient.html', {'form': form})
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(request, 'delete_patient.html', {'patient': patient})
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')

    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'edit_doctor.html', {'form': form})
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')

    return render(request, 'delete_doctor.html', {'doctor': doctor})
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save()
            return redirect('appointment_list')

    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'edit_appointment.html', {'form': form})
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')

    return render(
        request,
        'delete_appointment.html',
        {'appointment': appointment}
    )