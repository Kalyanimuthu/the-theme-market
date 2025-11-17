from django.urls import path
from .import views


urlpatterns =[
    path('', views.home, name='home'),
    path('theme/', views.theme, name='theme'),
    path('templates/', views.templates, name='templates'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path("cart/add-ajax/<int:theme_id>/", views.add_to_cart_ajax, name="add_to_cart_ajax"),
    path("cart/update/<int:item_id>/<str:action>/", views.update_cart, name="update_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/empty/", views.empty_cart, name="empty_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("clear-cart-ajax/", views.clear_cart_ajax, name="clear_cart_ajax"),
]
