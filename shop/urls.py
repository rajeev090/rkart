from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="Aboutus"),
    path("contact/", views.contact, name="ContactUs"),
    path("messages/", views.messages, name="messages"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productview, name="Productview"),
    path("checkout/", views.checkout, name="Checkout"),
    path("register/", views.register, name="register"),
    path("login/", views.loginuser, name="login"),
    path("cart/", views.cart, name="cart"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("handlerequest/", views.handlerequest, name="handlerequest")
    #path("logout/", views.logoutuser, name="logout")
]
