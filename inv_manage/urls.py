from django.urls import path
from .views import InvListView, InvDetailView, InvCreateView, InvUpdateView, InvDeleteView, UserInvListView
from . import views



urlpatterns = [
    path('', InvListView.as_view(), name='inv_manage-index'),
    path('user/<str:username>', UserInvListView.as_view(), name='inv_manage-user_invs'),
    path('inv/<int:pk>/', InvDetailView.as_view(), name='inv_manage-detail'),
    path('inv/<int:pk>/update/', InvUpdateView.as_view(), name='inv_manage-update'),
    path('inv/<int:pk>/delete/', InvDeleteView.as_view(), name='inv_manage-delete'),
    path('inv/<int:pk>/new-item/', views.ItemCreateView, name='inv_manage-create-item'),
    path('inv/new/', InvCreateView.as_view(), name='inv_manage-create'),
    path('about/', views.about, name='inv_manage-about')
]