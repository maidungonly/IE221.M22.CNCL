from django.contrib import admin
from .models import KcookPost,Categrory,Product,Customer,OrderItem,Order,ShippingAddress

# Register your models here.

class KcookPostAdmin(admin.ModelAdmin):
    """điều chỉnh thông tin hiển thị của KcookPost trên trang quản lý database"""
    list_display = ('id','title_post','image','nguyenlieu','introduction','cachlam')

class CatAdmin(admin.ModelAdmin):
    """điều chỉnh thông tin hiển thị của Category trên trang quản lý database"""
    list_display = ('id','cat_name')


class ProductAdmin(admin.ModelAdmin):
    """điều chỉnh thông tin hiển thị của Product trên trang quản lý database"""
    list_display = ('id','product_name','image','price','slug','product_des','cat_name')



"""Điều chỉnh hiện module trên trang quản lý database"""
admin.site.register(KcookPost,KcookPostAdmin)
admin.site.register(Categrory,CatAdmin)
admin.site.register(Product,ProductAdmin)

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)

