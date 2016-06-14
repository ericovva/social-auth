# ~*~ coding: utf-8 ~*~

# импортируем класс модели
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# и админки
from django.contrib import admin
# from django.contrib.auth.models import User, UserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
'''
    Blog posts
    '''
# class MyUser(User):
#     img = models.CharField(max_length=100,default="http://robohash.org/sitsequiquia.png?size=120x120")
#     objects = UserManager()

import pprint
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        error = 0
        try:
            MyUser.objects.get(email=email)
            print 'KKK\n'
            error = 1
        except Exception as e:
            print e
        if not email:
            raise ValueError('Users must have an email address')
        if error:
            raise ValueError('Пользователь был создан раннее')
            return
        print 'SADSADS\n'
        user = self.model(
            email=self.normalize_email(email),username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    #id = models.AutoField(primary_key=True,default = False,)
    username = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        default=False,
    )
    img = models.ImageField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# class MySocialUserManager(BaseUserManager):
#     def create_user(self, social_and_uid, username, token, email = None):
#         error = 0
#         try:
#             MySocialUser.objects.get(social_and_uid=social_and_uid)
#             print 'User exists\n'
#             error = 1
#         except Exception as e:
#             print e
#         if not social_and_uid:
#             raise ValueError('Users must have an social_and_uid field')
#         if error:
#             raise ValueError('Пользователь был создан раннее')
#             return
#         print 'Creating social user...\n'
#         user = self.model(
#             social_and_uid = social_and_uid,
#             username=username,
#             token = token,
#             email=self.normalize_email(email),
#         )
#         user.save(using=self._db)
#         return user

# class MySocialUser(AbstractBaseUser):
#     social_and_uid = models.CharField(max_length = 100,unique=True,default=False,verbose_name='social_and_uid   ')
#     username = models.CharField(max_length=100)
#     token = models.CharField(max_length=100)
#     email = models.EmailField(verbose_name='email address',max_length=255,default=False,)
#     img = models.ImageField(null=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     objects = MySocialUserManager()
#     USERNAME_FIELD = 'social_and_uid'
#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.social_and_uid

#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.social_and_uid

#     def __str__(self):              # __unicode__ on Python 2
#         return self.social_and_uid

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin


class Team(models.Model):
    # название поста
    title = models.CharField(max_length=100)
    # содержимое поста
    text = models.TextField()
    img = models.ImageField(upload_to='team/',null=True)
    # функция необходима для того, чтобы при выводе объекта Post
    # как строки выводился вместо этого его title
    def __unicode__(self):
        return self.title

class Game(models.Model):
    text = models.TextField()
    # название поста
    title = models.CharField(max_length=100)
    # содержимое поста
    description = models.TextField(default='Play and enjoy')
    img = models.ImageField(upload_to='games/',null=True)
    date = models.DateTimeField(auto_now=True,null=True)
    download_link = models.CharField(max_length=300,null=True)
    play_link = models.CharField(max_length=300,null=True)
    show_times = models.IntegerField(default=0)
    # функция необходима для того, чтобы при выводе объекта Post
    # как строки выводился вместо этого его title
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=10000)
    game = models.ForeignKey(Game,null=True)
    user = models.ForeignKey(MyUser,null=True)
    date = models.DateTimeField(auto_now=True,null=True)
    def __unicode__(self):
        return self.text


class ProfilePhoto(models.Model):
    img_src = models.TextField(max_length=10000)
    user = models.ForeignKey(MyUser,null=True) 

class Screenshot(models.Model):
    img = models.ImageField(upload_to='screenshots/',null=True)
    game = models.ForeignKey(Game)

class Rating(models.Model): 
    #game = models.ForeignKey(Game)
    user = models.ForeignKey(MyUser,null=True)
    content_type = models.ForeignKey(ContentType,null=True)
    object_id = models.PositiveIntegerField(null = True)
    content_object = GenericForeignKey('content_type', 'object_id')
    mark = models.FloatField(default=0)

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
    list_display = ('email',)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('game',)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('game',)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('mark','content_type','object_id',)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title',)
class CommentBlogPostAdmin(admin.ModelAdmin):
    list_display = ('post',)
class ProfilePhotoAdmin(admin.ModelAdmin):
    list_display = ('user',)
# связываем эту модель с моделью PostAdmin
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Screenshot,ScreenshotAdmin)
admin.site.register(Rating,RatingAdmin)
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(CommentBlogPost,CommentBlogPostAdmin)
admin.site.register(ProfilePhoto,ProfilePhotoAdmin)