from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from functools import lru_cache

blog_posts = {
    "django": "Django is the best web-framework for python",
    "python": "Pyton`s the latest version is 3.12",
    "html": "HyperText Markup Language",
    "css": "Cascading Style Sheets",
    "flask": "Flask is a small and lightweight Python web framework",
    "sql": "SQL is language for database requests"
}

blog_posts_by_category = {
    "languages": {
        "python": "<h1>Python</h1><h2>Pyton`s the latest version is 3.12</h2>",
        "html": "<h1>HTML</h1><h2>HyperText Markup Language</h2>",
        "css": "<h1>CSS</h1><h2>Cascading Style Sheets</h2>",
        "sql": "<h1>SQL is language for database requests</h1>"
    },
    "frameworks": {
        "django": "<h1>Django</h1><h2>Django is the best web-framework for python</h2>",
        "flask": "<h1>Flask is a small and lightweight Python web framework</h1>"
    }
}

numbers_posts = list(blog_posts.keys())


def main_page(request) -> render:
    return render(request, 'blog/main_page.html')


def posts(request) -> render:
    data = {
        "posts": blog_posts.keys()
    }

    return render(request, "blog/posts_page.html", context=data)


def post_categories(request) -> render:
    data = {
        'categories': blog_posts_by_category.keys()
    }

    return render(request, "blog/category_page.html", context=data)


@lru_cache()
def get_post_content(request, post_title: str) -> render:
    data = {
        "post_title": post_title,
        "post_content": blog_posts[post_title]
    }

    return render(request, "blog/post_content_page.html", context=data)


def show_category_content(request, category: str) -> render:
    data = {
        "title_of_category": category,
        "posts": blog_posts_by_category[category]
    }

    return render(request, "blog/category_content_page.html", context=data)
