from django.urls import path
from .views import IndexView
from django.contrib.auth.views import LoginView,LogoutView
from .views import IndexView, SignupView, custom_logout, UploadImageView

app_name = "giffy_app"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
    path('login/', LoginView.as_view( 
        template_name="giffy_app/login.html",
        next_page="giffy+app:index",
        redirect_authenticated_user=True,
        ),
         name='login',),
    
    path('logout/', custom_logout,
         name='logout'),
    
    path('signup/', SignupView.as_view(), name='signup'),
    
    path('upload/', UploadImageView.as_view(), name='upload'),
]