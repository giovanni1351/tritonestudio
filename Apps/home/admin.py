from django.contrib import admin
from .models import Reports,GameImage,Game
# Register your models here.

admin.site.site_header = 'Tritonestudio Administration'
admin.site.site_title = 'Tritonestudio Administration'
admin.site.index_title = 'Tritonestudio Administration'

class ReportsAdmin(admin.ModelAdmin):

    list_display = ("email","name","mensagem",)
    search_fields = ("email","name","mensagem",)
    list_filter = ("email","name","mensagem",)


admin.site.register(Reports,ReportsAdmin)


class GameImageInline(admin.TabularInline):
    model = GameImage
    extra = 1


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'in_development', 'order')
    search_fields = ('title', 'description')
    list_filter = ('in_development', 'release_year')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GameImageInline]


@admin.register(GameImage)
class GameImageAdmin(admin.ModelAdmin):
    list_display = ('game', 'alt_text', 'is_main', 'order')
    list_filter = ('game', 'is_main')
    search_fields = ('game__title', 'alt_text')