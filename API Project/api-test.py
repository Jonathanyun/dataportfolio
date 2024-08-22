import requests

url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

querystring = {"country":"England"}

headers = {
	"x-rapidapi-key": "e2c5d3e355msh1b52a14e097c335p1c48c3jsn1ad73c8994c4",
	"x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())