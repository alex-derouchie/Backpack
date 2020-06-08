from django.urls import path
from .views import InvListView, InvDetailView, InvCreateView, InvUpdateView, InvDeleteView, ItemDetailView, ItemDeleteView
from . import views

#######################################################################
# This file defines the URL patterns for the inv_manage app.
#######################################################################

urlpatterns = [
    path('', InvListView.as_view(), name='inv_manage-index'),
    path('shared/', views.SharedInvs, name='inv_manage-shared'),
    path('inv/<int:pk>/', InvDetailView.as_view(), name='inv_manage-detail'),
    path('inv/<int:pk>/update/', InvUpdateView.as_view(), name='inv_manage-update'),
    path('inv/<int:pk>/delete/', InvDeleteView.as_view(), name='inv_manage-delete'),
    path('inv/<int:pk>/new-item/', views.ItemCreateView, name='inv_manage-create-item'),
    path('item/<int:pk>/update/', views.ItemUpdateView, name='inv_manage-update-item'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='inv_manage-item-detail'),
    path('item/<int:pk>/delete', ItemDeleteView.as_view(), name='inv_manage-delete-item'),
    path('inv/new/', InvCreateView.as_view(), name='inv_manage-create'),
    path('inv/<int:pk>/share/', views.AddUserView, name='inv_manage-add-user'),
    path('about/', views.AboutView, name='inv_manage-about')
]