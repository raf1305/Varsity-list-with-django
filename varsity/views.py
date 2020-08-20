from django.shortcuts import render
from .models import Varsity
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.


def index(request):

    return render(request, 'varsity/index.html')


def public(request):
    var = Varsity.objects.filter(category="Public").order_by('foundation')
    # print(var)
    params = {'var': var}
    return render(request, 'varsity/public.html', params)


def private(request):
    var = Varsity.objects.filter(category="Private").order_by('foundation')
    # print(var)
    params = {'var': var}
    return render(request, 'varsity/private.html', params)


def individual(request, nick):
    var = Varsity.objects.filter(univarsity_nickname=nick)
    # print(var)
    params = {'var': var[0]}
    return render(request, 'varsity/individual.html', params)


def search(request):
    if request.method=="POST":
            name = request.POST.get('search', '')        
            var=Varsity.objects.filter(Q(univarsity_nickname=name)|Q(univarsity_name__contains=name)|Q(location__contains=name)).order_by('-category')
            params = {'var': var}
    # params={'var':var[0]}
    # return render(request,'varsity/individual.html',params)
    return render(request, 'varsity/search.html',params)

    # return HttpResponse("Hello")

def engineering(request):
    var = Varsity.objects.filter(specailization="Engineering").order_by('-category','foundation')
    # print(var)
    params = {'var': var,'speciality':'Enginerring'}
    return render(request, 'varsity/private.html', params)
def agricultural(request):
    var = Varsity.objects.filter(specailization__contains="Agricultural").order_by('-category','foundation')
    # print(var)
    params = {'var': var,'speciality':'Agricultural'}
    return render(request, 'varsity/private.html', params)
def science(request):
    var = Varsity.objects.filter(Q(specailization__contains="technology")|Q(specailization="STEM")).order_by('-category','foundation')
    # print(var)
    params = {'var': var,'speciality':'Science & Technology'}
    return render(request, 'varsity/private.html', params)
def general(request):
    var = Varsity.objects.filter(specailization="General").order_by('-category','foundation')
    # print(var)
    
    params = {'var': var,'speciality':'General'}
    return render(request, 'varsity/private.html', params)