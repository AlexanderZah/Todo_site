from django.contrib import admin
from .models import Todos


class TodosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(Todos, TodosAdmin)
