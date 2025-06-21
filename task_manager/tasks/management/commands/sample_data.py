from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from tasks.models import Task, Category

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            email='demo@example.com',
            defaults={
                'username': 'demo',
                'first_name': 'Demo',
                'last_name': 'User'
            }
        )
        if created:
            user.set_password('demo123')
            user.save()

        categories = ['Work', 'Personal', 'Learning']
        for cat_name in categories:
            Category.objects.get_or_create(
                name=cat_name,
                created_by=user
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data')
        )