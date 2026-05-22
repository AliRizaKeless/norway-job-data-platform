import requests
import pandas as pd


def fetch_ssb_data():
    url = "https://data.ssb.no/api/pxwebapi/v2/tables/08651/data"
    params = {
        "lang": "en",
        "outputFormat": "json-stat2"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def convert_to_dataframe(data):
    values = data["value"]

    dimensions = data["id"]
    sizes = data["size"]

    print("[INFO] Dimensions:", dimensions)
    print("[INFO] Sizes:", sizes)
    print("[INFO] Number of values:", len(values))

    df = pd.DataFrame({
        "value": values
    })

    return df


def main():
    data = fetch_ssb_data()
    df = convert_to_dataframe(data)

    print("[INFO] DataFrame created")
    print(df.head())


if __name__ == "__main__":
    main()