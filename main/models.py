from django.db import models


# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class About(TimeStamp):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    name = models.CharField(max_length=212)
    data_birthday = models.CharField(max_length=212)
    address = models.CharField(max_length=212)
    zib_code = models.CharField(max_length=212)
    email = models.EmailField()
    phone = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Resume(TimeStamp):
    title = models.CharField(max_length=212)
    description = models.TextField()
    year = models.CharField(max_length=212)
    title2 = models.CharField(max_length=212)
    description2 = models.TextField()

    def __str__(self):
        return self.title


class Service(TimeStamp):
    title = models.CharField(max_length=212)
    body = models.TextField()

    def __str__(self):
        return self.title


class Skills(TimeStamp):
    title = models.CharField(max_length=212)
    description = models.TextField()
    skills_percentage = models.IntegerField()

    def __str__(self):
        return self.title


class Author(TimeStamp):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='authors')
    description = models.TextField()

    def __str__(self):
        return self.name


class Project(TimeStamp):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='project/')

    def __str__(self):
        return self.title


class Post(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='post/  ')
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(TimeStamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    image = models.ImageField(upload_to='comment_author/')


class Contact(TimeStamp):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    phone = models.CharField(max_length=212)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactInfo(TimeStamp):
    address = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.phone
