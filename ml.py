import pandas as pd
import requests

data = pd.read_csv("test.csv")
data["solarSystemName"] = None
for i, row in data.iterrows():
    r = requests.get(
        "https://api-serenity.eve-online.com.cn/killmails/" + str(row["kill_id"]) + "/" + str(row["hash"] + "/"))
    data.loc[i, "solarSystemName"] = r.json()["solarSystem"]["name"]
data.to_csv("eve1.csv", encoding="utf-8")
