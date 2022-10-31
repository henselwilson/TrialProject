from django.urls import path
from Products.views import home_view,Phone_input_view,Phone_list_view,Phone_edit_view
from Products.api.views import make_order
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',home_view),
    path('auth/', obtain_auth_token),
    path('createPhone/',Phone_input_view),
    path('viewPhoneList/',Phone_list_view),
    path('edit/<int:id>',Phone_edit_view),
    path('order/', make_order)
]