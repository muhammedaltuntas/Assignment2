from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    categoryname = models.CharField(max_length=75)
    isactive = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return '{}-{}'.format(self.id, self.categoryname)

class NewsPost(models.Model):
    category = models.ForeignKey(NewsCategory,on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    isactive = models.BooleanField()
    content = models.TextField()
    relase_date=models.DateTimeField(null=True)

    def __str__(self):
        return '{}-{}'.format(self.id, self.title)

class NewsPostComment(models.Model):
    post = models.ForeignKey(NewsPost,on_delete=models.CASCADE)
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    content = models.TextField()
    isactive = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return '{}-{}'.format(self.id,self.name)