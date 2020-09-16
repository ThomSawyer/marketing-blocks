from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class MarketingBlocksManager(models.Manager):
    def get_active_block_for_position_and_label(self, position, label=""):
        """Returns the active block for a specific position and label"""
        try:
            block = self.get(position=position, label=label, active=True)
        except ObjectDoesNotExist:
            block = None

        return block

    def get_block_contents_by_position_for_label(self, backend, label=""):
        """Returns all the active block contents by position, for given backend and label"""

        blocks = self.filter(active=True, label=label)

        data = {
            block.position: getattr(block, f"content_{backend}", "") for block in blocks
        }

        return data
