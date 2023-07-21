from django.contrib import admin
from .models import Stogit, StogitGame, StogitPlayer,StogitStatus,StogitRound,StogitStats
# Register your models here.
admin.site.register(StogitGame)
admin.site.register(StogitPlayer)
admin.site.register(StogitStatus)
admin.site.register(StogitRound)
admin.site.register(StogitStats)
