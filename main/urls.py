from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static  
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
    path('kcook-post-list/<int:id>',views.chitietkcook,name='chitietkcook'),
    path("kcook/chitietkcook/", views.chitietkcook, name="chitietkcook"),
    path("thongtinmuahang/", views.thongtinmh, name="thongtinmuahang"),
    path("chitietsanpham/", views.chitietsanpham, name="chitietsanpham"),
]
 
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  