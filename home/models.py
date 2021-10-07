from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify

class Profile(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    website = models.URLField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + ' ' + str(self.last_name))
            ex = Profile.objects.filter(slug = to_slug).exists()
            while ex:
                to_slug = slugify(str(self.first_name) + ' ' + str(self.last_name) + ' ' + get_random_code())
                ex = Profile.objects.filter(slug = to_slug).exists()
        else:
            to_slug = slugify(self.user)

        self.slug = to_slug
        super().save(*args, **kwargs)
