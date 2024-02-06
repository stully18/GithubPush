import requests

def get_joke():
	url = "https://dad-jokes.p.rapidapi.com/random/joke"

	headers = {
		"X-RapidAPI-Key": "d400589733msh18a40305224910dp186204jsnc2c18369624a",
		"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)
	x = response.json()
	y = x['body']
	z = y[0]
	setup = z['setup']
	punchline = z['punchline']
	total_joke = f'{setup}\n{punchline}'
	return total_joke





