import pytest

from marketing_blocks.models import MarketingBlock

pytestmark = pytest.mark.django_db(transaction=True)


class TestMarketingBlockManagers(object):
    def test_get_active_block_for_position(self, active_header_block):
        """Return the last active block for a specific position"""
        # WHEN
        header = MarketingBlock.objects.get_active_block_for_position_and_label(
            "header"
        )

        # THEN
        assert header.title == "Active Header"
        assert header.active
        assert header.position == "header"

    def test_get_block_contents_by_position(
        self, active_header_block, active_footer_block
    ):
        """Returns all the active block contents as a dictionary."""
        # WHEN
        dict_blocks = MarketingBlock.objects.get_block_contents_by_position_for_label(
            backend="mailchimp", label=""
        )

        # THEN
        assert type(dict_blocks) == dict
        assert dict_blocks["header"] == u"I'm an active header"
        assert dict_blocks["footer"] == u"I'm an active footer"

    def test_get_block_contents_by_position_fail_silently(self, active_header_block):
        """Returns empty string if given backend does not exist yet."""

        # GIVEN
        assert not hasattr(active_header_block, "content_stromboli")

        # WHEN
        dict_blocks = MarketingBlock.objects.get_block_contents_by_position_for_label(
            backend="stromboli", label=""
        )

        # THEN
        assert dict_blocks["header"] == ""
