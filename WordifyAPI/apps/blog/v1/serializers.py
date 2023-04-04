from rest_framework import serializers

from ..models import Category, Tag, Blog, SubText, SubPicture, Comment

from apps.account.models import Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class MiniBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title']


class MiniSubPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPicture
        fields = ['id', 'blog_text', 'image', 'is_vite']


class MiniSubTextSerializer(serializers.ModelSerializer):
    subpicture = MiniSubPictureSerializer(read_only=True, many=True)

    class Meta:
        model = SubText
        fields = ['id', 'blog', 'description', 'subpicture']


class MiniCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'blog', 'description', 'created_at']


class BlogGETSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    subtext = MiniSubTextSerializer(read_only=True)
    comments = MiniCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'category', 'image', 'description', 'subtext', 'tags', 'comments', 'views',
                  'created_at']


class BlogPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'category', 'image', 'description', 'tags', 'views',
                  'created_at']
        extra_fields = {
            'author': {"required": False},
            'views': {"read_only": True},
        }

    def create(self, validated_data):
        request = self.context['request']
        author_id = request.user.profile_user.id
        instance = super().create(validated_data)
        instance.author_id = author_id
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    blog = MiniBlogSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'blog', 'description', 'created_at']

        extra_kwargs = {
            "blog": {'required': False},
        }

    def create(self, validated_data):
        request = self.context['request']
        blog_id = self.context['blog_id']
        author_id = request.user.profile_user.id
        description = validated_data.get('description')
        instance = Comment.objects.create(blog_id=blog_id, author_id=author_id, description=description)
        return instance


class SubPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPicture
        fields = ['id', 'image', 'is_vite']

    def create(self, validated_data):
        request = self.context['request']
        blog_text_id = self.context['blog_text_id']
        image = validated_data.get('image')
        instance = SubPicture.objects.create(blog_text_id=blog_text_id, image=image)
        return instance


class SubTextSerializer(serializers.ModelSerializer):
    subpicture = MiniSubPictureSerializer(read_only=True, many=True)

    class Meta:
        model = SubText
        fields = ['id', 'blog', 'description', 'subpicture']

    def create(self, validated_data):
        request = self.context['request']
        blog_id = self.context['blog_id']
        description = validated_data.get('description')
        instance = SubText.objects.create(blog_id=blog_id, description=description)
        return instance
