from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item/', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase-amount/<int:id>/', increase_amount, name='increase_amount'),
    path('decrease-amount/<int:id>/', decrease_amount, name='decrease_amount'),
    path('edit-item/<int:id>/', edit_item, name='edit_item'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
    path('get-item-json/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('delete-ajax/', delete_ajax, name='delete_ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
]