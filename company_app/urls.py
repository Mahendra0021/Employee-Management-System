from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.Home,name='all-Employee'),
    # path('Add-Employee',views.home),
    path('all-Employee',views.All_Employee,name='all-Employee'),
    path('Add-Employee',views.Add_Employee,name='Add-Employee'),
    path('Remove-Employee',views.Remove_Employee,name='Remove-Employee'),
    path('Remove-Employee/<int:id>',views.Remove_Employee,name='Remove-Employee'),

    path('Filter-Employee',views.Filter_Employee,name='Filter-Employee'),

]