from django.shortcuts import render,redirect

from django.views import View
from .forms import PostForm
from .models import Blogs
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify









class BlogView(View):
    def get(self,request):
        return render(request,'blogs/blogs.html')
    def post(self,request):
        return render(request, 'blogs/blogs.html')

class CreatPostView(View):
    template_name='blogs/blogs.html'
    def get(self,request):
        form =PostForm
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blogs/blogs')
        return render(request,self.template_name,{'form':form})

class PostView(View):
    def get(self,request):
        posts=Blogs.objects.all()
        return render(request,'blogs/post_list.html',{'posts':posts})





