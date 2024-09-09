from django.urls import path
from .views import *

urlpatterns = [
    path('', PostView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('category/', CategoryView.as_view(), name='category-list'),
    path('tag/', TagView.as_view(), name='tags'),
    path('skills/', SkillsView.as_view(), name='skills-list'),
    path('resume/', ResumeView.as_view(), name='resume-list'),
    path('service/', ServiceView.as_view(), name='services'),
    path('project/', ProjectView.as_view(), name='projects'),
    path('author/', AuthorView.as_view(), name='authors'),
    path('about', AboutView.as_view(), name='abouts'),
    path('comments/', CommentView.as_view(), name='comments'),
    path('contact', ContactView.as_view(), name='contact'),
    path('info/', ContactInfoView.as_view(), name='contact-info')
]
