from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Posting
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render


def todos_for_user(request):
    todos = Posting.objects.filter(user=request.user)
    return render(request, 'home.html', {'todos': todos})


class TodoDeleteView(DeleteView):
    model = Posting
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home',)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})


def login_page(request):
    return render(request, 'login.html',)
