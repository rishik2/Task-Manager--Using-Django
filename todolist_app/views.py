from django.contrib.auth.signals import user_logged_in
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
# to check if the request is post or get (v imp we are working only on todolist app)
#all the functionality and template rendering is done on views through python and connecting it to html using jinja 2
        if request.method == "POST":
            form = TaskForm(request.POST or None)
            if form.is_valid():
                form.save( commit=False).manage = request.user
                form.save()
                messages.success(request, 'New Task Added. Best Of Luck')
        
                return redirect('todolist')
        else:
    # accessing all elemnets in a querty set from database named TaskList
            all_tasks = TaskList.objects.filter(manage = request.user)
            paginator = Paginator(all_tasks, 5) # Show 5 contacts per page.
            page = request.GET.get('pg')
            all_tasks = paginator.get_page(page)

            return render(request, 'todolist.html', {'all_tasks': all_tasks})
                      
            

#defining a function to delete a task, task_id is variable passed
@login_required
def delete(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.manage == request.user:
        task.delete()
    else:
         messages.error(request,("Access Restricted, You Are Not Allowed."))
    
    return redirect('todolist')

@login_required
def edit(request, task_id):
    if request.method == 'POST':
        task_obj = TaskList.objects.get(pk = task_id)
        form = TaskForm(request.POST or None, instance= task_obj) # using task_obj to get a specific object only
        
        if form.is_valid():
            form.save()
        
        messages.success(request,"Task Has Been Editied!" )
        return redirect('todolist')


    else:
        task_obj = TaskList.objects.get(pk = task_id) 
        return render(request, 'edit.html', {'task_obj':task_obj} )

@login_required
def completed(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    task.done = True
    if task.manage == request.user:
        task.save()
    else:
       messages.error(request,("Access Restricted, You Are Not Allowed.")) 

    return redirect('todolist')

@login_required
def pending(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    task.done = False
    task.save()
   
    return redirect('todolist')


@login_required
def index(request):
    
    context = {
        'home_page': " Hello Home Page welcomes you.",
    
    }
    return render(request, 'index.html', context)







def aboutus(request):
    
    context = {
        'aboutus': " Hello About Us welcomes you.",
    
    }
    return render(request, 'about us.html', context)

def contactus(request):
    context = {
        'contactus': " Hello Contact Us welcomes you.",
    
    }
    return render(request, 'contact us.html', context)