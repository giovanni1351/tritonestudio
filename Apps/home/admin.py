from django.contrib import admin
from .models import Reports
# Register your models here.

admin.site.site_header = 'Tritonestudio Administration'
admin.site.site_title = 'Tritonestudio Administration'
admin.site.index_title = 'Tritonestudio Administration'

class ReportsAdmin(admin.ModelAdmin):

    list_display = ("email","name","mensagem",)
    search_fields = ("email","name","mensagem",)
    list_filter = ("email","name","mensagem",)


admin.site.register(Reports,ReportsAdmin)