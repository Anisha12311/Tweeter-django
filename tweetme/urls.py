
from django.contrib import admin
from django.urls import path,include
from tweet.views import (
    home_view,
    tweet_list_view, 
    tweet_create_view,
    tweet_detail_view,
    tweet_delete_view,
    tweet_action_view)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('tweet',tweet_list_view),
    path('create-tweet',tweet_create_view),
    path('tweet/<int:tweet_id>',tweet_detail_view),
    # path('api/tweet/action',tweet_action_view),
    # path('api/tweet/<int:tweet_id>/delete',tweet_delete_view),
    path('api/tweet/',include('tweet.urls'))
]

#http://127.0.0.1:8000/tweet - Tweet List view
#http://127.0.0.1:8000/tweet/1 - Tweet Detail view
#http://127.0.0.1:8000/api/tweet/action/ - Tweet Action view
#http://127.0.0.1:8000/api/tweet/6/delete/ - Tweet Delete view
