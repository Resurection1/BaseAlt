import json
import logging
from altpkgdiff.api import fetch_branch_packages
from altpkgdiff.compare import compare_branches


def main():
    logging.basicConfig(level=logging.INFO)

    sisyphus = fetch_branch_packages("sisyphus")
    p11 = fetch_branch_packages("p11")

    result = compare_branches(sisyphus, p11)
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    logging.info("Result written to result.json")


if __name__ == "__main__":
    main()
