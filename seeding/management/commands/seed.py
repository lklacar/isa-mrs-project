from django.core.management import BaseCommand

from seeding.config import SEEDS
import logging

FORMAT = "%(levelname)s - %(asctime)s - %(name)s - \t %(message)s"
logging.basicConfig(level=logging.NOTSET, format=FORMAT)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for seed in SEEDS:
            try:
                logger.debug("Attempting to seed %s" % seed.__name__)
                seed().seed()
                logger.debug("Successfully seeded: %s" % seed.__name__)
            except Exception as e:
                logger.error("Failed to seed: %s\n\t%s" % (seed.__name__, e))
