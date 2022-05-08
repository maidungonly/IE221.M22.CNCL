from django.contrib import admin
from .models import KcookPost

# Register your models here.

class KcookPostAdmin(admin.ModelAdmin):
    list_display = ('id','title_post','image','nguyenlieu','introduction','cachlam')


admin.site.register(KcookPost,KcookPostAdmin)
