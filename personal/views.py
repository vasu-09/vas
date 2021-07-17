from django.shortcuts import render
from .models import Question
from django.http import JsonResponse
# Create your views here.
def home(request):
	return render(request,'personal/home1.html')

def home2(request):
	context={}
	q=Question.objects.all()
	context['question']=q
	return render(request,'personal/home.html', context)

