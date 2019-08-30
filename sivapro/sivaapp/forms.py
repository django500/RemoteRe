from django import forms
from multiselectfield import MultiSelectFormField
class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label='Enter Your Rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label='Enter Your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Valiable Feedback'
            }
        )
    )
class EnquryForm(forms.Form):
    name = forms.CharField(
        label='Enter Your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Your Email Id',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )
    GENDER_CHOICES =(
        ('F','FEMALE'),
        ('M','MALE')
    )
    gender = forms.ChoiceField(
        label='Enter Your Gender',
        widget=forms.RadioSelect(),choices=GENDER_CHOICES
    )
    COURSES_CHOICES = (
        ('PY', 'PTHON'),
        ('DJ', 'DJANGO'),
        ('RA', 'REST API'),
        ('FL', 'FLASK'),
        ('J', 'JAVA'),
        ('UI', 'UI')
    )
    courses = MultiSelectFormField(choices=COURSES_CHOICES)
    SHIFTS_CHOISES = (
        ('Morning', 'Morning Shift'),
        ('Afternoon', 'Afternoon Shift'),
        ('Evening', 'Evening Shift'),
        ('Night', 'Night Shift')
    )
    shifts = MultiSelectFormField(choices=SHIFTS_CHOISES)
    y= range(1986,2020)
    start_date = forms.DateTimeField(label='Select Date',widget=forms.SelectDateWidget(years=y))