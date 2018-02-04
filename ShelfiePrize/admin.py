from django.contrib import admin

# Register your models here.
from ShelfiePrize.models import Prize

class PrizeModelAdmin(admin.ModelAdmin):
	list_display = ["name", "description", "winner"]
	list_display_links = ["name"]

	search_fields = ["name", "description", "winner"]
	class Meta:
		model = Prize

admin.site.register(Prize, PrizeModelAdmin)
