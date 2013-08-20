from django.contrib import admin
from apps.todos.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','done','order','created_at',)


admin.site.register(Todo, TodoAdmin)
