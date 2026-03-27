from django.db import models
from users.models.new_user import User
from projects.models.project import Project

# Create your models here.

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coordinator', 'Coordinator'),
        ('volunteer', 'Volunteer'),
    ]

    team_member = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
        
    role = models.CharField(max_length=20, choices= ROLE_CHOICES, default='volunteer'
                            )
    title = models.CharField(max_length=100, blank=True)
    team = models.CharField(max_length=50, null = True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['team_member', 'project', 'role']

    def __str__(self):
        return f"{self.team_member.username} ({self.role})"