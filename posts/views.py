from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

posts = [
    {
        'title': '.My Dog',
        'user': 'Fernando',
        'timestamp': datetime.now().strftime('%d %m, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200'
    },
    {
        'title': 'Khe.',
        'user': 'Montes de Oca',
        'timestamp': datetime.now().strftime('%d %m, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'title': 'Nautural web.',
        'user': 'Alonso',
        'timestamp': datetime.now().strftime('%d %m, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },
]


def list_posts_old(requests):
    concat_posts = []
    for post in posts:
        concat_posts.append("""
        <p style='color:red'>{title}</p>
        <p>{user}</p>
        <p>{timestamp}</p>
        <figure>
        <img src={picture}/>
        </figure>
        """.format(**post))
    return HttpResponse('<br>'.join(concat_posts))


def list_posts(request):
    return render(request, 'posts/posts.html', {'posts': posts})
