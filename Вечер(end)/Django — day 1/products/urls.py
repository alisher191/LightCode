from django.urls import path

from .views import index, category_views, show_product, profile, basket_add, basket_remove

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', show_product, name='product'),
    path('category/<int:cat_id>', category_views, name='category'),
    path('profile/', profile, name='profile'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
  