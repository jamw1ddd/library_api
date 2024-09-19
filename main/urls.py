from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AuthorView,GenreView,BookView

router = DefaultRouter()
router.register(r"authors",AuthorView,basename='author')
router.register(r"genres",GenreView,basename='genre')
router.register(r"books",BookView,basename='book')

urlpatterns = [
    path('',include(router.urls)),
]