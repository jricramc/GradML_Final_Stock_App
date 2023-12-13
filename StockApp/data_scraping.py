# from polygon import RESTClient

# client = RESTClient(api_key="c6T0CxJSsS12geETIbr15rl_5X61otI3")

# ticker = "AAPL"

# # List Aggregates (Bars)
# aggs = []
# for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
#     aggs.append(a)

# print(aggs)

# # Get Last Trade
# trade = client.get_last_trade(ticker=ticker)
# print(trade)

# # List Trades
# trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
# for trade in trades:
#     print(trade)

# # Get Last Quote
# quote = client.get_last_quote(ticker=ticker)
# print(quote)

# # List Quotes
# quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
# for quote in quotes:
#     print(quote)

# from polygon import RESTClient

# # Assuming RESTClient is a valid imported module and api_key is correctly provided.
# def save_to_file(data, filename, mode='w'):
#     with open(filename, mode) as f:
#         for item in data:
#             f.write(f"{item}\n")

# stocks= ["RIOT", "CLSK", "LYFT", "OPEN", "RIG", "RUN", "MARA", "IONQ", 
# "GSAT", "HBI", "BB", "ZIM", "MNMD", "RUM", "IOVA", "GERN", "TAL", "SWN"]

# def fetch_and_save_data(api_key):
#     client = RESTClient(api_key)

#     ticker = "RIOT"

#     #####
#      """
# #     For each stock

#     I will get all this data per week:
#         - the price that the stock had at the 1hr interval for 1 week
#         - the variance of the stock each day of the week
#         - highest percentage range in each day

#         To-Compute
#         - avg volume traded per hour in each day
#         - avg distance from positive and negative points of resistance observed in the stock
#         - largest one day variance in the span of each time-period
#     """
    
#     # Save aggregates to a file
#     aggs = client.list_aggs(ticker=ticker, multiplier=1, timespan="hour", from_="2023-01-09", to="e", limit=5000)
#     save_to_file(aggs, "test1.txt")

    

# # Calling the function with an API key
# fetch_and_save_data("c6T0CxJSsS12geETIbr15rl_5X61otI3")



# Save last trade to a file
    # trade = client.get_last_trade(ticker=ticker)
    # save_to_file([trade], "last_trade.txt")

    # Save list of trades to a file
    # trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
    # save_to_file(trades, "trades.txt")

    # Save last quote to a file
    # quote = client.get_last_quote(ticker=ticker)
    # save_to_file([quote], "last_quote.txt")

    # # Save list of quotes to a file
    # quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
    # save_to_file(quotes, "quotes.txt")


from polygon import RESTClient
import os
import datetime
import time

def save_to_file(data, filename, mode='w'):
    with open(filename, mode) as f:
        for item in data:
            f.write(f"{item}\n")

def calculate_variance(data):
    return data.high - data.low

def calculate_range_percentage(data):
    return ((data.high - data.low) / data.low) * 100


first_stocks = ["RIOT", "CLSK", "LYFT", "OPEN", "RIG", "RUN", "MARA", "IONQ", "GSAT", "HBI", "BB", "ZIM", "MNMD", "RUM", "IOVA", "GERN", "TAL", "SWN"]

