from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

from blog.models.post import Post
from blog.models.nav import Nav
from blog.models.maintext import MainText

NUM_OF_POSTS = 5


def home(request, username=None):
    first_name = ''
    last_name = ''
    user = None
    main_text = MainText.objects.filter(text_type='Main Page')[0]
    if username:
        user = User.objects.get(username=username)
        first_name = user.first_name
        last_name = user.last_name
        post_list = Post.objects.filter(user=user)
    else:
        post_list = Post.objects.all()

    post_list = post_list.order_by('-pub_date')

    paginator = Paginator(post_list, NUM_OF_POSTS)  # Show NUM_OF_PAGES posts per page
    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'posts': posts,
                                              'first_name': first_name,
                                              'last_name': last_name,
                                              'main_text': main_text,
                                              'postuser': user,
                                              })


def nav(request, link):
    nav_item = Nav.objects.get(link=link);
    return render(request, 'blog/nav.html', {"nav": nav_item})
