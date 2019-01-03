from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mis_listas', views.mis_listas, name='mis_listas'),
    path('add_lista', views.add_lista, name='add_lista'),
    path('edit_lista/<int:lista_id>', views.edit_lista, name='edit_lista'),
    path('add_items/<int:lista_id>', views.add_items, name='add_items'),
    path('delete_lista/<int:lista_id>', views.delete_lista, name='delete_lista'),
    path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),
    path('toogle_cross/<int:item_id>', views.toogle_cross, name='toogle_cross'),
    path('signup/', views.signup, name='signup'),
]
