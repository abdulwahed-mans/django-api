# Desc: Admin configuration for vpp app


from django.contrib import admin

# Register your models here.
import vpp.models as models

admin.site.register(models.Member)
admin.site.register(models.Device)
admin.site.register(models.EnergyData)

