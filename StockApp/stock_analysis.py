import finnhub
import pandas as pd
finnhub_client = finnhub.Client(api_key="cl4f9hpr01qrlanplm6gcl4f9hpr01qrlanplm70")
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import json
import re
import time
from datetime import datetime
import pytz

# current_timestamp = int(time.time())
# print(current_timestamp)


# The URL where the pre-market gainers are found on Webull
def top_webull_pre_market_stocks(x):
    url = "https://www.webull.com/quote/us/gainers/pre"

    # Send a GET request to the Webull URL
    response = requests.get(url)
    response.raise_for_status()  # This will raise an exception if the request failed

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Fetch the page content
    response = requests.get(url)
    response.raise_for_status()


    # print(response.text)
    # # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tags = soup.find_all('script')
    script_tag=script_tags[0]

    script_tag_string = str(script_tag)

    # Use regular expressions to extract the JSON object
    # We are looking for an object that starts with `{"` and ends with `"};`
    json_str_match = re.search(r'window\.__initState__=({.*?});', script_tag_string)

    if json_str_match:
        json_str = json_str_match.group(1)  # This should be the JSON string
        data = json.loads(json_str)  # Parse the JSON string into a Python dictionary

        # Now you can access the data as before
        result= []
        stocks_data = data['quoteHomeData']['gainers']['data']
        top_x_stocks= x #how many of the top stocks do you want to see.
        i= 0
        for stock in stocks_data:
            if i>top_x_stocks:
                break
            else:
                ticker = stock['ticker']
                name = ticker['name']
                symbol = ticker['symbol']
                # market_value = ticker['marketValue']
                result.append((symbol))
                i+=1
            # ... and so on, for other fields you're interested in.
    else:
        print("JSON string not found in the script tag.")

    return result


test_time = 1699622220


start_premarket= 1699606800
end_premarket= 1699626600

# data_for_csv = []


def pre_market_visualizer():
    result= ['INVO','TCON','MRAI','INBS', 'DRCT']
    for stock in result:
        # res = finnhub_client.stock_candles(stock, '1', test_time, test_time+ 300 )
        res = finnhub_client.stock_candles(stock, '1', start_premarket-10000, end_premarket )
        print(stock, res)
        # print ('open', res['o'])


        percentage = np.round((np.array(res['c'][1:])/np.array(res['c'][:-1])) - 1, 4)
        # percentage= (diff/np.array(res['o']))*100
        # print(percentage)
        # data_for_csv.append([stock] + percentage.tolist())


        minutes = np.arange(len(percentage))

        plt.figure(figsize=(15,5))  # Set the figure size to be larger for better visibility
        plt.plot(minutes, percentage, marker='o', linestyle='-', color='blue')
        plt.title(f'Stock Price Percentage Changes per Minute for {stock}')
        plt.xlabel('Minutes')
        plt.ylabel('Percentage Change (%)')
        plt.grid(True)
        plt.show()

# pre_market_visualizer()


# Function to convert Unix timestamp to human-readable date
def convert_unix_to_readable(unix_timestamp):
    times = []
    if len(unix_timestamp) == 0:
        return None
    else:
        # Define the Eastern timezone
        eastern = pytz.timezone('US/Eastern')
        for i in unix_timestamp:
            # Convert the timestamp to a datetime object in UTC
            utc_time = datetime.utcfromtimestamp(i).replace(tzinfo=pytz.utc)
            # Convert the UTC time to Eastern time
            eastern_time = utc_time.astimezone(eastern).strftime('%Y-%m-%d %H:%M:%S')
            times.append(eastern_time)
        return times

time_test= 1699617600

# result_test= ['INVO','TCON','MRAI','INBS', 'DRCT']


def indicators():
    # result= ['INVO','TCON','MRAI','INBS', 'DRCT']
    result = top_webull_pre_market_stocks(7)
    # print(result)
    indicators=[]
    alert_flag = False
    current_timestamp = int(time.time())
    for stock in result:
            # res = finnhub_client.stock_candles(stock, '1', test_time, test_time+ 300 )
            res = finnhub_client.stock_candles(stock, '1', current_timestamp-120, current_timestamp, timeout=10)
            try:
                percentages = np.round((np.array(res['c'][1:])/np.array(res['c'][:-1])) - 1, 4)
            except:
                continue
                
            strong_candle_times = []
            strong_look_times = []
            strong_traction_times = []

            for i in range(len(percentages)):
                # Check for strong candle condition
                if percentages[i] > 0.13:  # 0.15 representing 15%
                    strong_candle_times.append(time_test + (i+1)*60)  # Adjusted to (i+1) for correct timing
                    print('stock', stock, percentages[i],time_test + (i+1)*60)
                    alert_flag = True
                

                # Check for strong look condition
                if i < len(percentages) - 2:  # Ensure there are enough elements left
                    if percentages[i] > 0.07 and percentages[i+1] > 0.07 and percentages[i+2] > 0.07:
                        strong_look_times.append(time_test + (i+1)*60)
                        alert_flag = True  # Adjusted to (i+1) for correct timing

                # Check for strong traction condition
                if i < len(percentages) - 1:  # Ensure there is at least one element left
                    if percentages[i] > 0.10 and percentages[i+1] > 0.10:
                        print(percentages[i])
                        strong_traction_times.append(time_test + (i+1)*60)  # Adjusted to (i+1) for correct timing
                        alert_flag = True


            # indicators.append((stock, convert_unix_to_readable(strong_candle_times),convert_unix_to_readable(strong_look_times), convert_unix_to_readable(strong_traction_times)))
            indicators.append({
            'stock': stock,
            'strong_candle': convert_unix_to_readable(strong_candle_times),
            'alert': alert_flag,  # Include the alert flag in the result
            'strong_look': convert_unix_to_readable(strong_look_times),
            'strong_traction': convert_unix_to_readable(strong_traction_times)
        })
    return indicators


def run_stock_analysis():
    # return pre_market_visualizer()

    # result = top_webull_pre_market_stocks(5)
    # pre_market_visualizer(result)
    # Add any other function calls you need and format the results
    indicators_result = indicators()
    # # Format and return the results
    return indicators_result

if __name__ == "__main__":
    run_stock_analysis()


#127.0.0.1 - - [15/Nov/2023 08:02:16] "GET /alerts HTTP/1.1" 200 -
#['CMMB', 'HSCS', 'BURU', 'KNTE', 'SLDB']