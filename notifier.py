# A crude script to check for dark.fail link changes
import argparse
import os
import sys
import time
from logging import WARNING

from loguru import logger

from scraper import DarkFailScraper


def notify(title: str, text: str):
    """
    Send a native macOS notification
    :param title: notification title
    :param text: notification text
    """
    os.system(
        """osascript -e 'display notification "{}" with title "{}"'""".format(
            text, title
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a dark.fail site notifier")
    parser.add_argument(
        "site", help="Site to target (e.g. empire)", action="store", type=str
    )
    parser.add_argument(
        "-i",
        help="Scraping interval in seconds (default: 5 seconds)",
        default=5,
        action="store",
        type=int,
        dest="interval",
    )
    args = parser.parse_args()
    scraper = DarkFailScraper(args.site)
    logger.configure(
        **{"handlers": [{"sink": sys.stdout, "format": "[{time}] {message}"}]}
    )
    logger.info(
        f"Initial state for site {args.site}: {'online' if scraper.is_online else 'offline, last online ' + scraper.last_online} at {scraper.onion_link}"
    )
    while 1:
        try:
            if scraper.fetch() is True:
                notification = f"Change detected for site {args.site}: {'online' if scraper.is_online else 'offline, last online ' + scraper.last_online} at {scraper.onion_link}"
                logger.debug(notification)
                notify("dark.fail", notification)
        except Exception as e:
            logger.catch(exception=e, level=WARNING)
        time.sleep(args.interval)
