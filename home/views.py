from django.shortcuts import render, HttpResponse

#.....
from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import requests
import os
import json
import csv
#.....

# Create your views here.
def home(request):
    context = {'name' : "Asiya", "course": "Programming"}
    #return HttpResponse("This is my home page (/)")
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse("This is my about page ")
    return render(request, 'about.html')


def projects(request):
    #API not working
    # API_Key = "RC21E6QKCDX9UVUW"
    # #API_Key = "ZQQ7GGTAMO4QUVYB"
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={API_Key}'
    # r = requests.get(url)
    # data = r.json()
    # data = dict(list(data["Time Series (Daily)"].items())[:20])

    # for key, value in data.items():
    #     data[key] = data[key]["1. open"]

    # days = [int(date[-2:]) for date in data.keys()][::-1]  # Extracting day numbers
    # opens = [data[date] for date in data.keys()][::-1]

    #Redundancy Issue
    '''with open("C:/Users/Tesla Laptops/OneDrive/Desktop/daily_IBM.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    # Convert data to JSON string
    data_json = json.dumps(data, indent=4)
    # Parse JSON string back to list of dictionaries
    data_list = json.loads(data_json)
    # Create an empty dictionary to store the result
    result_dict = {}

    for item in data_list:
        date = item['date']
        open_price = float(item["open"])
        result_dict[date] = open_price
    days = [int(date.split('/')[1]) for date in result_dict.keys()] # Extracting day numbers
    opens = [result_dict[date] for date in result_dict.keys()]
    plt.plot(days, opens, marker='o', linestyle='-')
    plt.xlabel('Day')
    plt.ylabel('Open Value')
    plt.title('Open Values Over Time')
    # Save the visualization to a file in the static directory
    plot_file = os.path.join('static', 'open_values.jpg')
    plt.savefig(plot_file)

    for item in data_list:
        date = item['date']
        high_price = float(item["high"])
        result_dict[date] = high_price
    days = [int(date.split('/')[1]) for date in result_dict.keys()] # Extracting day numbers
    highs = [result_dict[date] for date in result_dict.keys()]
    plt.plot(days, highs, marker='o', linestyle='-')
    plt.xlabel('Day')
    plt.ylabel('HIgh Value')
    plt.title('High Values Over Time')
    # Save the visualization to a file in the static directory
    plot_file = os.path.join('static', 'high_values.jpg')
    plt.savefig(plot_file)

    for item in data_list:
        date = item['date']
        low_price = float(item["low"])
        result_dict[date] = low_price
    days = [int(date.split('/')[1]) for date in result_dict.keys()] # Extracting day numbers
    lows = [result_dict[date] for date in result_dict.keys()]
    plt.plot(days, lows, marker='o', linestyle='-')
    plt.xlabel('Day')
    plt.ylabel('Low Value')
    plt.title('Low Values Over Time')
    # Save the visualization to a file in the static directory
    plot_file = os.path.join('static', 'low_values.jpg')
    plt.savefig(plot_file)

    for item in data_list:
        date = item['date']
        volume = float(item["volume"])
        result_dict[date] = volume
    days = [int(date.split('/')[1]) for date in result_dict.keys()] # Extracting day numbers
    volumes = [result_dict[date] for date in result_dict.keys()]
    plt.plot(days, volumes, marker='o', linestyle='-')
    plt.xlabel('Day')
    plt.ylabel('Volume')
    plt.title('Volume Over Time')
    # Save the visualization to a file in the static directory
    plot_file = os.path.join('static', 'volume.jpg')
    plt.savefig(plot_file)'''

    #return HttpResponse("This is my projects page ")
    return render(request, 'projects.html')


def stock(request):
    #return HttpResponse("This is my contact page ")
    return render(request, 'stock.html')
