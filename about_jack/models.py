from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible



# Create your models here.

#About Jackson model: fields(summary_text)
@python_2_unicode_compatible
class Jackson(models.Model):
    summary_text = models.CharField(max_length=3000)
        
    #returns the summary_text as a string
    def __str__(self):
        return '%s' %  self.summary_text	    	

#BlogPost model: fields(pub_date, title, blog_text)
@python_2_unicode_compatible
class BlogPost(models.Model):
    pub_date = models.DateTimeField('date published')	
    title = models.CharField(max_length=150)
    blog_text = models.CharField(max_length=5000)	
	
    #returns true if the publish date is greater than the currentdate
    def was_pub_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 	    
    
    #returns title and blog_text in string form
    def __str__(self):
        return '%s %s' % (self.title, self.blog_text)
	
