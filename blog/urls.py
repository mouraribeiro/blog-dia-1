from django.urls import path

from.views import PostList, PostDetail, novoPost


urlpatterns = [
    path('', PostList.as_view(), name='post'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('novo-post', novoPost, name='novo-post'),

]