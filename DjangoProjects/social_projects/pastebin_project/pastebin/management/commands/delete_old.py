import datetime
from django.core.management.base import BaseCommand
from pastebin.models import Paste

class Command(BaseCommand):
    help = """
            deletes pastes not updated in last 24 hrs

            Use this subcommand in a cron job
            to clear older pastes
           """

    def handle(self, **options):
        now = datetime.datetime.now()
        twodays = now - datetime.timedelta(2)  #represents a full 24 hour cycle ([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
        old_pastes = Paste.objects.filter(updated_on__lte=twodays)
        old_pastes.delete()

    # We subclass either of the BaseCommand, LabelCommand or AppCommand from 
    # django.core.management.base. BaseCommand suits our need because we dont need to pass any 
    # arguments to this subcommand.  Handle will be called when the script runs.
    # We have used the lte lookup on updated_on field to get all posts older than a day. Then we 
    # delete them using delete method on the queryset.
    # You can test if the subcommand works by doing: python manage.py delete_old