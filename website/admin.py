from django.contrib import admin
from .models import Message
from .models import Article
from .models import Image
from .models import Paragraph

class ParagraphInLine(admin.StackedInline):
    model = Paragraph
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'is_published')
    inlines = [ParagraphInLine]

class ImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'image')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subject', 'publication_date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Message, MessageAdmin)
