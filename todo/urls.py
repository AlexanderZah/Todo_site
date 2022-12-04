from django.urls import path
from .views import (
    signupuser, createtodo, home,currenttodos, logoutuser, loginuser, edittodo, completetodo, deletetodo, completedtodos
)

urlpatterns = [
        ### AUTH ###
    path('signup/', signupuser, name='signupuser'),
    path('logout/', logoutuser, name='logoutuser'),
    path('login/',loginuser, name='loginuser'),
        ### todo pages ###
    path('current/',currenttodos, name='currenttodos' ),
    path('completedtodos/',completedtodos, name='completedtodos' ),
    path('create/', createtodo, name='createtodo'),
    path('home/', home, name='home'),
    path('todo/<int:todo_id>', edittodo, name='edittodo'),
    path('todo/<int:todo_id>/complete/', completetodo, name='completetodo'),
    path('todo/<int:todo_id>/delete', deletetodo, name='deletetodo'),
]
