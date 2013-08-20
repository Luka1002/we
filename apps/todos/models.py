from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Todo(models.Model):
    title      = models.CharField(max_length=1024)
    order      = models.IntegerField(default=0,verbose_name='Order')
    done       = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_show', args=[self.id])
