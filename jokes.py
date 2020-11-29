import requests
from random import randint
from pyfiglet import figlet_format
from termcolor import colored 

url = "https://icanhazdadjoke.com/search"
header = figlet_format("DAD JOKES 3000!")
header = colored(header, color = "red")
print(header)

topic = input("Let me tell you a joke! Give me a topic: ")
response = requests.get(
	url, 
	headers = {"Accept": "application/json"},
	params = {"term":topic}
).json()

number_of_jokes = len(response["results"])
if number_of_jokes > 1:
	print(f"I've got {number_of_jokes} joke/s about {topic}. Here's one: ")
	print(response["results"][randint(0, number_of_jokes)]["joke"])
elif number_of_jokes == 1:
	print("There is just one joke: ")
	print(response["results"][randint(0, number_of_jokes)]["joke"])
else:
	print(f"Sorry, there are no jokes with your term {topic}")
