from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create a superuser"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            dest="username",
            default=None,
            help="Specifies the username for the superuser.",
        )
        parser.add_argument(
            "--email",
            dest="email",
            default=None,
            help="Specifies the email for the superuser.",
        )
        parser.add_argument(
            "--password",
            dest="password",
            default=None,
            help="Specifies the password for the superuser.",
        )

    def handle(self, *args, **options):
        password = options.get("password")
        username = options.get("username")
        email = options.get("email")

        if password and not username:
            raise CommandError("--username is required")

        if User.objects.filter(email=email, username=username).exists():
            self.stdout.write(self.style.WARNING("User already exists"))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
