from django.core.management.base import BaseCommand
from polls.models import Team,MyUser,Comment,Game,BlogPost,CommentBlogPost, Rating, Screenshot
import random
import math
class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'
    
    def _create_tags(self):
        count = 1000
        i = 0
        while i < count:
            src = 'eugene.jpg'
            if i % 2 == 0:
                src = 'Art.jpg'
            tlisp = Team(title='Mike' + str(i) ,text='seo',img = src)
            tlisp.save()
            i = i + 1
        #tjava = Tag(name='Java')
        #tjava.save()
        
        i = 0
        while i < count:
            login_ = 'Black' + str(i)
            password_ = 'qwerty'
            username_ = 'Wolf' + str(i)
            img_ = str ( i % 7 + 1) + ".jpg"
            new_user = MyUser(password = password_,username = username_,img = img_)
            new_user.save()
            i = i + 1

        i = 0
        while i < count:
            title_ = 'Game number ' + str(i)
            text_ = 'Game text number ' + str(i)
            img_ = str(i % 5 + 1) + '_' + '1.jpg'
            download_link_ = 'http://mail.ru'
            play_link_ = 'http://yandex.ru'
            description_ = 'Game description number ' + str(i)
            new_game = Game(title = title_, text = text_, img = img_, download_link = download_link_, play_link = play_link_, description = description_)
            new_game.save()
            i = i + 1
        
        i = 0
        _id = 1
        while i < count:
            i = i + 1
            g = Game.objects.get(id=i)
            u = MyUser.objects.get(id=i)
            j = 0
            while j < 10:
                print("i " + str(i))
                print("  j" + str(j))
                text_ = "Comment number " + str(j) + "game" + str(i)
                new_comment = Comment(text = text_)
                new_comment.save()
                print("ID " + str(_id))
                e = Comment.objects.get(id=_id)
                g.comment_set.add(e)
                u.comment_set.add(e)
                _id = _id + 1
                j = j + 1
                    
        i = 0
        my_str = "abcdefghigklmnopqrstuvwxyz          "
        while i < count:
            title_ = "Post " + str(i)
            img_ = str ( i % 7 + 1) + ".jpg"
            text_ = ""
            j = 0
            while (j < 1000):
                text_ = my_str[math.trunc(random.random() * 36)] + text_
                j = j + 1
            new_post = BlogPost(title = title_, img = img_, text = text_)
            new_post.save()
            u = MyUser.objects.get(id=i + 1)
            e = BlogPost.objects.get(id=i + 1)
            u.blogpost_set.add(e)
            i = i + 1

        i = 0
        _id = 1
        while i < count:
            i = i + 1
            g = BlogPost.objects.get(id=i)
            u = MyUser.objects.get(id=i)
            j = 0
            while j < 10:
                print("i " + str(i))
                print("  j" + str(j))
                text_ = "Comment number " + str(j) + "post" + str(i)
                new_comment_blog = CommentBlogPost(text = text_)
                new_comment_blog.save()
                print("ID " + str(_id))
                e = CommentBlogPost.objects.get(id=_id)
                g.commentblogpost_set.add(e)
                u.commentblogpost_set.add(e)
                _id = _id + 1
                j = j + 1


        i = 0
        _id = 1
        while i < count:
            i = i + 1
            p = BlogPost.objects.get(id=i)
            g = Game.objects.get(id=i)
            u = MyUser.objects.get(id=i)
            j = 0
            while j < 10:
                if ( i % 2 == 0):
                    content_object_ = g
                else:
                    content_object_ = p
                mark_ = math.trunc(random.random() * 5)
                new_rating = Rating(mark = mark_, content_object = content_object_)
                new_rating.save()
                e = Rating.objects.get(id=_id)
                u.rating_set.add(e)
                _id = _id + 1
                j = j + 1

        i = 0
        _id = 1
        while i < count:
            i = i + 1
            g = Game.objects.get(id=i)
            j = 1
            while j < 11:
                game_ = g
                img_ = str(j) + ".jpg"
                new_img= Screenshot(game = game_, img = img_)
                new_img.save()
                e = Screenshot.objects.get(id=_id)
                g.screenshot_set.add(e)
                _id = _id + 1
                j = j + 1




    def handle(self, *args, **options):
        self._create_tags()




