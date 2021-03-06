from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('cart/',views.cart,name='cart'),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
    path('shop_single/',views.shop_single,name='shop_single'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
    path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
    path('seller_delete_product/<int:pk>/',views.seller_delete_product,name='seller_delete_product'),
    path('collection_men/',views.collection_men,name='collection_men'),
    path('collection_women/',views.collection_women,name='collection_women'),
    path('collection_kids/',views.collection_kids,name='collection_kids'),
    path('color_red/',views.color_red,name='color_red'),
    path('color_blue/',views.color_blue,name='color_blue'),
    path('product_detail/<int:pk>/',views.product_detail,name='product_detail'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
    path('change_qty/',views.change_qty,name='change_qty'),
    path('pay/', views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),
    path('myorders/',views.myorders,name='myorders'),
    path('ajax/validate_email/',views.validate_signup,name='validate_email'),
]