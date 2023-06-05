from django.shortcuts import render
from django.http import Http404
from .models import School
from .forms import ContactForm

# Create your views here.
def main_page(request):
    return render(request, "schools/main_page.html")

def schools_page(request):
    schools = School.objects.all().order_by("name")
    return render(request, "schools/all_schools.html", {
        "schools": schools,
    })

def school_detail_page(request, id):
    try:
        school = School.objects.get(pk=id)
    except:
        raise Http404
    return render(request, "schools/school_detail.html", {
        "school": school,
    })

def contact_page(request):
    contact = ContactForm()
    return render(request, "schools/contact.html", {
        "contact": contact,
    })