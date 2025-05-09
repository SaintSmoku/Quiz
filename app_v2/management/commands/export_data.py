from django.core.management.base import BaseCommand
from django.shortcuts import redirect
from app_v2.models import Team, User, Score  # Import your models
import os

class Command(BaseCommand):
    help = 'Exports all team, user, and score data to a text file'

    def handle(self, *args, **kwargs):
        # Path to the output file
        output_file = 'output_data.txt'

        # Open the file in write mode
        with open(output_file, 'w') as f:
            f.write("Teams, Users, and Scores Data\n")
            f.write("="*50 + "\n")

            # Export Teams
            f.write("\nTeams:\n")
            teams = Team.objects.all()
            for team in teams:
                f.write(f"Team Name: {team.temaname}\n")
                # Export Users in each team
                users = User.objects.filter(team=team)
                for user in users:
                    f.write(f"  User: {user.username}\n")
                # Export Score for the team
                score = Score.objects.filter(team=team).last()  # Get the most recent score
                if score:
                    f.write(f"  Score: {score.score}\n")
                else:
                    f.write("  Score: No score recorded\n")
                f.write("-" * 50 + "\n")

        self.stdout.write(self.style.SUCCESS(f'Successfully exported data to {output_file}'))
