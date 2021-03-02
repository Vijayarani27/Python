from django.shortcuts import render
from django.http import HttpResponse
from .models import Developer
from django.shortcuts import get_object_or_404, render

def index(request):
    dev_list = Developer.objects.all()
    output = ', '.join([q.name for q in dev_list])
    return HttpResponse(output)
# Create your views here.
def detail(request, id):
    dev = get_object_or_404(Developer, pk=id)
    return render(request, 'ninjas/detail.html', {'dev': dev})