from django.db import models
#from ceemlez.users.models.new_user import User
from projects.models.team_member import TeamMember
from projects.models.task import Task
from projects.models.project import Project

# Create your models here.
class TeamAssignment(models.Model):
    owner = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='team_assignments'
        ) # The user who created the assignment
    
    # ForeignKey to User model
    ''' If the user is in team member, they can be assigned to a task. '''
    team_member = models.ForeignKey(
        TeamMember,
        on_delete= models.CASCADE,
        related_name='team_assignments'
    )

    
    # ForeignKey to Task model
    task = models.ForeignKey(
        Task,
        on_delete= models.CASCADE,
        related_name='team_assignments'
    )

    joined_at = models.DateTimeField(auto_now_add=True) # Timestamp when the volunteer joined the project

    # String representation of the TeamAssignment
    class Meta:
        unique_together = ('team_member', 'task')  # Ensure a user can be assigned to a task only once


    def __str__(self):
        return f"{self.team_member.username} assigned to {self.task.title}"