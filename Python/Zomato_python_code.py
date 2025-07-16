import pandas as pd
df1= pd.read_csv("zomato.csv")
df2=df1.drop(columns=['url','phone','rest_type','dish_liked','reviews_list','menu_item','listed_in(city)'] , axis=1)
df3=df2.rename(columns={'approx_cost(for two people)':'two_people_cost','listed_in(type)':'type_of_restaurant'})
df4=df3.rename(columns={'rate':'rating'})
df4=df4.dropna(subset=['location'])
df4=df4.dropna(subset=['cuisines','two_people_cost'])
df4['two_people_cost']=df4['two_people_cost'].str.replace(',', '').astype(int)
df4['two_people_cost']=df4['two_people_cost']/2
df4=df4.rename(columns={'two_people_cost':'cost_per_person'})
df4.isna().sum()
def handlerate(x):
    try:
        return float(x.split('/')[0])
    except:
        return None
df4['rating'] = df4['rating'].apply(handlerate)
df4['rating'] = df4['rating'].fillna(df4['rating'].mean)
df4.to_csv('zomato_cleaned_data_analysis.csv')