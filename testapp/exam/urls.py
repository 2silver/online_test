from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('exam.views',
    url(r'^$', 'index'),
    url(r'^login/$', 'user_login'),
    url(r'^manage/$', 'prof_manage'),
    url(r'^manage/addquestion/$', 'add_question'),
    url(r'^manage/addquiz/$', 'add_quiz'),
    url(r'^manage/gradeuser/$', 'show_all_users'),
    url(r'^register/$', 'user_register'),
    url(r'^start/$', 'start'),
    url(r'^quit/$', 'quit'),
    url(r'^complete/$', 'complete'),
    url(r'^manage/monitor/$', 'monitor'),
    url(r'^monitor/(?P<quiz_id>\d+)/$', 'monitor'),    
    url(r'^user_data/(?P<username>[a-zA-Z0-9_.]+)/$', 'user_data'),
    url(r'^grade_user/(?P<username>[a-zA-Z0-9_.]+)/$', 'grade_user'),
    url(r'^(?P<q_id>\d+)/$', 'question'),
    url(r'^(?P<q_id>\d+)/check/$', 'check'),
)
