from django.shortcuts import render
from django.views import View

# Create your views here.

# def dashboard(request):
#     return render(request, 'scraper/dashboard.html',
#     {})


class DashboardView(View):
    template_name = 'scraper/dashboard.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST.get('action', ""))
        if request.POST.get('action', "") == "scan":
            print("scanning...")
            render(request, self.template_name)
        else:
            render(request, self.template_name)