from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="index"),
    path('uniqueLink/<uuid:pk>', views.uniqueLink, name="uniqueLink"),
]
