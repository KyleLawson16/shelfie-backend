# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ShelfieTeam.models import Team

class TeamModelAdmin(admin.ModelAdmin):
	list_display = ["name", "random_team_id", "location", "point_of_contact"]
	list_display_links = ["name"]

	search_fields = ["name", "location"]
	class Meta:
		model = Team

admin.site.register(Team, TeamModelAdmin)
