from django.urls import path
from .views import product_create_view,dynamic_lookup_view,delete_suc,delete_my_object,product_list_view
app_name="product"
urlpatterns = [
    path('create/',product_create_view),
    path('<int:id>/',dynamic_lookup_view, name="product-details"),
    path('<int:id>/delete',delete_my_object),
    path('delete/suc',delete_suc ,name="success"),
    path("list",product_list_view)
]