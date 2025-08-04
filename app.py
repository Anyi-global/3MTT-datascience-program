import requests
url = 'https://raw.githubusercontent.com/AlexTheAnalyst/PandasYouTubeSeries/refs/heads/main/countries%20of%20the%20world.csv'
res = requests.get(url, allow_redirects=True)
with open('countries_of_the_world.csv','wb') as file:
    file.write(res.content)
file.close()