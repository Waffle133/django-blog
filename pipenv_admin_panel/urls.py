from django.urls import path, register_converter
# from django.contrib import admin
from . import views as local_views
from posts import views as posts_views
from . import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world),
    path('server-hour/', local_views.server_hour),
    path('test-request/', local_views.test_request),
    path('test-path-conveters/<str:name>/<int:age>/<yyyy:year>', local_views.test_path_converter),
    path('posts-old', posts_views.list_posts_old),
    path('posts', posts_views.list_posts),

]
