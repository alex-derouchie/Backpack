from django.urls import path
from .views import InvListView, InvDetailView, InvCreateView, InvUpdateView, InvDeleteView, ItemDetailView
from . import views



urlpatterns = [
    path('', InvListView.as_view(), name='inv_manage-index'),
    path('shared/', views.SharedInvs, name='inv_manage-shared'),
    path('inv/<int:pk>/', InvDetailView.as_view(), name='inv_manage-detail'),
    path('inv/<int:pk>/update/', InvUpdateView.as_view(), name='inv_manage-update'),
    path('inv/<int:pk>/delete/', InvDeleteView.as_view(), name='inv_manage-delete'),
    path('inv/<int:pk>/new-item/', views.ItemCreateView, name='inv_manage-create-item'),
    path('inv/<int:pk>/share/', views.AddUserView, name='inv_manage-add-user'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='inv_manage-item-detail'),
    path('inv/new/', InvCreateView.as_view(), name='inv_manage-create'),
    path('about/', views.About, name='inv_manage-about')
]