from django.shortcuts import render
from blog.models import Post
from rest_framework import serializers

# Create your views here.
class PostSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'created','comment']
        
    def get_comment(self, obj):
        return obj.comments.values('id', 'text').last()
