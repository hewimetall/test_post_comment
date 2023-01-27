from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 64, verbose_name='Заголовок')
    text = models.TextField(verbose_name = "Текст поста")
    created = models.DateField(verbose_name= "Дата создания", auto_now_add = True)
    count = models.PositiveIntegerField(default = 0,editable = False)

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name = "comments",
        related_query_name = "comment",
    )

    text = models.TextField(verbose_name = "Текст коментария")
    created = models.DateField(verbose_name= "Дата создания", auto_now_add = True)
