from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import List
from django.core.paginator import Paginator
from django.db.models import Q





# Create your views here.
def home(request):
    lists = List.objects.all()
    
    
    search_term=''
    filter_item=''
    
    if 'search' in request.GET:#for searching
        search_term= request.GET['search']
        lists=lists.filter(Q(title__iexact=search_term)|Q(title__istartswith=search_term)|Q(title__iendswith=search_term))
    
    
    
    if 'filter' in request.GET:# for filtering
        filter_item=request.GET['filter']
        if filter_item =="all":
            paginator = Paginator(lists, 2) # Show 2 object per page
            page = request.GET.get('page')
            lists = paginator.get_page(page)
            contex={'list':lists}
            
            return render(request, 'lists/home.html',contex)
            
        
        else:
            lists=lists.filter(Q(level__iexact=filter_item))
        

    paginator = Paginator(lists, 2) # Show 2 object per page
    page = request.GET.get('page')
    lists = paginator.get_page(page)
    context ={'list': lists,'search_term':search_term,'filter_item':filter_item}
    
    return render(request, 'lists/home.html',context)
    
def detail(request, lists_id):
    detaillists = get_object_or_404(List, pk=lists_id)
    return render(request, 'lists/detail.html', {'lists':detaillists})

def mycourses(request):
    return render(request, 'lists/mycourses.html')

