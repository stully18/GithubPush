import requests

list_names = []
try:
	for i in range(1,2000):
		url = "https://api-football-v1.p.rapidapi.com/v3/players"
		querystring = {"id":f"{i}","season":"2022"}
		headers = {
			"X-RapidAPI-Key": "0142ab06f3mshf4e17c5911c470cp158874jsn7081aebc27a9",
			"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
		}
		response = requests.get(url, headers=headers, params=querystring)
		ans = response.json()
		response = (ans['response'])
		name = response[0]
		name2 = name['player']
		real_name = name2['name']
		print(real_name)
except IndexError:
	pass
