from django.db.models import Q
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CategorySerializer, TagSerializer, BlogGETSerializer, BlogPOSTSerializer, SubTextSerializer, \
    SubPictureSerializer, CommentSerializer

from ..models import Category, Tag, Blog, SubText, SubPicture, Comment


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BlogListCreateAPIView(ListCreateAPIView):
    queryset = Blog.objects.order_by('-id')

    # serializer_class = BlogSerializer

    def get_queryset(self):
        tc = super().get_queryset()
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')
        tag_condition = Q()
        if tag:
            tag_condition = Q(tags__title__exact=tag)
        cat_condition = Q()
        if category:
            cat_condition = Q(category__title_exact=category)
        tc = tc.filter(tag_condition, cat_condition)

        return tc

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["author_id"] = self.kwargs.get("author_id")
        return ctx

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BlogGETSerializer
        if self.request.method == 'POST':
            return BlogPOSTSerializer


class BlogRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    # serializer_class = BlogPOSTSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tc = super().get_queryset()
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')
        tag_condition = Q()
        if tag:
            tag_condition = Q(tags__title__exact=tag)
        cat_condition = Q()
        if category:
            cat_condition = Q(category__title_exact=category)
        tc = tc.filter(tag_condition, cat_condition)

        return tc

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BlogGETSerializer
        if self.request.method == 'PUT':
            return BlogPOSTSerializer
        if self.request.method == 'PATCH':
            return BlogPOSTSerializer


class SubTextListCreateAPIView(ListCreateAPIView):
    queryset = SubText.objects.all()
    serializer_class = SubTextSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        blog_id = self.kwargs.get("blog_id")
        if blog_id:
            qs = qs.filter(blog_id=blog_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["blog_id"] = self.kwargs.get("blog_id")
        return ctx


class SubTextRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubText.objects.all()
    serializer_class = SubTextSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubPictureListCreateAPIView(ListCreateAPIView):
    queryset = SubPicture.objects.all()
    serializer_class = SubPictureSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        blog_text_id = self.kwargs.get("blog_text_id")
        if blog_text_id:
            qs = qs.filter(blog_text_id=blog_text_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["blog_text_id"] = self.kwargs.get("blog_text_id")
        return ctx


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        blog_id = self.kwargs.get('blog_id')
        if blog_id:
            qs = qs.filter(blog_id=blog_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['blog_id'] = self.kwargs.get('blog_id')
        return ctx
