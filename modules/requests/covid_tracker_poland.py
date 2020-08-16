import requests
from datetime import date

API_URL_POLAND_DATA = ' https://coronavirus-19-api.herokuapp.com/countries/Poland'
API_URL_WORLD_DATA = 'https://coronavirus-19-api.herokuapp.com/countries'

response = requests.get(API_URL_POLAND_DATA)
response_world = requests.get(API_URL_WORLD_DATA)

def get_daily_stats(response):
    try:
        all_data_list = response.json()
        formatted_data = f'''
            COVID Poland DAILY STATS:
            AS of {date.today()}
            ******************************
            Total Confirmeed Cases : {all_data_list['cases']}
            Total Recovered Cases : {all_data_list['recovered']}
            Total Deaths Reported: {all_data_list['deaths']}
            Confirmed Cases Yesterday: {all_data_list['todayCases']}
            Deaths Reported Yesterday: {all_data_list['todayDeaths']}
            ******************************
        '''    
        print(formatted_data)
    except:
        print('An error occurred while processing data')

def get_top5_countries_with_active_cases(response):
    try:
        all_countries_data = response.json()
        for country in all_countries_data:
            if country['active'] is None:
                country['active'] = 0
        all_countries_data.sort(key=lambda x: x['todayCases'], reverse=True)
        top5_countries = all_countries_data[1:6]
        print('Top 5 countries with most cases today in the world:')
        for index, state in enumerate(top5_countries):
            formatted_data = f'''
            ********{index + 1}*************
            State: {state['country']}
            Today: {state['todayCases']}
            Active: {state['active']}
            Total Confirmed : {state['cases']} 
            ***************************
            '''
            print(formatted_data)
    except Exception as error:
        print(f'An error occured while processing data, {error}')

if __name__ == "__main__":
    #get_daily_stats(response)
    get_top5_countries_with_active_cases(response_world)