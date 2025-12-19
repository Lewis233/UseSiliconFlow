import json
import os

def make_empty_apikey_file():
    with open("APIKey.json", "w") as f:
        json.dump({"APIKey": "sk-xxxxxxxxxx"}, f, indent=4)

def check_apikey_valid():
    if not os.path.exists("APIKey.json"):
        make_empty_apikey_file()
        return False

    with open("APIKey.json", "r") as f:
        data = json.load(f)
        apikey = data.get("APIKey")
        if apikey is None or apikey == "sk-xxxxxxxxxx":
            return False
        return True
    
def write_apikey(apikey: str):
    with open("APIKey.json", "w") as f:
        json.dump({"APIKey": apikey}, f, indent=4)

if __name__ == "__main__":
    if not os.path.exists("APIKey.json"):
        make_empty_apikey_file()
    print("The APIKey is","Valid" if check_apikey_valid() else "Invalid")