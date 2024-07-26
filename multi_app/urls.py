from django.urls import path
from .views import register, login_view, logout_view,admin_dashboard,lawyer_dashboard,client_dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('lawyer_dashboard/', lawyer_dashboard, name='lawyer_dashboard'),
    path('client_dashboard/', client_dashboard, name='client_dashboard'),
]
