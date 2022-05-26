from django.db import models
from django.contrib.auth.models import User #extending the django user model
from django.utils import timezone

#User Profile information extending the vanilla Django user model.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    bio = models.TextField()
    #majlis = models.ManyToManyField('accounts.Majlis', related_name='majlis')

    def __str__(self):
        return str(self.user)

#Tag / Category Model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


#Course Model
class Majlis(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    people = models.ManyToManyField('Profile', related_name="people")
    #author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
            return self.title

    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)


