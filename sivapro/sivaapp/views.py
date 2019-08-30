from django.shortcuts import render
from .models import ServicesData,FeedbackData,EnquiryData
from .forms import FeedbackForm,EnquryForm
from django.http.response import HttpResponse

import datetime as dt
date1 = dt.datetime.now()

# Create your views here.
def home_view(request):
    return render(request,'durgasoft_home.html')


def services_view(request):
    services = ServicesData.objects.all()
    return render(request,'durgasoft_services.html',{'services':services})


def enquiry_view(request):
    if request.method=='POST':
        eform = EnquryForm(request.POST)
        if eform.is_valid():
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            gender = eform.cleaned_data.get('gender')
            courses = eform.cleaned_data.get('courses')
            shifts = eform.cleaned_data.get('shifts')
            start_date = eform.cleaned_data.get('start_date')
            data = EnquiryData(
                name=name,
                mobile = mobile,
                email =  email,
                gender = gender,
                courses = courses,
                shifts = shifts,
                start_date = start_date
            )
            data.save()
            eform = EnquryForm()
            return render(request, 'durgasoft_contact.html', {'eform': eform})
        else:
            return HttpResponse('User invalid data')
    else:
        eform = EnquryForm()
        return render(request,'durgasoft_contact.html',{'eform':eform})


def gallary_view(request):
    return render(request,'durgasoft_gallary.html')


def feedback_view(request):
    if request.method=='POST':
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')
            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            feedbacks1 = FeedbackData.objects.all()
            fform = FeedbackForm()
            return render(request,'durgasoft_feedback.html',{'fform':fform,'feedbacks1':feedbacks1})
        else:
            return HttpResponse('user invalid data')
    else:
        feedbacks1 = FeedbackData.objects.all()
        fform = FeedbackForm()
        return render(request,'durgasoft_feedback.html',{'fform':fform,'feedbacks1':feedbacks1})

