from multiprocessing import context
from queue import PriorityQueue
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import KcookPost,Product,Order,OrderItem
from django.http import JsonResponse
import json

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

# def giohang(response):
#     return render(response,"main/giohang.html",{})

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

# def chitietsanpham(response,slug):
#     data = Product.objects.get(slug=slug)
#     # chitietsanpham_post = Product.objects.get(id=id)
#     # chitietsanpham_post = get_object_or_404(Product, slug=slug)
#     # data = Product.objects.get(slug=slug)
#     return render(response,"main/chitietsanpham.html",{'data':data})

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
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        product = Product.objects.filter(product_name__contains= searched)
        return render(request,'main/search.html', {'searched':searched, 'product': product})
    else:
        return render(request,'main/search.html', {})
             

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
   
def chitietsanpham(request,slug):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items =[]
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']

    data = Product.objects.get(slug=slug)
    context = {'products':data,'cartItems':cartItems}
    return render(request,'main/chitietsanpham.html',context)


def giohang(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart ={}
        print('Cart:',cart)

        items =[]
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        
        for i in cart:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id = i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item ={
                'product':{
                    'id':product.id,
                    'product_name':product.product_name,
                    'price':product.price,
                    'image':product.image
                    },
                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            items.append(item)

    
    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request,'main/giohang.html',context)


def thongtinmuahang(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items =[]
        order = {'get_cart_total':0,'get_cart_items':0}
        # cartItems = order['get_cart_items']

    
    context = {'items':items,'order':order}
    return render(request,'main/thongtinmh.html',context)



    
  