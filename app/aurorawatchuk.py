#!/usr/bin/env python3

import requests
from lxml import etree

AWUK_URL = "https://aurorawatch-api.lancs.ac.uk/0.2.5/status/all-site-status.xml"

def get_status_ids():
    # Retrieves the all-site-status.xml file from AWUK and returns all status_id values.
    # Fetch xml file.
    response = requests.get(
        AWUK_URL,
        # AWUK request that referer is used to identify clients accessing their API.
        headers={
            "referer": "https://github.com/cowgoesmoo69/aurorawatch-uk-alerts"
        },
        timeout=10,
    )
    response.raise_for_status()
    # Process xml for status_id values.
    root = etree.fromstring(response.content)
    sites = root.xpath("//site_status")
    status_ids = []
    for site in sites:
        status_ids.append(
            {
                "site_id": site.get("site_id"),
                "site_url": site.get("site_url"),
                "status_id": site.get("status_id"),
            }
        )
    return status_ids
    
    
def process_status_ids(
    status_ids,
    ):
    # Determine the lowest-ranked status ID across all sites and return it as an integer between 0 and 3.
    RANK_ORDER = ["green", "yellow", "amber", "red"]
    statuses = {s["status_id"] for s in status_ids}
    for i, rank in enumerate(RANK_ORDER):
        if rank in statuses:
            return i
    # If something goes wrong, raise.
    raise RuntimeError(
        "Data returned from AuroraWatch UK API contained invalid status values."
        )


def get_status():
    s_ids = get_status_ids()
    return process_status_ids(s_ids)


def main():
    print("This script is not intended to be run as-is.")
    print("Put this file in the same directory as your script and import: from aurorawatchuk.py import get_status.")
    

if __name__ == "__main__":
    main()