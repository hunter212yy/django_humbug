from django.utils.text import slugify
from django.db import models
from django.core.urlresolvers import reverse
from fluent_comments.moderation import moderate_model


# Create your models here.

class Tag(models.Model):
    tag_text = models.CharField(max_length=50)
    tag_slug = models.SlugField(unique=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.tag_slug = slugify(self.tag_text)
        super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.tag_text


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    post_slug = models.SlugField(editable=False, max_length=200)
    image = models.ImageField(default = "<img src='http://shere.buruma.net/wp-content/uploads/2014/09/django.png'>", upload_to='documents/%Y/%m/%d', blank=True, null=True)
    
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.post_title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.post_slug = slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'post_slug': self.post_slug,
        })
    
    def get_text_batch(self):
        return self.post_text[:250] + "..."


moderate_model(Post,
    publication_date_field='publication_date',
    enable_comments_field='enable_comments',
)

