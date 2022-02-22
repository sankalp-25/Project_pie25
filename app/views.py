from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import *
from django.contrib.staticfiles import finders
from .models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, FileResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings

# Create your views here.
def index(request):
    context={
        'varible':"This is the varible"  
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is home page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'index.html')
    #return HttpResponse("This is service page")

def Notes_it(request):
    return render(request, 'Notes_it.html')
    #return HttpResponse("This is IT service page")

def Notes_cse(request):
    return render(request, 'Notes_cse.html')
    #return HttpResponse("This is CSE service page")
def Notes_ece(request):
    return render(request, 'Notes_ece.html')

def Notes_eee(request):
    return render(request, 'Notes_eee.html')

def Notes_civil(request):
    return render(request, 'Notes_civil.html')

def Notes_mech(request):
    return render(request, 'Notes_mech.html')

def Notes_it_alc(request):
    return render(request, 'Notes_it_alc.html')

def Notes_it_dccn(request):
    return render(request, 'Notes_it_dccn.html')

def Notes_it_mpi(request):
    return render(request, 'Notes_it_mpi.html')

def Notes_it_os(request):
    return render(request, 'Notes_it_os.html')

def show_pdf1(request):
    country = request.GET['name1']
    x=country + ".pdf"
    filepath = os.path.join('static', x)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    
def show_pdf2(request):
    country = request.GET['name2']
    x=country + ".pdf"
    filepath = os.path.join('static', x)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def show_pdf3(request):
    country = request.GET['name3']
    x=country + ".pdf"
    filepath = os.path.join('static', x)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def show_pdf4(request):
    country = request.GET['name4']
    x=country + ".pdf"
    filepath = os.path.join('static', x)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def show_pdf5(request):
    country = request.GET['name5']
    x=country + ".pdf"
    filepath = os.path.join('static', x)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def show_pdf6(request):
    country = request.GET['name6']
    x=country + ".pdf"
    filepath = os.path.join('static', x)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


























# def payslip_view(request, employee):    
#     data = dict()
#     data["employee"] = employee
#     if "GET" == request.method:
#         return render(request, "appname/payslip.html", data)

#     # else for post call, procced
#     post_data = request.POST.copy()
#     year = post_data.get("year", None)
#     month = post_data.get("month", None)

#     if not year or not month:
#         messages.error(request, "Please select year and month.")
#         return HttpResponseRedirect(reverse("appname:payslip", args=(employee,)))

#     try:
#         filename = employee + ".pdf"
#         filepath = os.path.join(settings.MEDIA_ROOT, "payslips", year, month, filename)
#         print(filepath)
#         return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
#     except FileNotFoundError:
#         messages.error(request, "Payslip of Employee with Id " + employee + " doesn't exists for " + month + " " + year)
#         return HttpResponseRedirect(reverse("appname:payslip", args=(employee,)))

# from django.http import HttpResponse
# from django.shortcuts import render
# from django.template.loader import get_template

# Create your views here.
# def run(request):
#     country = request.GET['countrySelect']
#     print(country)
#     return HttpResponse("Completed."+country)

# def try(request):
#    return render(request, "try.html", {})