from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class AboutView(View):
    def get(self,request):
        return render(request,'about/about.html')
    def post(self,request):
        pass
