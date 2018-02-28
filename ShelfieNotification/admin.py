from django.contrib import admin

# Register your models here.
from ShelfieNotification.models import Notification

class NotificationModelAdmin(admin.ModelAdmin):
	list_display = ["actor", "recipient", "category", "message", "timestamp"]
	list_display_links = ["actor", "recipient", "category"]

	search_fields = ["actor", "recipient", "category"]
	class Meta:
		model = Notification

admin.site.register(Notification, NotificationModelAdmin)
