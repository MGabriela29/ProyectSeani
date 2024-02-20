from django.contrib import admin

from .models import Module, Question

class QuestionInline(admin.StackedInline):
    model = Question

@admin.register(Module)
class ModuleAdim(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_question']
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display= ['question_text','module','correct']
    ordering=['module']



# Register your models here.
# admin.site.register(Module, ModuleAdim)
# admin.site.register(Question,QuestionAdmin)

