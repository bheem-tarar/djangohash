from rest_framework import viewsets
from .models import Category, Tag, Post, Comment, Contact
from blog.serializers import CategorySerializer,TagSerializer,PostSerializer,CommentSerializer,ContactSerializer

class Categortyapiviews(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class Tagapiviews(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class Postapiviews(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class Commentapiviews(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class Contactapiviews(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
