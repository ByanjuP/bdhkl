from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .models import Post,Destinations, Gallery, Hotel,Thingstodo
from .forms import PostCreateForm,DestinationForm, GalleyForm,UserLoginForm,ThingstodoForm
from django.contrib import  messages
from  django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.conf import ValidationError
from django.contrib.auth.views import PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView
from django.contrib.auth.models import User


def login(request):
    return render(request,'login.html')

@login_required()
def profile(request):
    if request.user.is_authenticated:
        myuser = request.user
        print(myuser)
    return render(request,'profile.html',context={'myuser':myuser})


#----------------------STUDENT OPERATION-----------------------------------------------
@login_required()
def test_form(request):
   students = TestModel.objects.all().order_by('student')
   paginator = Paginator(students,10)
   page_number = request.GET.get('pages')
   page_obj = paginator.get_page(page_number)
   if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            x = form.instance.student
            print(x)
            p = form.save(commit=False)
            p.save()
            messages.success(request,'Student "{}" has been succesfully added!'.format(x))
            return redirect('testform')

   elif request.method == 'GET' and 'testform-query' in request.GET:
       form = TestForm()
       query = request.GET.get('testform-query')
       print('The query is',query)
       students = TestModel.objects.filter(student__contains = query).order_by('student')
       paginator = Paginator(students, 6)
       page_number = request.GET.get('pages')
       page_obj = paginator.get_page(page_number)
       if query!= None:
          messages.success(request,'Search Results for {}!!'.format(query))

   else:
        form = TestForm()
   return render(request,'testform.html',  {'form':form,'students':page_obj})





@login_required()
def update_form(request,id):
    if request.method == 'POST': #defpost
        obj = TestModel.objects.get(pk = id)
        form = TestForm(request.POST,instance=obj)
        if form.is_valid():
            p = form.save(commit= False)
            p.date_posted = obj.date_posted
            p.save()
            messages.success(request,'Student "{}" was succesfully updated'.format(obj.student))
            return redirect('testform')
    else: #def get()
        obj = TestModel.objects.get(pk=id)
        print(obj.student)
        print('###')
        form = TestForm(instance=obj)

    return render(request,'testform_update.html',{'form':form})

@login_required()
def del_testform(request,id):
    if request.method == 'POST':
        obj = TestModel.objects.get(pk = id)
        student = obj.student
        obj.delete()
        messages.warning(request,'Student "{}" has been deleted succesfully!'.format(student))
    return redirect('testform')


def home(request):
    posts = Post.objects.all().order_by('-date_posted')[:7]
    destinations = Destinations.objects.all().order_by('date_posted')
    ttd = Thingstodo.objects.all().order_by('title')
    return render(request,'home.html',  {'posts':posts, 'destinations':destinations,'ttd':ttd})

#-------------------STUDENTOPERATION ENDS---------------------------------------------

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()[:10]
        context['name'] = 'Prashant'
        print(kwargs)
        #context ={'hotels':Hotel.objects.all()[:10]}
        return  context










@login_required(login_url='/login')
def dashboard(request):
    destinations = Destinations.objects.all().order_by('date_posted')
    return render( request,'dashboard.html',{'destinations': destinations})

def hotels(request):
    hotel_list = []
    for i in Hotel.objects.all():
        hotel_list.append(i.address)
    hotel_list = set(hotel_list)

    hotels = Hotel.objects.all()
    no_of_hotels = len(hotels)
    page = request.GET.get('page')
    paginator = Paginator(hotels, 10)
    try:
        hotels_p = paginator.page(page)
    except PageNotAnInteger:
        hotels_p = paginator.page(1)
    except EmptyPage:
        hotels_p = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        hotel_query = request.POST.get('location')
        hotels = Hotel.objects.filter(address__contains = hotel_query)
        no_of_hotels = len(hotels)
        page = request.GET.get('page')
        paginator = Paginator(hotels, 4)
        try:
            hotels_p = paginator.page(page)
        except PageNotAnInteger:
            hotels_p = paginator.page(1)
        except EmptyPage:
            hotels_p = paginator.page(paginator.num_pages)


    return render(request,'hotels.html',{'hotels':hotels_p,'no_of_hotels':no_of_hotels,'hotel_address':hotel_list})

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
    return render(request,'destination_create_form.html', {'form':form})


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

class AboutView(TemplateView):
    template_name = 'about.html'
    ViewCount = 0

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        AboutView.ViewCount += 1
        context['info'] = "The page name beautiful dhulikhel is established with the aim to promote  tourism in dhulikel"
        context['viewcount'] = AboutView.ViewCount
        return context


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'postcreateform.html'
    success_message = 'Post %(title)s is succesfully created'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



# ================   DESTINATIONS ================================================================================
class DestinationList(ListView):
    model = Destinations
    template_name = 'destinations.html'
    paginate_by = 10
    context_object_name = 'destinations'


class DestinationDetail(DetailView):
    model = Destinations
    template_name = 'destinations-detail.html'

    def get_context_data(self, **kwargs):
        context = super(DestinationDetail, self).get_context_data(**kwargs)
        current_object = self.get_object()
        context['destination_options'] = Destinations.objects.exclude(id = current_object.id)
        return  context



# ================   DESTINATIONS  ENDS ==========================================================================


#class listview
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 4



    def get_queryset(self):
        if self.request.GET.get('textinput'):
            x = self.request.GET.get('textinput')
            print('the input word is',x)
            if len(x)>=4:
                queryset = Post.objects.filter(title__contains = x).order_by('-date_posted')
                if queryset == None:
                    messages.warning('No Result Found')
                    return render(request,'postlist.html',{})
            else:
                queryset = Post.objects.all()[:1]
        else:
            queryset = Post.objects.all().order_by('-date_posted')
        return queryset



#class detailview
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_current_object = self.get_object()
        filtered_obj = Post.objects.exclude(id=get_current_object.id).order_by('-date_posted')
        context['posts'] = filtered_obj[:5]
        return context

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
    success_message = '%(title)s was updated!'
    template_name = 'postcreateform.html'
    success_url = '/'



    def form_valid(self, form):
        form.instance.author = self.request.user
        x = self.get_object()
        form.instance.date_posted = x.date_posted
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


#===============================================================================================================
@login_required()
def thingstodo_create(request):
    form = ThingstodoForm()
    if form.is_valid():
        form.save()
    return render(request,'thingstodo_add.html',{'form':form})
















