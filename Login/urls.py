from django.urls import path
from Login import views


urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('servicios/', views.servicios, name="servicios"),
    path('contacto/', views.contacto, name="contacto"),
    path('tienda/', views.tienda, name="tienda"),


]