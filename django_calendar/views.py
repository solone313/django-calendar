from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import View
# Create your views here.
class MakeMonthly(View):  
    def get(self, request):
        # 뷰 로직 작성
        return HttpResponse('result')