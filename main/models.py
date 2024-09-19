from django.db import models

#Book, Author, Ganre
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Author(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Genre(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Book(BaseModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    ganre = models.ManyToManyField(Genre)
    pages = models.PositiveIntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title
