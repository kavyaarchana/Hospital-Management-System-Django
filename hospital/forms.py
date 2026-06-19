from django import forms
from django.utils import timezone
from .models import Patient, Doctor, Appointment


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'phone']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'phone']


class AppointmentForm(forms.ModelForm):

    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date']

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']

        if appointment_date < timezone.now().date():
            raise forms.ValidationError(
                "Appointment cannot be booked in the past."
            )

        return appointment_date

    def clean(self):
        cleaned_data = super().clean()

        doctor = cleaned_data.get('doctor')
        appointment_date = cleaned_data.get('appointment_date')

        if doctor and appointment_date:

            exists = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date
            ).exclude(
                id=self.instance.id
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "This doctor already has an appointment on this date."
                )

        return cleaned_data