from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Seeds 100 new data and cleans up the terminal when it needs to run'

    def handle(self, *args, **options):
        # clear database
        call_command('flush', '--no-input')

        self.stdout.write(self.style.SUCCESS(
            'cleared All Database Records!'))

        call_command('seed', 'api', number=100)
        self.stdout.write(self.style.SUCCESS(
            '\nsuccessfully added 100 new data!'))
