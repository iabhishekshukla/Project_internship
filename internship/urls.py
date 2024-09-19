from django.urls import path,include
from .import views,provider_views
urlpatterns=[
    path("",views.home),
    path("about/",views.about_internship),
    path("feedback/",views.feedback),
    path("contactus/",views.contactus,name="contactus"),
    path("login/",provider_views.login,name="login"),
    path("registration/",views.registration,name="registration"),
    path("providercourse/",provider_views.providercourse),
    path("providerviewcourse/",provider_views.providerviewcourse),
    path("providerviewprofile/",provider_views.providerviewprofile),
    path("providereditprofile/",provider_views.providereditprofile),
    path("providercourse/",provider_views.providercourse),
    path("notice/",views.notice),
]