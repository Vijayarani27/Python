from django.contrib import admin

from .models import Developer,Skill

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class DeveloperAdmin(admin.ModelAdmin):
    #fields = ['name', 'country','experience']
    list_display = ('name', 'country', 'experience')
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Country', {'fields': ['country']}),
        ('Experience', {'fields': ['experience'],'classes': ['collapse']}),
    ]
    inlines = [SkillInline]

admin.site.register(Developer, DeveloperAdmin)
#admin.site.register(Skill)