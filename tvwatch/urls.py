from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_interest",views.add_interest, name ="add_interest"),
    path("reccomended",views.reccomended, name ="reccomended"),
    path("detail",views.detail_view, name ="detail_view"),
    path("add_mylist",views.add_mylist, name ="add_mylist"),
    path("mylist",views.mylist, name ="mylist"),
    path("remove",views.remove_mylist, name ="remove_mylist"),
    path("about", views.about_view, name="about"),
    path("newsletter", views.newsletter, name="newsletter")
]
