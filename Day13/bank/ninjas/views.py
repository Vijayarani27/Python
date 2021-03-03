from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Developer,Skill
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'ninjas/index.html'
    context_object_name = 'dev_list'

    def get_queryset(self):
        return Developer.objects.all()
'''
def index(request):
    dev_list = Developer.objects.all()
    return render(request, 'ninjas/index.html', {'dev_list':dev_list})
'''

def detail(request, id):
    dev = get_object_or_404(Developer, pk=id)
    return render(request, 'ninjas/detail.html', {'dev': dev})

def results(request, id):
    dev = get_object_or_404(Developer, pk=id)
    return render(request, 'ninjas/results.html', {'dev': dev})
'''
class DetailView(generic.DetailView):
    model = Developer
    template_name = 'ninjas/detail.html'

class ResultsView(generic.DetailView):
    model = Developer
    template_name = 'ninjas/results.html'
'''

def vote(request,id):
    dev = get_object_or_404(Developer, pk=id)
    print(dev.name)
    try:
        selected_skill = dev.skill_set.get(pk=request.POST['skill'])
    except (KeyError, Skill.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'ninjas/detail.html', {
            'dev': dev,
            'error_message': "You didn't select a skill.",
        })
    else:
        selected_skill.level += 1
        selected_skill.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('ninjas:results', args=(dev.id,)))  