# # import yfinance as yf

# import yfinance as yf

# # Define the ticker symbol
# ticker_symbol = "VLY"

# # Create a Ticker object
# ticker = yf.Ticker(ticker_symbol)

# print(ticker.info)

# # Specify the time frame
# start_date = "2022-01-01"
# end_date = "2022-03-31"

# # Get historical data
# historical_data = ticker.history(start=start_date, end=end_date)

# # Example calculations
# average_close_price = historical_data['Close'].mean()
# total_volume = historical_data['Volume'].sum()

# print("Average Close Price:", average_close_price)
# print("Total Volume Traded:", total_volume)


# Print the historical data
# print(historical_data)






# # List of company ticker symbols
# companies = ["RIOT", "CLSK"]

# # Function to get the number of employees for each company
# def get_number_of_employees(companies):
#     employee_counts = {}
#     for company in companies:
#         ticker = yf.Ticker(company)
#         print(ticker)
#         info = ticker.info
#         print(info)
#         employee_counts[company] = info.get('fullTimeEmployees')
#     return employee_counts

# # Get the number of employees for each company
# employee_counts = get_number_of_employees(companies)
# print(employee_counts)

# import yfinance as yf
# msft = yf.Ticker("AAL")

# quarterly_earnings = msft.quarterly_cashflow
# print(quarterly_earnings)
# net_income = quarterly_earnings.loc['Net Income From Continuing Operations']
# print(net_income)


# stocks= ["AAL"]

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


import yfinance as yf
import os


# Fetching data for Microsoft
def fetch_macro_data(stocks):

   

    for stock in stocks:
        os.makedirs(stock, exist_ok=True)
        marcro_filename = f"{stock}/2022-macro_data.txt"

        ticker = yf.Ticker(stock)

    # Getting quarterly cash flow data
        # quarterly_cashflow = ticker.quarterly_cashflow

        # print("quarterly", quarterly_cashflow)

        # # Extracting and printing net income for each quarter
        # # if quarterly_cashflow is not None and 'Net Income From Continuing Operations' in quarterly_cashflow.index:
        # net_income = quarterly_cashflow.loc['Net Income From Continuing Operations']
            # print(net_income)
        # else:
        #     print("Net Income data not available")


        # employees = ticker.info.get('fullTimeEmployees')
        # industry = ticker.info.get('industry')
        # market_cap= ticker.info.get('marketCap')
        # two_hundred_day_avg= ticker.info.get('twoHundredDayAverage')
        # enterprise_value= ticker.info.get('enterpriseValue')
        # earnings_quarterly_growth= ticker.info.get('earningsQuarterlyGrowth')
        # revenue_growth= ticker.info.get('revenueGrowth')

        volatility_beta= ticker.info.get('beta')
        # peg_ratio= ticker.info.get('pegRatio')
        # fifty_day_average= ticker.info.get('fiftyDayAverage')
        # ebitda= ticker.info.get('ebitda')

        # sector= ticker.info.get('sector')

        # volume= ticker.info.get('volume')
        

        with open(marcro_filename, 'a') as f:
        
            # f.write(f"Net Income: {net_income}\n")

            # f.write(f"Employees: {employees}\n")
            # f.write(f"Industry: {industry}\n")
            # f.write(f"Market Cap: {market_cap}\n")
            # f.write(f"Enterprise Value: {enterprise_value}\n")
            # f.write(f"Volume: {volume}\n")
            # f.write(f"Sector: {sector}\n")
            # f.write(f"200-Day Average: {two_hundred_day_avg}\n")
            
            # f.write(f"Earnings Quarterly Growth: {earnings_quarterly_growth}\n")
            # f.write(f"Revenue Growth: {revenue_growth}\n\n")

            f.write(f"Volatity Beta: {volatility_beta}\n")
            # f.write(f"Price/Earnings to Growth ratio: {volatility_beta}\n\n")
            # f.write(f"50-Day Average: {fifty_day_average}\n\n")
            # f.write(f"Earnings Before Interest, Taxes, Depreciation, and Amortization: {ebitda}\n\n")

           

            # volume



fetch_macro_data(stocks)
