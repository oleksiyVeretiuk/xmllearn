from django.conf.urls import url
from .views import ThemeListView, ArticleListView, ThemeTestView, UserResultView, login_user


urlpatterns = [
    url(r'^themes/$', ThemeListView.as_view()),
    url(r'^themes/(?P<pk>\d+)/$', ArticleListView.as_view()),
    url(r'^themes/(?P<pk>\d+)/test$', ThemeTestView.as_view()),
    url(r'^results/$', UserResultView.as_view(), name='result_list'),
    url(r'^login/$', login_user, name='login_user')
]
