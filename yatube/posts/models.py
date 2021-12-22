from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    """Defines the Group table."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title or ''


class Post(models.Model):
    """Defines Post table with descrement order by dates."""

    text = models.TextField(
        'Текст поста',
        help_text='Введите текст поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Выберите группу'
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        error_messages={"unique": 'IMAGE NOT UPLOADED'})

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.text[:15] or ''


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
        verbose_name='комментарии',
        help_text='не троллить'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
        verbose_name='Автор',
        help_text='Имя или Ник'
    )
    text = models.TextField(
        help_text='Введите текст комментария'
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment {} by {}'.format(self.text or '', self.author or '')


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        blank=False,
        null=False,
        verbose_name='последователь',
        help_text='последователь'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        blank=False,
        null=False,
        verbose_name='Автор',
        help_text='Имя или Ник автора'
    )

    class Meta:
        constraints = (
            models.CheckConstraint(check=~models.Q(user=models.F('author')),
                                   name='user_user_constraint'),
            models.UniqueConstraint(fields=['user', 'author'],
                                    name='user_author_constraint'),
        )
