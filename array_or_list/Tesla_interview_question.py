

# 01.
# Using the requests, and pandas libraries (optional, you can  choose to - use whichever method) to create a function -which calculates the strike price for new hires at Tesla.
# Definitions:
# Strike price is determined to be the Median Closing Value
# for the 60 trading days  following their start date.
# Data provided are trading days prices
# Input: start date (string '2022-07-15*)
# Return: strike price Astring: 'Your strike price is $308.
# 9'
# )
# -Utilize the following API to fetch stock information:
# if you are not familiar with reading json data, let me
# know. I will provide the first step
# ##After reading json data from API,  select - ('Time Series
# (Daily) °]. Be sure to check the data
import sys
import json
import requests
import pandas as pd

API_URL = "https://www.alphavantage.co/query"
PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "outputsize": "compact",
    "datatype": "json",
    "apikey": "OAKHLGIDX4YR350T*"
}

COLUMNS = ('date', 'open', 'high', 'low', 'close', 'adjusted',
           'volume', 'dividend amount', 'split coefficient')


def fetch_data():
    with requests.Session() as s:
        download = s.get(API_URL, params=PARAMS)
        contents = download.content.decode('utf-8')
        return json.loads(contents)['Time Series (Daily)']


def dict_to_array(dic):
    key, value = dic
    return [key] + list(value.values())


def covert_to_df(data):
    data = map(dict_to_array, data.items())
    df = pd.DataFrame(data, columns=COLUMNS)
    return df


def calculates_the_strike_price(start):
    raw_data = fetch_data()
    df = covert_to_df(raw_data)
    df = df[df['date'] >= start][:60]
    return df['close'].astype(float).mean()


if __name__ == '__main__':
    stock_price = calculates_the_strike_price(sys.argv[1])
    print(f"Your strike price is ${stock_price :.2f}")


# #•02
# #-Given the array prices where prices[i]
# is the price of the ith item in a shop. There is a special discount for items in the shop,
# if you buy the ith item, then you will receive a discount equivalent to prices[j]
# where j is the minimum index such as  that j>i and prices[j] <= prices[i]
# otherwise, you will not receive any discount at all.

# # Input: [8,4,6,2,3] ---> i = 3 price[i]=6 and j =4 price[j]= 2  ---> discount= 2 == result =4
# * result: [4,4,4,2,3]

def get_discount(items):
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            yield items[i] - items[i+1]
        else:
            yield items[i]
    yield items[-1]


# print(list(get_discount([8,4,6,2,3])))


vehicles = [
    {"Vehicle": '5Y1', "FactoryGateDate": "2021-05-01",
        "Process": "Paint", "ProcessingTime": 100},
    {"Vehicle": '5Y1', 'FactoryGateDate': "2021-05-01",
        "Process": "GA", "ProcessingTime": 100},
    {"Vehicle": '5Y3', "FactoryGateDate": "2021-05-02",
        'Process': 'Paint', 'ProcessingTime': 100},
    {"Vehicle": '5Y3', 'FactoryGateDate': "2021-05-02",
        'Process': 'GA', "ProcessingTime": 100},
    {"Vehicle": '5Y2', 'FactoryGateDate': "2021-05-01",
        'Process': 'Paint', 'ProcessingTime': 50},
    {"Vehicle": '5Y2', 'FactoryGateDate': "2021-05-01",
        'Process': 'GA', 'ProcessingTime': 50}
]

# {'"2021-05-01" : {'5Y1': 200,  '5Y2: -100, - '"2021-05-02";
# {'5Y3': -200}

plans = [
    {'ProductionDay':  "2021-05-01", 'Plan': 0},
    {'ProductionDay': '2021-05-02', 'Plan': 2}
]


def blend_vehicle_with_plan(vehicles, plan):
    out_put = []
    for plan in plans:
        counter = 0
        plan_dict = {}
        plan_dict["AvgProcess"] = 0
        for vehicle in vehicles:
            if vehicle["FactoryGateDate"] == plan["ProductionDay"]:
                plan_dict["AvgProcess"] += vehicle["ProcessingTime"]
                counter += 1
        plan_dict["AvgProcess"] /= counter
        plan_dict["Plan"] = plan["Plan"]
        plan_dict["ProductionDay"] = plan["ProductionDay"]
        plan_dict["TotalCount"] = counter//len(plans)
        plan_dict["Delta"] = plan_dict["TotalCount"] - plan["Plan"]
        out_put.append(plan_dict)
    return out_put


print(blend_vehicle_with_plan(vehicles, plans))
