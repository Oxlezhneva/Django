from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        
        tag_ids = set([form.cleaned_data['tag'].id for form in self.forms])
        is_main_ids = [str(form.cleaned_data['is_main']) for form in self.forms] 
        count = is_main_ids.count("True")        
        if len(tag_ids) != len(self.forms):                    
            raise ValidationError('Такой тег уже есть')
        if "True"  not in is_main_ids:            
            raise ValidationError('Укажите основной раздел')
        if count >1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()

class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 0
    ordering = ('-is_main','tag',)
    formset = ArticleTagInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'text','published_at','image',)
    inlines = [ArticleTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    

