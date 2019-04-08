# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)

data.rename(columns={'Total': 'Total_Medals'}, inplace=True)
data.head(10) 
#Code starts here



# --------------
#Code starts here

data["Better_Event"] = np.where(data["Total_Summer"]==data["Total_Winter"],"Both",(np.where(data["Total_Summer"]>data["Total_Winter"],"Summer","Winter")))
better_event = data["Better_Event"].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries = top_countries.iloc[0:len(top_countries)-1]

def top_ten(df, col_name):
    country_list=[]
    top_ten = df.nlargest(10,col_name)
    country_list = list(top_ten['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
print("Top 10 Summer : ",top_10_summer)
top_10_winter = top_ten(top_countries,'Total_Winter')
print("Top 10 Winter : ",top_10_winter)
top_10 = top_ten(top_countries,'Total_Medals')
print("Top 10 : ",top_10)

common = []
for i in range(0,10):
    if (top_10_summer[i] in top_10_winter) and (top_10_summer[i] in top_10):
        common.append(top_10_summer[i])

print("Common in all 3 : ",common)
    



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot.bar('Country_Name','Total_Summer')
winter_df.plot.bar('Country_Name','Total_Winter')
top_df.plot.bar('Country_Name','Total_Medals')


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = (summer_df['Golden_Ratio']).max()
summer_country_gold = list(summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'])[0]
print(summer_max_ratio)
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = (winter_df['Golden_Ratio']).max()
winter_country_gold = list(winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'])[0]
print(winter_max_ratio)
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = (top_df['Golden_Ratio']).max()
top_country_gold = list(top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'])[0]

print(top_max_ratio)
print(top_country_gold)


# --------------
#Code starts here
data_1 = data.iloc[0:len(data)-1]
data_1['Total_Points'] = (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']*1)

most_points = data_1['Total_Points'].max()

best_country = list(data_1[data_1['Total_Points']==most_points]['Country_Name'])[0]

print(most_points)
print(best_country)


# --------------
#Code starts here

best = data[data['Country_Name']==best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)

plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


