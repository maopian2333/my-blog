from django.db import models
from django.utils import timezone


class Post(models.Model):
    # models.CharField - 这是你如何用为数有限的字符来定义一个文本
    # models.TextField - 这是没有长度限制的长文本
    # models.DateTimeField - 这是日期和时间
    # models.ForeignKey - 这是指向另一个模型的连接
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
