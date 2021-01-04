from django.shortcuts import render,redirect
from .models import Post,Destinations, Gallery
from .forms import PostCreateForm,DestinationForm, GalleyForm
from django.contrib import  messages
from .models import Post
from  django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    posts = Post.objects.all().order_by('-date_posted')[:6]
    destinations = Destinations.objects.all().order_by('date_posted')[:6]
    return render(request,'home.html',  {'posts':posts, 'destinations':destinations})


@login_required(login_url='/login')
def dashboard(request):
    destinations = Destinations.objects.all().order_by('date_posted')
    return render( request,'dashboard.html',{'destinations': destinations})


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


@login_required()
def gallerycreate(request):
    if request.method == 'POST':
        form = GalleyForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,'Picture has been added succesfully')
            return redirect('home')
    else:
            form = GalleyForm()
    return render(request,'galleryadd.html', {'form': form})
def gallery(request):
    gallery = Gallery.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})



#class view begins here

class PostCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'postcreateform.html'
    success_message = 'Post %(title)s is succesfully created'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#class listview
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 6

#class detailview
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

#class delete view
class PostDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/'
    success_message = '%(title)s has been deleted!'

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return false

#class updateview
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = Post
    form_class = PostCreateForm
    success_message = '%(title)s was updated succesfully!'
    template_name = 'postcreateform.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False






















