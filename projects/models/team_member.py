from django.db import models
from accounts.models import CustomUser
from projects.models.project import Project

# Create your models here.

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coordinator', 'Coordinator'),
        ('team lead', 'Team Lead'),
        ('member', 'Member'),
    ]

    team_member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
        
    role = models.CharField(max_length=20, choices= ROLE_CHOICES, default='member')
    title = models.CharField(max_length=100, blank=True)
    team = models.CharField(max_length=50, null = True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['team_member', 'project', 'role']

    def __str__(self):
        return f"{self.team_member.username} ({self.role})"