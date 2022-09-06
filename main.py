from bs4 import BeautifulSoup
import requests
import pandas as pd

url= "https://www.numbeo.com/quality-of-life/rankings_by_country.jsp"
page=requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')


result = []
table=soup.find('table', id="t2")
# print(len(table))
tbody=table.find('tbody')
# print(tbody)
for i, tr in enumerate(tbody.find_all('tr'), 1):
    td = tr.find_all('td')
    data_list = []
    for data in td:
        # print(data)
        x = data.text.strip()
        data_list.append(x)

    data_list.insert(0, i)
    del data_list[1]
    print(f"{data_list}")

    result.append(data_list)
    
    
# print(result)

df = pd.DataFrame(result, columns = ['rank','country','quality_of_life','purchasing_power_index','safety_index','health_care_index','cost_of_living_index','property_price_to_income_ratio','traffic_commute_time_index','pollution_index', 'climate_index' ])
file_name = "health.csv"
df.to_csv(file_name,index=False)
print(df)

# drop_cols = ['purchasing_power_index','safety_index','property_price_to_income_ratio','traffic_commute_time_index','pollution_index','climate_index' ]
# for col in drop_cols:
#     df.pop(col)
# print(df)