from rest_framework import serializers
from .models import Category, Tag, Post, Comment, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'slug', 'timestamp', 'utimestamp', 'track', 'utrack', 'status']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'timestamp', 'utimestamp', 'track', 'utrack', 'status']

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'description', 'slug', 'author', 'thumbnail', 'feature_image', 'content', 
            'created_at', 'updated_at', 'published_date', 'timestamp', 'utimestamp', 'track', 'utrack', 
            'status', 'category', 'tags'
        ]

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'email', 'message', 'created_at', 'parent', 'timestamp', 'utimestamp', 'track', 'utrack', 'status']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'subject', 'message', 'created_at', 'timestamp', 'utimestamp', 'track', 'utrack', 'status']
