from django.db import models

# Create your models here.
# class ToDoList(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Item (models.Model):
#     todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)
#     complete = models.BooleanField()
#     def __str__(self):
#         return self.text

class KcookPost(models.Model):
    title_post=models.TextField()
    image = models.ImageField(upload_to = "kcookpost_imgs/")
    nguyenlieu = models.TextField()
    introduction = models.CharField(max_length=350,null=True)
    cachlam = models.TextField()

    def __str__(self):
        return self.title_post

