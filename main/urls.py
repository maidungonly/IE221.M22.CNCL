from django.urls import path

from . import views

urlpatterns = [
    # path("<int:id>",views.index,name="index"),
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    # path("create/",views.create,name="create"),
    path("giohang/",views.giohang,name="giohang"),
    path("kcook/",views.kcook,name="kcook"),
    path("giavisot/",views.giavisot,name="giavisot"),
    path("thucphamanlien/",views.thucphamanlien,name="thucphamanlien"),
    path("kcook/chitietkcook/", views.chitietkcook, name="chitietkcook"),
    path("thongtinmuahang/", views.thongtinmh, name="thongtinmuahang"),
    path("chitietsanpham/", views.chitietsanpham, name="chitietsanpham"),
]
 