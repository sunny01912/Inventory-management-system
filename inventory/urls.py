from django.urls import path
from inventory import views
urlpatterns = [
    path('',views.index,name='index'),
    path('display_laptop/',views.display_laptop,name='display_laptops'),
    path('display_mobile/',views.display_mobile,name='display_mobiles'),
    path('display_desktop/',views.display_desktop,name='display_desktops'),
    path('add_laptop/',views.add_laptop,name='add_laptop'),
    path('add_mobile/',views.add_mobile,name='add_mobile'),
    path('add_desktop/',views.add_desktop,name='add_desktop'),
    path('edit_mobile/<int:id>/',views.edit_mobile,name='edit_mobile'),
    path('edit_laptop/<int:id>/',views.edit_laptop,name='edit_laptop'),
    path('edit_desktop/<int:id>/',views.edit_desktop,name='edit_desktop'),
    path('delete_mobile/<int:id>/',views.delete_mobile,name='delete_mobile'),
    path('delete_laptop/<int:id>/',views.delete_laptop,name='delete_laptop'),
    path('delete_desktop/<int:id>/',views.delete_desktop,name='delete_desktop'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),









]
