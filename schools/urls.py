from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main-page"),
    path("schools/", views.schools_page, name="schools-page"),
    path("schools/<int:id>/", views.school_detail_page, name="school-detail"),
    path("contact/", views.ContactPageView.as_view(), name="contact-page"),
    path("thank-you/", views.thank_page),
]
