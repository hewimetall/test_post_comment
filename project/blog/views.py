from blog.serializers import PostSerializer
from blog.models import Post
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        post.count +=1
        post.save(update_fields=['count'])
        serializer = self.serializer_class(post)
        return Response(serializer.data)
