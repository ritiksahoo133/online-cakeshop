from django.urls import path
from UserApp import views 
urlpatterns = [
path('',views.Home),
path('showCakes/<cid>',views.showCakes),
path('showDetails/<cid>',views.showDetails),
path('Signup',views.Signup),
path("Login",views.Login),
path("Logout",views.Logout),
path("showAllCartItems",views.showAllCartItems),
path("MakePayment",views.MakePayment),
]
