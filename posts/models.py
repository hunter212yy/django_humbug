from django.utils.text import slugify
from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    post_slug = models.SlugField(editable=False)
    
    def __str__(self):
        return self.post_title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.post_slug = slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return ('post', (), {
            'post_slug': self.post_slug,
            'id': self.post_id,
        })


class Tag(models.Model):
    tag_text = models.CharField(max_length=50)
    tag_slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.tag_slug = slugify(self.tag_text)
        super(Tag, self).save(*args, **kwargs)