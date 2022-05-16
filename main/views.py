from itertools import product
from multiprocessing import context
from queue import PriorityQueue
from sqlite3 import Cursor
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, KcookPost, Product, Order, OrderItem,ShippingAddress
from django.http import JsonResponse
import json
from .utils import cookieCart,cartData,guestOrder
import datetime

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


# def home(response):
#     data = Product.objects.filter(pk__in = [14,15,16,19,18,22,27,28,29,24,25,30,10,11,13])

#     return render (response,"main/home.html",{'data':data})


def base(response):
    """render sườn chung dành cho các page"""
    return render(response, "main/base.html", {})
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
    """render trang kcook và truyền vào data là danh sách KcookPost đã được định nghĩa ở models.py"""

    cartdata=cartData(response)
    cartItems = cartdata['cartItems']
    data = KcookPost.objects.all().order_by('-id')
    return render(response, "main/kcook.html", {'data': data,'cartItems':cartItems})


def chitietkcook(response, id):
    """render trang chi tiết kcook thể hiện thông tin từng KcookPost"""
    cartdata=cartData(response)
    cartItems = cartdata['cartItems']
    kcook_post = KcookPost.objects.get(id=id)
    # kcook_post = KcookPost.objects.get(id = kcook_post_id)
    # data=KcookPost.objects.filter(id=kcook_post).order_by('-id')
    return render(response, "main/chitietkcook.html", {'data': kcook_post,'cartItems':cartItems})


def home(response):
    """render trang home, truyền vào data Product"""
    cartdata=cartData(response)
    cartItems = cartdata['cartItems']
    
    banchay = Product.objects.filter(pk__in = [47,37,41,51,54,62,64,71,81,15])
    giavisot = Product.objects.filter(cat_name = 2)[:5]
    banhkeo = Product.objects.filter(cat_name = 1)[:5]
    rongbien = Product.objects.filter(cat_name = 5)[:5]
    douong = Product.objects.filter(cat_name = 4)[:5] 
    anlien = Product.objects.filter(cat_name = 6)[:5]
    context = {'banchay': banchay, 'cartItems': cartItems,'giavisot':giavisot,'banhkeo':banhkeo,'rongbien':rongbien,'douong':douong,'anlien':anlien}
    # data = Product.objects.all()

    return render(response, "main/home.html",context)



def thucphamanlien(response):
    """render trang thực phẩm ăn liền, truyền vào data là Product với CategoryId=6 (vì id=6 là thực phẩm ăn liền)"""
    cartdata=cartData(response)
    cartItems = cartdata['cartItems']
    data = Product.objects.filter(cat_name=6)
    return render(response, "main/thucphamanlien.html", {'data': data,'cartItems':cartItems})


def giavisot(response):
    """render trang gia vị và sốt, truyền vào data là Product với CategoryId=2 (vì id=2 là gia vị và sốt)"""
    cartdata=cartData(response)
    cartItems = cartdata['cartItems']
    data = Product.objects.filter(cat_name=2)
    return render(response, "main/giavisot.html", {'data': data,'cartItems':cartItems})


def douong(response):
    """render trang đồ uống, truyền vào data là Product với CategoryId=4 (vì id=4 là đồ uống)"""
    cartdata=cartData(response)
    cartItems = cartdata['cartItems']
    data = Product.objects.filter(cat_name=4)
    return render(response, "main/douong.html", {'data': data,'cartItems':cartItems})


def banhkeo(response):
    """render trang bánh kẹo, truyền vào data là Product với CategoryId=1 (vì id=1 là bánh kẹo)"""
    cartdata=cartData(response)
    cartItems = cartdata['cartItems']
    data = Product.objects.filter(cat_name=1)
    return render(response, "main/banhkeo.html", {'data': data,'cartItems':cartItems})


def rongbien(response):
    """render trang rong biển, truyền vào data là Product với CategoryId=5 (vì id=5 là rong biển)"""
    cartdata=cartData(response)
    cartItems = cartdata['cartItems']


    data = Product.objects.filter(cat_name=5)
    return render(response, "main/rongbien.html", {'data': data,'cartItems':cartItems})
# def thongtinmh(response):
#     """render trang thông tin mua hàng"""
#     return render(response,"main/thongtinmh.html",{})


def search(request):
    """render trang search, trang này sẽ hiện kết quả khi người dùng nhập từ khóa vào ô search"""
    cartdata=cartData(request)
    cartItems = cartdata['cartItems']

    if request.method == "POST":
        searched = request.POST['searched']
        product = Product.objects.filter(product_name__contains=searched)
        return render(request, 'main/search.html', {'searched': searched, 'product': product,'cartItems':cartItems})
    else:
        return render(request, 'main/search.html', {'cartItems':cartItems})


def updateItem(request):
    """thực hiện chức năng cập nhật sản phẩm đối với người có tài khoản đăng nhập, ở đây chỉ là tài khoản admin quản lý database"""
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def chitietsanpham(request, slug):
    """render trang chi tiết sản phẩm"""
    cartdata=cartData(request)
    cartItems = cartdata['cartItems']

    data = Product.objects.get(slug=slug)
    context = {'products': data, 'cartItems': cartItems}
    return render(request, 'main/chitietsanpham.html', context)


def giohang(request):
    """render trang giỏ hàng"""
    cartdata=cartData(request)
    cartItems = cartdata['cartItems']
    items = cartdata['items']
    order= cartdata['order']


    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'main/giohang.html', context)


def thongtinmh(response):
    """render trang thông tin mua hàng"""
    cartdata=cartData(response)
    cartItems = cartdata['cartItems']
    items = cartdata['items']
    order= cartdata['order']

    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(response, 'main/thongtinmh.html', context)

def processOrder(request):
    print('Data:',request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
       
    else:
        customer,order = guestOrder(request,data)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True

    order.save()

    ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address = data['shipping']['address']
        )
    return JsonResponse('Payment submitted..', safe=False)