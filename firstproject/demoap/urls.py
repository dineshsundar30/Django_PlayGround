from django.urls import path
from . import views
#app_name = "demoap"
urlpatterns = [path("", views.index, name='index'),
               path("contact/", views.contact, name='contact'),
               path("contactn/<int:phone_num>", views.contact_num, name="cantact_num"),
               path("newurl/",views.newurl, name="newurl"),
               path("oldurl/",views.oldurl, name="oldurl"),
               path("oldurl22/",views.oldurl, name="oldurl2")
               ]