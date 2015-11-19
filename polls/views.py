# ~*~ coding: utf-8 ~*~

# функция генерирующая 404 страницу
from django.http import Http404

# функция отрисовки страницы, принимающая путь до шаблона и данные помещенные в шаблон
from django.shortcuts import render_to_response
from django.contrib.contenttypes.models import ContentType
# наша модель
from polls.models import Game
from polls.models import Team
from polls.models import Comment
from polls.models import BlogPost
from polls.models import CommentBlogPost
from polls.models import Screenshot
from polls.models import Rating

def main_page (request):

    return render_to_response('index.html')
def auth (request):
    
    return render_to_response('login.html')
def blog (request):
    blog_posts = BlogPost.objects.all()
    return render_to_response('blog.html',{"blog_posts": blog_posts})
def get_blog_post(request, blog_post_id):
    try:
        # выбираем конкретный пост, pk - primary key
        blog_post = BlogPost.objects.get(pk=blog_post_id)
        blog_comments = CommentBlogPost.objects.filter(post=blog_post_id)
    except BlogPost.DoesNotExist:
        # если такого поста нет, то генерируем 404
        raise Http404
    # отрисовываем
    return render_to_response('blog_post.html', {"title":  blog_post.title, "img": blog_post.img, "user": blog_post.user ,"id": blog_post.id, "text": blog_post.text,"comments": blog_comments})


def profile (request):
    
    return render_to_response('profile.html')
def we (request):
    
    # Получаем список постов
    teams = Team.objects.all()
    # отрисовываем
    return render_to_response('our_team.html', {"teams":  teams})


def get_post (request, post_id):
    try:
        # выбираем конкретный пост, pk - primary key
        post = Game.objects.get(pk=post_id)
        comments = Comment.objects.filter(game=post_id)
        images = Screenshot.objects.filter(game=post_id)
        post_type = ContentType.objects.get_for_model(post)
        rating = Rating.objects.filter(content_type=post_type.id,object_id=post_id)
        print(len(rating))
        sum = 0.0
        votes = len(rating)
        if votes != 0:
            for rate in rating:
                sum = sum + rate.mark
            sum = sum / len(rating)
            
        count = len(images)
        list = []
        for i in range(0,count):
            list.append(i)
    except Game.DoesNotExist:
        # если такого поста нет, то генерируем 404
        raise Http404
    except Comment.DoesNotExist:
        return render_to_response('single.html', {"title":  post.title, "description": post.description, "no_comments": 1 ,"id": post.id})
    # отрисовываем
    return render_to_response('single.html', {"title":  post.title, "description": post.description, "comments": comments ,"id": post.id,"images": images,"count": list, "rating": sum,"votes": votes})


def posts_page (request):
    # Получаем список постов
    games = Game.objects.all()
    i = 0
    ratings = []
    while i < len(games):
        game_type = ContentType.objects.get_for_model(games[i])
        rating = Rating.objects.filter(content_type=post_type.id,object_id=games[i].id)
        print("rating")
        print(rating)
        j = 0
        sum = 0.0
        if (len(rating) != 0):
            while j < len(rating):
                sum = sum + rating[j].mark
                j = j + 1
            ratings.append(sum / len(rating))
        else: 
            ratings.append(sum)
        print("ratings[i]")
        print(ratings[i])
        i = i + 1
        print("______________")
    # отрисовываем
    return render_to_response('list.html', {"games":  posts})









