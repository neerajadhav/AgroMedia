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

    def get_friends(self):
        return self.friends.all()

    def get_friends_count(self):
        return self.friends.count()
    
    def get_posts_no(self):
        return self.posts.all().count()
    
    def get_all_authors_posts(self):
        return self.posts.all()

    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            total_liked += 1
        return total_liked

    def get_likes_received_no(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.liked.all().count()
        return total_liked

    def __str__(self):
        return f"{self.user.username}"

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


STATUS_CHOICES = (
    ('send', 'Send'),
    ('accepted', 'Accepted'),
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return f'{self.sender}-{self.receiver}-{self.status}'