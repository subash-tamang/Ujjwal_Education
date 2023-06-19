from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views import View
from .models import School, Contact
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

# def contact_page(request):
#     if request.method == "POST":
        
#         contact = ContactForm(request.POST)  # from request.POST, POST is the collected data of the post request 
        
#         if contact.is_valid():
#             # print(contact.cleaned_data)  # cleaned_data field of the forms.Form/ModelForm contains cleaned validated data in dictionary

#             # user_messgae = Contact(name=contact.cleaned_data["name"],  # Contact(name=contact.cleaned_data["user_name"] -> name is name of property in Contact model, "user_name" is name of property in ContactForm class
#             #                        message=contact.cleaned_data["message"],
#             #                        rating=contact.cleaned_data["rating"])
#             # user_messgae.save()

#             contact.save()
#             return HttpResponseRedirect("/thank-you/")
#     else:
#         contact = ContactForm()

#     return render(request, "schools/contact.html", {
#         "contact": contact,
#     })

#     # if request.method == "POST":
#     #     entered_username = request.POST["user-name"]

#     #     if entered_username == "":
#     #         return render(request, "schools/contact.html", {
#     #             "has_error": True
#     #         })
#     #     print(entered_username)
#     #     return HttpResponseRedirect("/thank-you/")
    
#     # return render(request, "schools/contact.html", {
#     #     "has_error": False
#     # })

class ContactPageView(View):
    def get(self, request):
        contact = ContactForm()

        return render(request, "schools/contact.html", {
            "contact": contact,
        })
    

    def post(self, request):
        contact = ContactForm(request.POST)  # from request.POST, POST is the collected data of the post request 
        
        if contact.is_valid():
            contact.save()
            return HttpResponseRedirect("/thank-you/")
        
        return render(request, "schools/contact.html", {
            "contact": contact,
        })


def thank_page(request):
    return render(request, "schools/thanks.html")