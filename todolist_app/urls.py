from todolist_app import views
from django.urls import path


urlpatterns = [
    path((''), views.todolist, name = 'todolist'),
    path(('delete/<task_id>'), views.delete, name = 'delete'), #<task_id> is used to pass a variable through url
    path(('edit/<task_id>'), views.edit, name = 'edit'),
    path(('completed/<task_id>'), views.completed, name = 'completed'),
    path(('pending/<task_id>'), views.pending, name = 'pending') #implementation of CRUD functionality (create,edit,delete,udpate)
    
    

]

