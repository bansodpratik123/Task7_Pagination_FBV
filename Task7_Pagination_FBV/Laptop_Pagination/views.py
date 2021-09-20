from django.shortcuts import render
from .models import Laptops

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def homepage(request):
    return render(request,'Homepage.html',{})


def showlaptops(request):
    records=Laptops.objects.all()
    rec_per_page=Paginator(records,2)
    print('PAGINATOR=', rec_per_page)

    page=request.GET.get('page',1)
    print('PAGE=',page)
    print(rec_per_page.count)
    print(rec_per_page.num_pages)
    print(rec_per_page.page_range)

    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)

    return render(request,'ShowLaptops.html',{'records':rec})














# def showlaptops(request):
#     records=Laptops.objects.all()
#     paginate=Paginator(records,3)
#     page_show=request.GET.get('page')
#
#     try:
#         rec = paginate.page(page_show)
#     except PageNotAnInteger:
#         rec = paginate.page(1)
#     except EmptyPage:
#         rec = paginate.page(paginate.num_pages)
#
#     # return render(request, 'studentpages/show.html', {'posts': posts})
#     return render(request,'Laptops_list.html',{'rec':rec})