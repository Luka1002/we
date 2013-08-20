from django.conf.urls.defaults import patterns, url

from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from apps.todos.resources import TodoResource

my_model_list = ListOrCreateModelView.as_view(resource=TodoResource)
my_model_instance = InstanceModelView.as_view(resource=TodoResource)

urlpatterns = patterns('',
    url(r'^todos/$', my_model_list, name='todos_api_root'),
    url(r'^todos/(?P<id>[0-9]+)$', my_model_instance, name='todos_api_instance'),
)