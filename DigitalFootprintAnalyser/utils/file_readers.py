import csv

def read_screen_time(path):
    minutes = []
    with open(path, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [h.strip().lower() for h in reader.fieldnames]

        for row in reader:
            minutes.append(int(row["minutes"]))
    return minutes


def read_app_usage(path):
    data = []
    with open(path, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [h.strip().lower() for h in reader.fieldnames]

        for row in reader:
            data.append({
                "app": row["app"].strip(),
                "category": row["category"].strip(),
                "minutes": int(row["minutes"])
            })

    return data
