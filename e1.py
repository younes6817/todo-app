import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter city name: ")

for row in data:
    if city == row[0]:
        print(row[1])

# print(data)