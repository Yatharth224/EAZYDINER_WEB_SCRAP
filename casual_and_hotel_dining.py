import requests
import csv
import os
import time

CITY = "indore"
CATEGORIES = ["casual-dining", "hotel-dining"]

OUTPUT_FOLDER = "final_restro"
OUTPUT_FILENAME = f"casual_hotel_dining_{CITY}.csv"
FULL_PATH = os.path.join(OUTPUT_FOLDER, OUTPUT_FILENAME)

BASE_URL = "https://www.eazydiner.com/_next/data/SnHMuiMhd83orLphAebIU/en/restaurants.json"

cookies = {
    "islive": "0"
}

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0",
    "x-nextjs-data": "1"
}

def extract_restaurants(json_data):
    try:
        items = json_data["pageProps"]["listingData"]["data"]["data"]
    except:
        return []

    rows = []

    for item in items:
        images = []

        for key in ["image", "gallery", "photos", "album_img", "photo_gallery"]:
            v = item.get(key)
            if isinstance(v, list):
                images.extend(v)
            elif isinstance(v, str):
                images.append(v)

        rows.append({
            "name": item.get("name", ""),
            "location": item.get("location", ""),
            "cost_for_two": item.get("cost_for_two", ""),
            "images": list(set(images))
        })

    return rows

all_rows = []

for category in CATEGORIES:
    page = 1
    while True:
        params = {
            "location": CITY,
            "categories[]": category,
            "page": page
        }

        r = requests.get(BASE_URL, params=params, headers=headers, cookies=cookies)

        if r.status_code != 200:
            break

        try:
            data = r.json()
        except:
            break

        rows = extract_restaurants(data)

        if not rows:
            break

        all_rows.extend(rows)
        page += 1
        time.sleep(1)

if not all_rows:
    print("No data found")
    exit()

max_images = max(len(r["images"]) for r in all_rows)

csv_headers = ["name", "location", "cost_for_two"] + [
    f"image{i+1}" for i in range(max_images)
]

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

with open(FULL_PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(csv_headers)

    for r in all_rows:
        row = [r["name"], r["location"], r["cost_for_two"]]
        row.extend(r["images"])
        row.extend([""] * (max_images - len(r["images"])))
        w.writerow(row)

print("Scraping completed")
print("Total restaurants:", len(all_rows))
print("File saved at:", FULL_PATH)
