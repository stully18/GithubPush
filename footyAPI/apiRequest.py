import requests

id = 342

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"id":f"{str(id)}","season":"2020"}

headers = {
	"x-rapidapi-key": "0142ab06f3mshf4e17c5911c470cp158874jsn7081aebc27a9",
	"x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())