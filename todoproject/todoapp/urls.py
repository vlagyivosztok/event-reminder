from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('new/', views.EventCreateView.as_view(), name='event_create'),
    path('ajax/create-person/', views.ajax_create_person, name='ajax_create_person'),
    path('ajax/create-main-category/', views.ajax_create_main_category, name='ajax_create_main_category'),
    path('ajax/create-subcategory/', views.ajax_create_subcategory, name='ajax_create_subcategory'),
]
