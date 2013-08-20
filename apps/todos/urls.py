from django.conf.urls import patterns, url


urlpatterns = patterns('apps.todos.views',
    url(r'^$', 'todo_list', name='todo_list'),

)