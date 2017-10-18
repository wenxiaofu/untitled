from django.conf.urls import url
from mysitenew import views
from mysitenew import calview

app_name = 'mysitenew'
urlpatterns = [
    # ex: /polls/
    url(r'^add/$',calview.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', calview.add2, name='add2'),
    url(r'^$', views.index, name='index'),

    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
