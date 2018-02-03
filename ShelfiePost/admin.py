# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ShelfiePost.models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["user", "game", "challenge", "caption", "timestamp"]
	list_display_links = ["user", "game"]

	search_fields = ["user", "game", "challenge"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
