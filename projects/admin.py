from django.contrib import admin

from projects.models.project import Project
from projects.models.task import Task
from projects.models.team_member import TeamMember
from projects.models.teamassignment import TeamAssignment

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_member', 'project', 'role', 'title', 'team', 'added_at', 'updated_at')
    search_fields = ('team_member__username', 'team_member__email', 'project__title', 'role', 'team')
    list_filter = ('role', 'team', 'project')

@admin.register(TeamAssignment)
class TeamAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'team_member', 'task', 'joined_at')
    search_fields = (
        'owner__title',
        'team_member__team_member__username',
        'task__title',
        'task__description',
    )
    list_filter = ('owner', 'task', 'joined_at')
