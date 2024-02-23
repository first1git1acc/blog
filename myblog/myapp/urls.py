from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('',views.post_list,name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name="post_detail"),
    path('<int:post_id>/comment/',views.post_comment, name='post_comment'),
    path('find/<slug:tag>',views.finded_posts_by_tag,name="finded_posts_by_tag"),
    path('a',views.posts_by_tag,name="posts_by_tag")
]