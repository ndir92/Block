from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
# Create your views here.



def register(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('posts:index')
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
        
    context = {
            'form': form,
        }
        
    return render(request,'compte/register.html',context)