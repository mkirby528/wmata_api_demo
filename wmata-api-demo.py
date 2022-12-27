import requests
API_KEY: str = "<API_KEY_GOES_HERE>"
HEADERS = {
    "api_key": API_KEY
}
TRAIN_LINE_MAPPING = {"SV": "Silver",
                      "OR": "Orange",
                      "BL": "Blue",
                      "RD": "Red",
                      "GR": "Green",
                      "YL": "Yellow"
                      }


def get_next_trains(station: str):
    uri = f'https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{station}'
    incoming_trains = requests.get(uri, headers=HEADERS).json()['Trains']
    formatted_trains = []
    for train in incoming_trains:
        formatted_train_data = {}
        formatted_train_data["line"] = TRAIN_LINE_MAPPING[train["Line"]]
        formatted_train_data["destination"] = train["DestinationName"]
        formatted_train_data["min_away"] = train["Min"]
        formatted_trains.append(formatted_train_data)
    return formatted_trains


def main():
    next_trains = get_next_trains('K02')
    for train in next_trains:
        print(train)


main()
