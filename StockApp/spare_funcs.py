#table in the HTML that contains the pre-market gainers
#     table = soup.find('table', {'class': 'W(100%)'})

#     # Initialize an empty list to hold all the gainers data
#     gainers = []
#     symbols= []

#     # Loop through the table rows and fetch the data
#     for row in table.find_all('tr')[1:]:  # Skip the header row
#         columns = row.find_all('td')
#         if columns:
#             symbol = columns[0].text
#             name = columns[1].text
#             price = columns[2].text
#             change = columns[3].text
#             percent_change = columns[4].text
#             volume = columns[6].text

#             # Add the gainer data to the list
#             gainers.append({
#                 'Symbol': symbol,
#                 'Name': name,
#                 'Price': price,
#                 'Change': change,
#                 '% Change': percent_change,
#                 'Volume': volume
#             })
#             symbols.append(symbol)

#     # Create a DataFrame from the list of gainers
#     gainers_df = pd.DataFrame(gainers)

#     # Convert the '% Change' column to numeric values and sort by it
#     gainers_df['% Change'] = gainers_df['% Change'].str.rstrip('%').astype('float')
#     top_gainers_df = gainers_df.sort_values(by='% Change', ascending=False)

#     # Return the top 5 pre-market gainers
#     return top_gainers_df.head(5) , symbols

# # Get the top 5 pre-market gainers and print them
# top_5_gainers, symbols = get_pre_market_gainers()
# print(top_5_gainers)
