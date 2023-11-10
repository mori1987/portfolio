from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Portfolio


class PortfolioView(View):
    def get(self,request):
        portfolio_items = Portfolio.objects.all()
        return render(request, 'portfolio/portfolio.html', {'portfolio_items': portfolio_items})
    def post(self,request):
        pass


# class PortfolioPostView(View):
#     template_name='potfolio/portfolio.html'

    # def get(request):
    #     portfolio_items = Portfolio.objects.all()
    #     return render(request, 'portfolio/portfolio.html', {'portfolio_items': portfolio_items})