stocks= ["AAL", "ABR", "ADT", "AGI", "AGL", "AGNC", "ALIT", "AM", "AMBP", "APLE", "AQN", "AROC", "ARRY", "ASAN", "ASB", "AU", 
"AUR", "AVDX", "BB", "BE", "BGC", "BHC", "BILI", "BNL", "BRFS", "BTE", "BTG", "BVN", "BZ", "CCCS", "CHWY", "CIG", "CLF", "CLVT", "CNX", 
"CPG", "CRDO", "CRK", "CUK", "CVBF", "CWAN", "CWK", "CXM", "DBRG", "DEI", "DISH", "DNA", "DNB", "DNUT", "DOC", "DRS", "DRVN", "EGO", 
"ELAN", "ENLC", "EQC", "ERF", "ERJ", "ETRN", "EURN", "EXPI", "EXTR", "FBP", "FHN", "FNB", "FOLD", "FRO", "FSK", "FSLY", "FTI", "FULT", 
"GDRX", "GGAL", "GGB", "GME", "GNL", "GNW", "GSAT", "GT", "GTES", "GTX", "HAYW", "HL", "HMY", "HR", "IBRX", "ICL", "IONQ", "IQ", "IRT", 
"IVZ", "JOBY", "JWN", "KD", "KGC", "KOS", "LBRT", "LBTYA", "LBTYK", "LCID", "LEVI", "LTHM", "LXP", "LYFT", "LZ", "M", "MAC", "MANU", 
"MARA", "MAT", "MCW", "MDU", "MIR", "MLCO", "MNSO", "MODG", "MP", "MPW", "MQ", "MTG", "NCLH", "NEA", "NEOG", "NLY", "NOV", "NWL", 
"NXE", "NYCB", "OBDC", "OGN", "OI", "ONB", "OPEN", "OUT", "OWL", "PAAS", "PACB", "PAGP", "PAGS", "PARA", "PDI", "PHYS", "PK", "PLTK", 
"PLUG", "PR", "PSEC", "PSLV", "PTEN", "QS", "RCM", "RELY", "RIG", "RIOT", "RITM", "RKLB", "RLX", "ROIV", "RUN", "SBRA", "SBS", "SBSW", 
"SHLS", "SHO", "SID", "SITC", "SLM", "SOFI", "SONO", "SSRM", "STNE", "SWN", "TAL", "TCN", "TDOC", "TDS", "TGNA", "TGTX", "TME", "TOST", 
"TRIP", "UA", "UAA", "UE", "UEC", "UGP", "VFC", "VIPS", "VLY", "VSTS", "VYX", "WEN", "WU", "YMM", "YPF", "ZI"]


# def fetch_and_save_data(api_key):
#     client = RESTClient(api_key)

#     # Create a folder for each stock
#     for stock in stocks:
#         os.makedirs(stock, exist_ok=True)
#         start_date = datetime.date(2023, 1, 1)
#         end_date = datetime.date(2023, 12, 1)

#         # Iterate through weeks
#         while start_date < end_date:
#             week_end_date = start_date + datetime.timedelta(days=6)
#             if week_end_date > end_date:
#                 week_end_date = end_date

#             # Fetch data for the week
#             aggs = client.list_aggs(ticker=stock, multiplier=1, timespan="hour", from_=start_date.isoformat(), to=week_end_date.isoformat(), limit=5000)

#             # Create a filename for the week
#             filename = f"{stock}/{start_date.isoformat()}_to_{week_end_date.isoformat()}.txt"
#             save_to_file(aggs, filename)

#             # time.sleep(15)

#             # Move to the next week
#             start_date = week_end_date + datetime.timedelta(days=1)

# Calling the function with an API key

# def fetch_and_save_data(api_key):
#     client = RESTClient(api_key)

#     for stock in stocks:
#         os.makedirs(stock, exist_ok=True)
#         start_date = datetime.date(2023, 1, 1)
#         end_date = datetime.date(2023, 12, 1)

#         while start_date < end_date:
#             week_end_date = start_date + datetime.timedelta(days=6)
#             if week_end_date > end_date:
#                 week_end_date = end_date

#             # # Fetch hourly data
#             # hourly_aggs = client.list_aggs(ticker=stock, multiplier=1, timespan="hour", from_=start_date.isoformat(), to=week_end_date.isoformat(), limit=5000)
#             # hourly_filename = f"{stock}/{start_date.isoformat()}_to_{week_end_date.isoformat()}_hourly.txt"
#             # save_to_file(hourly_aggs, hourly_filename)

#             # Fetch daily data
#             daily_aggs_generator = client.list_aggs(ticker=stock, multiplier=1, timespan="day", from_=start_date.isoformat(), to=week_end_date.isoformat(), limit=5000)

#             max_variance_day = None
#             max_range_percentage_day = None
#             max_variance = -1
#             max_range_percentage = -1

#             for daily_agg in daily_aggs_generator:
#                 variance = calculate_variance(daily_agg)
#                 range_percentage = calculate_range_percentage(daily_agg)

#                 if variance > max_variance:
#                     max_variance = variance
#                     max_variance_day = daily_agg

#                 if range_percentage > max_range_percentage:
#                     max_range_percentage = range_percentage
#                     max_range_percentage_day = daily_agg



#             summary_filename = f"{stock}/{start_date.isoformat()}_to_{week_end_date.isoformat()}_summary.txt"
#             with open(summary_filename, 'w') as f:
#                 f.write(f"Max Variance Day: {max_variance_day}\n")
#                 f.write(f"Max Variance : {max_variance}\n")
#                 f.write(f"Max Range Percentage Day: {max_range_percentage_day}\n")
#                 f.write(f"Max Range Percentage: {max_range_percentage}\n")

