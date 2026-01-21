import logging
import requests
from typing import List
from altpkgdiff.models import Package

logger = logging.getLogger(__name__)

BASE_URL = "https://rdb.altlinux.org/api"


def fetch_branch_packages(branch: str) -> List[Package]:
    url = f"{BASE_URL}/export/branch_binary_packages/{branch}"
    logger.info("Fetching packages for branch %s", branch)

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()
    items = data.get("packages", [])

    packages: List[Package] = []

    for item in items:
        packages.append(
            Package(
                name=item["name"],
                version=item["version"],
                release=item["release"],
                arch=item["arch"],
            )
        )

    logger.info("Fetched %d packages for %s", len(packages), branch)
    return packages
