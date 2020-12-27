from django.shortcuts import render,redirect
from .models import Post,Destinations
from .forms import PostCreateForm,DestinationForm
from django.contrib import  messages
from  django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,UpdateView,CreateView



def home(request):
    posts = Post.objects.all().order_by('-date_posted')[:6]
    destinations = Destinations.objects.all().order_by('date_posted')[:6]
    return render(request,'home.html',  {'posts':posts, 'destinations':destinations})


@login_required()
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '%(title)s is created Successfully!')
            return redirect('home')

    else:
        form = PostCreateForm()
    return render(request, 'postcreateform.html', {'form': form})


@login_required()
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST,request.FILES )
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,'Destination is  created succesfully!')
            return redirect('home')

    else:
        form = DestinationForm()
    return render(request,'destination_create_form.html',{'form':form})


#class view begins here

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 6

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



















