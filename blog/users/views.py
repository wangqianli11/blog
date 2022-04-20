from django.shortcuts import render
from django.views import View

# Create your views here.

class RegisterView(View):
    # 注册视图
    def get(self, request):
        return render(request, 'register.html')