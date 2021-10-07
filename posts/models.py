from django.db import models
from home.models import Profile
from django.core.validators import FileExtensionValidator

class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='images', validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])], blank=True)
    liked = models.ManyToManyField(Profile, related_name='liked', default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.content[:20]

    def num_likes(self):
        return self.liked.all().count()

    def num_comments(self):
        return self.comments_set.all().count()

    class Meta:
        ordering = ['-created']

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Dislike', 'Dislike'),
)

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self-user}-{self-post}-{self-value}"