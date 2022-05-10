from queue import PriorityQueue
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import KcookPost,Product

# def index(response,id):
#     ls = ToDoList.objects.get(id = id)
#     # {"save":["save"], "c1":["clicked"]}
#     if response.method == "POST":
#         print(response.POST)
#         if response.POST.get("save"):
#             for item in ls.item_set.all():
#                 if response.POST.get(("c"+str(item.id)) == "clicked"):
                    
#                     item.complete = True
#                 else:
#                     item.complete = False

#                 item.save()


#         elif response.POST.get("newItem"):
#             txt = response.POST.get("new")
#             if len(txt) >2 :
#                 ls.item_set.create(text = txt,complete = False)
#             else:
#                 print("invalid Input")

#     return render (response,"main/list.html",{"ls":ls})


def home(response):
    data = Product.objects.filter(pk__in = [14,15,16,19,18,22,27,28,29,24,25,30,10,11,13])

    return render (response,"main/home.html",{'data':data})


def base(response):
    return render (response,"main/base.html",{})
# def create(response):
#     if response.method == "POST":
#         form = CreateNewList(response.POST)
#         if form.is_valid():
#             n=form.cleaned_data["name"]
#             t= ToDoList(name=n)
#             t.save()
        
#         return HttpResponseRedirect("/%i" %t.id)

#     else:
#         form = CreateNewList()
#     return render(response,"main/create.html",{"form":form}) 

def giohang(response):
    return render(response,"main/giohang.html",{})

def kcook(response):
    data = KcookPost.objects.all().order_by('-id')
    return render(response,"main/kcook.html",{'data':data})

def chitietkcook(response,id):
    kcook_post = KcookPost.objects.get(id=id)
    # kcook_post = KcookPost.objects.get(id = kcook_post_id)
    # data=KcookPost.objects.filter(id=kcook_post).order_by('-id')
    return render(response,"main/chitietkcook.html",{'data':kcook_post})

def home(response):
    # data = Product.objects.filter(pk__in = [14,15,16,19,18,22,27,28,29,24,25,30,10,11,13])
    data = Product.objects.all()

    return render (response,"main/home.html",{'data':data})

def chitietsanpham(response,slug):
    data = Product.objects.get(slug=slug)
    # chitietsanpham_post = Product.objects.get(id=id)
    # chitietsanpham_post = get_object_or_404(Product, slug=slug)
    # data = Product.objects.get(slug=slug)
    return render(response,"main/chitietsanpham.html",{'data':data})

def thucphamanlien(response):
    data = Product.objects.filter(cat_name = 6)
    return render(response,"main/thucphamanlien.html",{'data':data})
def giavisot(response):
    data = Product.objects.filter(cat_name = 2)
    return render(response,"main/giavisot.html",{'data':data})
def douong(response):
    data = Product.objects.filter(cat_name = 4)
    return render(response,"main/douong.html",{'data':data})
def banhkeo(response):
    data = Product.objects.filter(cat_name = 1)
    return render(response,"main/banhkeo.html",{'data':data})
def rongbien(response):
    data = Product.objects.filter(cat_name = 5)
    return render(response,"main/rongbien.html",{'data':data})
def thongtinmh(response):
    return render(response,"main/thongtinmh.html",{})


