from rest_framework import generics
from .models import Category, Tag, Author, About, Comment, Post, Resume, Skills, Service, Project, Contact, \
    ContactInfo
from .serializers import CommentSerializer, TagSerializer, AuthorSerializer, AboutSerializer, CategorySerializer, \
    ContactSerializer, ContactInfoSerializer, ServiceSerializer, ProjectSerializer, PostSerializer, \
    ResumeSerializer, SkillsSerializer


# Create your views here.


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ResumeView(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class SkillsView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ContactInfoView(generics.ListAPIView):
    queryset = ContactInfo.objects.all().order_by('-id')[:1]
    serializer_class = ContactInfoSerializer


class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        q = self.request.query_params.get('q')

        if tag:
            return Post.objects.filter(tags__name=tag)
        if category:
            return Post.objects.filter(category__name=category)
        if q:
            return Post.objects.filter(title__icontains=q)
