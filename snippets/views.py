from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action





class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer    


class SnippetViewSet(viewsets.ModelViewSet):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)    



# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })
#     return Response(snippet.highlighted)

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#     


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class SnippetList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly]
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)



# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly]
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer



