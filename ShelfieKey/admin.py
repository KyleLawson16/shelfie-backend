from django.contrib import admin

# Register your models here.
from ShelfieKey.models import AmazonS3

class AmazonS3ModelAdmin(admin.ModelAdmin):
	list_display = ["bucket", "region", "access_key", "secret_access_key"]
	list_display_links = ["bucket"]

	class Meta:
		model = AmazonS3

admin.site.register(AmazonS3, AmazonS3ModelAdmin)
