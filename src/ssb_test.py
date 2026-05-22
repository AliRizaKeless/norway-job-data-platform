import requests


def fetch_ssb_data():
    url = "https://data.ssb.no/api/pxwebapi/v2/tables/08651/data"
    params = {
        "lang": "en",
        "outputFormat": "json-stat2"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    print("[INFO] SSB data fetch successful")
    print(type(data))
    print(data.keys())


if __name__ == "__main__":
    fetch_ssb_data()