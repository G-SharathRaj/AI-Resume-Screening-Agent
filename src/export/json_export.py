import json


def export_to_json(results, filename="output/ranking.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)