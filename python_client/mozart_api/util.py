"""Various helper functions useful for interacting with Mozart devices."""

import re

from mozart_api.models import Art, PlaybackContentMetadata


def check_valid_jid(jid: str) -> bool:
    """Check if a JID is valid."""
    return bool(re.fullmatch(r"\d{4}\.\d{7}\.\d{8}@products\.bang-olufsen\.com", jid))


def check_valid_serial_number(serial_number: str) -> bool:
    """Check if a serial_number is valid."""
    return bool(re.fullmatch(r"\d{8}", serial_number))


def split_jid(jid: str) -> tuple[str, str, str]:
    """Split JID into item, type and serial number."""
    split_jid = jid.split(".", maxsplit=2)
    return split_jid[0], split_jid[1], split_jid[2].split("@", maxsplit=1)[0]


def get_highest_resolution_artwork(metadata: PlaybackContentMetadata) -> Art:
    """Get the highest resolution Art from provided PlaybackContentMetadata."""
    # Return an empty Art if no artwork is in metadata to ensure no stale artwork
    if not metadata.art:
        return Art()

    # Dict for sorting images that have size defined by a string
    art_size = {"small": 1, "medium": 2, "large": 3}

    # Contains tuples, containing the size of the image and the original index
    images = []

    # Images either have a key for specifying resolution or a "size" for the image.
    for i, image in enumerate(metadata.art):
        # Skip any invalid artwork
        if not image.url:
            continue
        # Netradio.
        if image.key:
            images.append((int(image.key.split("x")[0]), i))
        # Everything else.
        elif image.size:
            images.append((art_size[image.size], i))

    # Check if only invalid images were provided
    if not images:
        return Art()

    # Choose the largest image.
    return metadata.art[max(images)[1]]
