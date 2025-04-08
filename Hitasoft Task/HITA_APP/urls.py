from django.urls import path
from .views import RegisterView, LoginView, LogoutView, TaskCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('pro/', ProtectedView.as_view(), name='logout'),

    path('tasks/', TaskCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
]
