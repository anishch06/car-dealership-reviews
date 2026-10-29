from django.core.management.base import BaseCommand
from serverapp.models import Dealer, Review

class Command(BaseCommand):
    help = "Create fictional sample dealers and reviews for local demo"

    def handle(self, *args, **options):
        samples = [
            ("Prairie Auto Group", "Topeka", "Kansas", "100 Demo Road", "555-0101"),
            ("Speedway Motors", "Wichita", "Kansas", "200 Sample Street", "555-0102"),
            ("AutoHub", "Columbia", "Missouri", "300 Example Lane", "555-0103"),
        ]
        for name, city, state, address, phone in samples:
            dealer, created = Dealer.objects.get_or_create(full_name=name, defaults={"city": city, "state": state, "address": address, "phone": phone})
            if created:
                Review.objects.create(dealer=dealer, name="Demo User", review="Fantastic services", purchase=True)
        self.stdout.write(self.style.SUCCESS("Demo records created. Fictional data only."))
