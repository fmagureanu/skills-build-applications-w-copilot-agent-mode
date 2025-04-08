from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), username='john_doe', email='john_doe@example.com', password='password123'),
            User(_id=ObjectId(), username='jane_smith', email='jane_smith@example.com', password='password123'),
            User(_id=ObjectId(), username='alice_wonder', email='alice_wonder@example.com', password='password123'),
        ]
        # Debug: Print users being created
        print("Creating users:", users)
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Team Alpha')
        team2 = Team(_id=ObjectId(), name='Team Beta')
        # Debug: Print teams being created
        print("Creating teams:", team1, team2)
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Running', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Cycling', duration=timedelta(minutes=45)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Swimming', duration=timedelta(minutes=60)),
        ]
        # Debug: Print activities being created
        print("Creating activities:", activities)
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=80),
        ]
        # Debug: Print leaderboard entries being created
        print("Creating leaderboard entries:", leaderboard_entries)
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Morning Run', description='A 5km run to start the day'),
            Workout(_id=ObjectId(), name='Cycling Session', description='An intense cycling workout'),
            Workout(_id=ObjectId(), name='Swimming Laps', description='Swimming laps in the pool'),
        ]
        # Debug: Print workouts being created
        print("Creating workouts:", workouts)
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))