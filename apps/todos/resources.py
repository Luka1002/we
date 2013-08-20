from djangorestframework.resources import ModelResource
from django.core.urlresolvers import reverse
from apps.todos.models import Todo


class TodoResource(ModelResource):
    model = Todo
    # by default, django rest framework won't return the ID - backbone.js
    # needs it though, so don't exclude it
    exclude = None
    ordering = ('order',)
    # django rest framework will overwrite our 'url' attribute with its own
    # that points to the resource, so we need to provide an alternative.
    include = ('resource_url',)
    ignore_fields = ('created_at', 'id',)

    '''
    def url(self, instance):
        return instance.url
    '''

    def resource_url(self, instance):
        return reverse('todos_api_instance', kwargs={'id': instance.id})

    def validate_request(self, data, files=None):
        """
        Backbone.js will submit all fields in the model back to us, but
        some fields are set as uneditable in our Django model. So we need
        to remove those extra fields before performing validation.
        """
        for key in self.ignore_fields:
            if key in data:
                del data[key]

        return super(TodoResource, self).validate_request(data, files)
