import requests


def search_ssb_tables():
    url = "https://data.ssb.no/api/pxwebapi/v2/tables"
    params = {
        "lang": "en",
        "query": "employment",
        "pagesize": 5
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    print("[INFO] SSB table search successful")
    print(data)


if __name__ == "__main__":
    search_ssb_tables()