#             # Move to the next week
#             start_date = week_end_date + datetime.timedelta(days=1)

# fetch_and_save_data("c6T0CxJSsS12geETIbr15rl_5X61otI3")


def calculate_weekly_change(open_price, close_price):
    return ((close_price - open_price) / open_price) * 100

def calculate_average_hourly_volume(total_volume, trading_days, hours_per_day=6.5):
    return total_volume / (trading_days * hours_per_day)

def fetch_weekly_data(api_key, stocks):
    client = RESTClient(api_key)

    for stock in stocks:
        os.makedirs(stock, exist_ok=True)
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 12, 1)

        while start_date < end_date:
            week_end_date = start_date + datetime.timedelta(days=6)
            if week_end_date > end_date:
                week_end_date = end_date

            # Fetch weekly data
            weekly_aggs = client.list_aggs(ticker=stock, multiplier=1, timespan="week", from_=start_date.isoformat(), to=week_end_date.isoformat(), limit=5000)
            
            total_volume = 0
            trading_days = 0

            weekly_summary_filename = f"{stock}/{start_date.isoformat()}_to_{week_end_date.isoformat()}_summary.txt"

            for weekly_agg in weekly_aggs:
                # Check if the necessary attributes are present in the Agg object
                if hasattr(weekly_agg, 'open') and hasattr(weekly_agg, 'close'):
                    open_price = weekly_agg.open
                    close_price = weekly_agg.close
                    weekly_change = calculate_weekly_change(open_price, close_price)
                    final_price = close_price
                    total_volume += weekly_agg.volume if hasattr(weekly_agg, 'volume') else 0
                    trading_days += 1

                    # Append the calculated information to the existing summary file
                    # with open(weekly_summary_filename, 'a') as f:
                    #     f.write(f"Weekly Change: {weekly_change:.2f}%\n")
                    #     f.write(f"Final Price: {final_price}\n")
                else:
                    # Handle cases where open or close price is not available
                    # You can choose to log this information or take other appropriate actions
                    print(f"Missing data for {stock} on {start_date}")
                        # Calculate average hourly volume
                if trading_days > 0:
                    average_hourly_volume = calculate_average_hourly_volume(total_volume, trading_days)
                    # Append the average hourly volume to the existing summary file
                    with open(weekly_summary_filename, 'a') as f:
                        f.write(f"Average Hourly Volume: {average_hourly_volume:.2f}\n")

            # Move to the next week
            
            start_date = week_end_date + datetime.timedelta(days=1)
fetch_weekly_data("c6T0CxJSsS12geETIbr15rl_5X61otI3", stocks)


def calculate_pivot_points(data):
    if not data:
        # Handle the case where data is empty
        return None, None, None, None, None, None, None

    high = max(item['high'] for item in data)
    low = min(item['low'] for item in data)
    close = data[-1]['close']
    
    # Calculate Pivot Point
    PP = (high + low + close) / 3

    # Calculate support and resistance levels
    R1 = (2 * PP) - low
    S1 = (2 * PP) - high
    R2 = PP + (high - low)
    S2 = PP - (high - low)
    R3 = high + 2 * (PP - low)
    S3 = low - 2 * (high - PP)

    return PP, R1, S1, R2, S2, R3, S3

def count_resistance_points(data, resistance_levels, tolerance_percentage=0.5, time_frame_hours=70):
    if not data:
        # Handle the case where data is empty
        # Return appropriate default values or handle this case as needed
        return 0, 0, [], [], None, None
    high_resistance_hits = low_resistance_hits = 0
    high_resistance_points = []
    low_resistance_points = []

    resistance_levels = [level for level in resistance_levels if level is not None]

    tolerance_values = [level * tolerance_percentage / 100 for level in resistance_levels]

    for i, item in enumerate(data):
        for j, level in enumerate(resistance_levels):
            level_range = (level - tolerance_values[j], level + tolerance_values[j])

            if i + time_frame_hours < len(data):
                for k in range(i, i + time_frame_hours):
                    if j < 3 and level_range[0] <= data[k]['high'] <= level_range[1]:
                        high_resistance_hits += 1
                        high_resistance_points.append((k, data[k]['high']))
                        break
                    elif j >= 3 and level_range[0] <= data[k]['low'] <= level_range[1]:
                        low_resistance_hits += 1
                        low_resistance_points.append((k, data[k]['low']))
                        break

    # Calculating distances
    last_low_trade = data[-1]['low']
    nearest_lower_resistance = min(resistance_levels[3:], key=lambda x: abs(x - last_low_trade))
    distance_from_lower_resistance = abs(last_low_trade - nearest_lower_resistance)

    if high_resistance_points and low_resistance_points:
        highest_hit = max(high_resistance_points, key=lambda x: x[1])[1]
        lowest_hit = min(low_resistance_points, key=lambda x: x[1])[1]
        distance_between_resistances = highest_hit - lowest_hit
    else:
        distance_between_resistances = None

    return high_resistance_hits, low_resistance_hits, high_resistance_points, low_resistance_points, distance_from_lower_resistance, distance_between_resistances


