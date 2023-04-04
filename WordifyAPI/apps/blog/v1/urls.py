from django.urls import path

from .views import CategoryListCreateAPIView, TagListCreateAPIView, BlogListCreateAPIView, BlogRUDAPIView, \
    SubTextListCreateAPIView, SubPictureListCreateAPIView, CommentListCreateAPIView, SubTextRUDAPIView

urlpatterns = [
    path('category-list-create/', CategoryListCreateAPIView.as_view()),
    path('tag-list-create/', TagListCreateAPIView.as_view()),
    path('blog-list-create/', BlogListCreateAPIView.as_view()),
    path('blog-rud/<int:pk>/', BlogRUDAPIView.as_view()),
    path('blog/<int:blog_id>/comment-list-create/', CommentListCreateAPIView.as_view()),
    path('blog/<int:blog_id>/subtext-list-create/', SubTextListCreateAPIView.as_view()),
    path('blog/<int:pk>/subtext-rud/', SubTextRUDAPIView.as_view()),
    path('subtext/<int:blog_text_id>/subpicture-list-create/', SubPictureListCreateAPIView.as_view()),
]
