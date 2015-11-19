# ~*~ coding: utf-8 ~*~

# импортируем класс модели
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# и админки
from django.contrib import admin
from django.contrib.auth.models import User, UserManager
'''
    Blog posts
    '''
class MyUser(User):
    login = models.CharField(max_length=100)
    img = models.ImageField(null=True)
    objects = UserManager()


class Team(models.Model):
    # название поста
    title = models.CharField(max_length=100)
    # содержимое поста
    text = models.TextField()
    img = models.ImageField(null=True)
    # функция необходима для того, чтобы при выводе объекта Post
    # как строки выводился вместо этого его title
    def __unicode__(self):
        return self.title;

class Game(models.Model):
    text = models.TextField()
    # название поста
    title = models.CharField(max_length=100)
    # содержимое поста
    description = models.TextField(default='Play and enjoy')
    img = models.ImageField(null=True)
    date = models.DateTimeField(auto_now=True,null=True)
    download_link = models.CharField(max_length=300,null=True)
    play_link = models.CharField(max_length=300,null=True)
    # функция необходима для того, чтобы при выводе объекта Post
    # как строки выводился вместо этого его title
    def __unicode__(self):
        return self.title;
class Comment(models.Model):
    text = models.TextField()
    game = models.ForeignKey(Game,null=True)
    user = models.ForeignKey(MyUser,null=True)
    date = models.DateTimeField(auto_now=True,null=True)

class Screenshot(models.Model):
    img = models.ImageField(null=True)
    game = models.ForeignKey(Game)

class Rating(models.Model): 
    #game = models.ForeignKey(Game)
    user = models.ForeignKey(MyUser,null=True)
    content_type = models.ForeignKey(ContentType,null=True)
    object_id = models.PositiveIntegerField(null = True)
    content_object = GenericForeignKey('content_type', 'object_id')
    mark = models.IntegerField(default=0)

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True,null=True)
    user = models.ForeignKey(MyUser,null=True)

class CommentBlogPost(models.Model):
    text = models.TextField()
    post = models.ForeignKey(BlogPost,null=True)
    user = models.ForeignKey(MyUser,null=True)
    date = models.DateTimeField(auto_now=True,null=True)



'''
Класс для админки, тут будут дополнительные атрибуты необходимые для админки
'''
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('login',)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('game',)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('game',)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('mark',)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title',)
class CommentBlogPostAdmin(admin.ModelAdmin):
    list_display = ('post',)
# связываем эту модель с моделью PostAdmin
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Screenshot,ScreenshotAdmin)
admin.site.register(Rating,RatingAdmin)
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(CommentBlogPost,CommentBlogPostAdmin)