# Assuming weekly_data is a list of Agg objects for a week

# Convert to a list of dictionaries for easier processing
# formatted_data = [{'open': agg.open, 'high': agg.high, 'low': agg.low, 'close': agg.close} for agg in weekly_data]

# pivot_point, R1, S1, R2, S2, R3, S3 = calculate_pivot_points(formatted_data)
# resistance_levels = [pivot_point, R1, R2, R3, S1, S2, S3]

# high_hits, low_hits = count_resistance_points(formatted_data, resistance_levels)

# print(f"High Resistance Hits: {high_hits}, Low Resistance Hits: {low_hits}")


def find_resistance_levels(hourly_data, cluster_range=0.02):
    # hourly_data is a list of dictionaries with 'low' and 'volume' keys
    # cluster_range is the price range within which lows are considered the same level

    # Create a dictionary to count frequency of lows within a cluster range
    resistance_levels = {}
    
    for data_point in hourly_data:
        low_price = data_point['low']
        
        # Find the cluster this low belongs to
        found_cluster = False
        for level in resistance_levels:
            if abs(level - low_price) <= cluster_range:
                resistance_levels[level]['frequency'] += 1
                resistance_levels[level]['volume'] += data_point['volume']
                found_cluster = True
                break
        
        if not found_cluster:
            resistance_levels[low_price] = {'frequency': 1, 'volume': data_point['volume']}
    
    # Convert to list and sort by frequency and volume
    resistance_levels = [{'price': level, 'frequency': info['frequency'], 'volume': info['volume']} for level, info in resistance_levels.items()]
    resistance_levels.sort(key=lambda x: (-x['frequency'], -x['volume']))
    
    return resistance_levels




import os
import datetime
# from your_rest_client import RESTClient  # Import your RESTClient

def fetch_res_data(api_key, stocks):
    client = RESTClient(api_key)

    for stock in stocks:
        os.makedirs(stock, exist_ok=True)
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date(2023, 12, 1)

        while start_date < end_date:
            week_end_date = start_date + datetime.timedelta(days=6)
            if week_end_date > end_date:
                week_end_date = end_date

            # Fetch hourly data for the week
            hourly_aggs = client.list_aggs(ticker=stock, multiplier=1, timespan="hour", from_=start_date.isoformat(), to=week_end_date.isoformat(), limit=5000)

            # Process the data
            formatted_data = [{'open': agg.open, 'high': agg.high, 'low': agg.low, 'close': agg.close} for agg in hourly_aggs]

            pivot_point, R1, S1, R2, S2, R3, S3 = calculate_pivot_points(formatted_data)
            resistance_levels = [pivot_point, R1, R2, R3, S1, S2, S3]
            # high_hits, low_hits = count_resistance_points(formatted_data, resistance_levels)

            weekly_summary_filename = f"{stock}/{start_date.isoformat()}_to_{week_end_date.isoformat()}_summary.txt"

            high_hits, low_hits, high_points, low_points, distance_from_lower, distance_between = count_resistance_points(formatted_data, resistance_levels)

            with open(weekly_summary_filename, 'a') as f:
                f.write(f"Resistance Levels: {resistance_levels}\n")
                f.write(f"High Hits: {high_hits}, Points: {high_points}\n")
                f.write(f"Low Hits: {low_hits}, Points: {low_points}\n")
                f.write(f"Distance from Lower Resistance on Last Trade: {distance_from_lower}\n")
                f.write(f"Distance Between High and Low Resistance Points: {distance_between}\n")




            # Optional: Sleep to avoid hitting API rate limits
            # time.sleep(15)

            # Move to the next week
            start_date = week_end_date + datetime.timedelta(days=1)

    

# fetch_res_data("c6T0CxJSsS12geETIbr15rl_5X61otI3", stocks)