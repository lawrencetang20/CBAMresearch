import pandas as pd

csvfile = 'data/2021trade6digit.csv'

df = pd.read_csv(csvfile, dtype={'hs_product_code': str}, low_memory=False)

selected_columns = ['location_code', 'partner_code', 'hs_product_code', 'export_value']
data = df[selected_columns].copy()

other_countries = {'USA', 'CAN', 'MEX', 'BRA', 'IND', 'CHN', 'RUS', 'GBR'} # to add another country, add here and BELOW
EU_countries = {'AUT', 'BEL', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LTU', 'LUX', 'MLT', 'NLD', 'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'SWE'}

# add more sectors here
crude = {'270900'}
gas = {'2711'}
refined = {'271000'}
iron_steel = {'72', '260112', '7301', '7302', '730300', '7304', '7305', '7306', '7307', '7308', '730900', '7310', '731100', '7318', '7326'}
iron_steel_exceptions = {'72022', '720230', '720250', '720270', '720280', '720291', '720292', '720293', '720299', '7204'}
fertilizer = {'280800', '2814', '283421', '3102', '3105'}
fertilizer_exceptions = {'310560'}
aluminum = {'7601', '7603', '7604', '7605', '7606', '7607', '7608', '760900', '7610', '761100', '7612', '761300', '7614', '7616'}
chemicals = {'280410'}

# add elif statement here if you add more sectors
def map_to_sector(hs_product_code):
  if hs_product_code in chemicals:
    return 'chemicals'
  elif (hs_product_code[0:4] in fertilizer or hs_product_code in fertilizer) and (hs_product_code not in fertilizer_exceptions):
    return 'fertilizer'
  elif hs_product_code[0:4] in aluminum or hs_product_code in aluminum:
    return 'alumninum'
  elif (hs_product_code[0:2] in iron_steel or hs_product_code[0:4] in iron_steel or hs_product_code in iron_steel) and not (hs_product_code[0:4] in iron_steel_exceptions or hs_product_code[0:5] in iron_steel_exceptions or hs_product_code in iron_steel_exceptions):
    return 'iron/steel'
  elif hs_product_code in crude:
    return 'crude'
  elif hs_product_code[0:4] in gas:
    return 'gas'
  elif hs_product_code in refined:
    return 'refined'
  else:
    return 'other'

def country_assignment(country):
  if country in other_countries:
    return country
  elif country in EU_countries:
    return 'EU'
  else:
    return 'ROW'

data['sector'] = data['hs_product_code'].apply(map_to_sector)
data.loc[:, 'sector'] = data['sector']

# test = data[data['sector'] == 'iron/steel']
# test.to_csv('test.csv', index=False)

data['destination'] = data['location_code'].apply(country_assignment)
data.loc[:, 'destination'] = data['destination']

data['origin'] = data['partner_code'].apply(country_assignment)
data.loc[:, 'origin'] = data['origin']

grouped_data = data.groupby(['sector', 'destination', 'origin']).sum().reset_index()

grouped_data_reset = grouped_data.reset_index()
sorted_data = grouped_data.sort_values(by=['destination', 'sector'])

# fills in categories where we have 0 so we have a data point for each combination
sectors = sorted_data['sector'].unique()
destinations = ['USA', 'CAN', 'MEX', 'BRA', 'IND', 'CHN', 'RUS', 'EU', 'ROW', 'GBR'] # ADD HERE FOR NEW COUNTRY TOO
all_combinations = [(sector, destination, origin) for sector in sectors for destination in destinations for origin in destinations]

template_data = pd.DataFrame(all_combinations, columns=['sector', 'destination', 'origin'])

merged_data = pd.merge(template_data, sorted_data, on=['sector', 'destination', 'origin'], how='left').fillna(0)

sorted_merged_data = merged_data.sort_values(by=['destination', 'sector'])
sorted_merged_data = sorted_merged_data[sorted_merged_data['destination'] != sorted_merged_data['origin']]

no_other = sorted_merged_data[sorted_merged_data['sector'] != 'other']

no_other.to_csv('trade_data.csv', index=False)
print('trade data saved to trade_data.csv')

