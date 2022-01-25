from django.contrib import admin
from .models import  Lottery

class LotteryAdmin(admin.ModelAdmin):
    list_display = ('id','timestamp', 
                    'numero1', 
                    'numero2', 
                    'numero3', 
                    'numero4', 
                    'numero5', 
                    'numero6', 
                    'numero7', 
                    'numero8', 
                    'numero9', 
                    'numero10', 
                    'numero11', 
                    'numero12', 
                    'numero13',
                   )

# Register your models here.

admin.site.register(Lottery, LotteryAdmin)
        