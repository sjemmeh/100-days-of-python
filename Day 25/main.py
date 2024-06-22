# data = []
# with open("weather_data.csv") as file:
#     for row in file.readlines():
#         values = row.strip()
#         data.append(values.split(","))
#
# print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240620.csv")
fur_count_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [0, 0, 0]
}
fur_count_dict["Count"][0] = len(data[data["Primary Fur Color"] == "Gray"])
fur_count_dict["Count"][1] = len(data[data["Primary Fur Color"] == "Cinnamon"])
fur_count_dict["Count"][2] = len(data[data["Primary Fur Color"] == "Black"])

fur_count_df = pandas.DataFrame(fur_count_dict)

fur_count_df.to_csv("squirrel_count.csv")