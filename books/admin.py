from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',            {'fields': ['a_title']}),
        ('Main information', {'fields': ['a_author', 'a_editor', 'a_type'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['a_pub_date'], 'classes': ['collapse']}),
        ('Other information', {'fields': ['a_reading_time', 'a_text'], 'classes': ['collapse']}),
    ]
    list_display = ('a_text', 'a_pub_date', 'was_published_recently')
    list_filter = ['a_pub_date']
    search_fields = ['question_text']

admin.site.register(Article, ArticleAdmin)