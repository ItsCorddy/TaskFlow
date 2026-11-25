
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'priority',
        'due_date',
        'completed',
        'created_at',
    )

    list_filter = (
        'priority',
        'completed',
        'due_date',
    )

    search_fields = (
        'title',
        'description',
        'user__username',
    )


admin.site.site_header = "TaskFlow Administration"
admin.site.site_title = "TaskFlow Admin"
admin.site.index_title = "TaskFlow Management Portal"
