#!/bin/bash python

import json

with open('./data/schacon.repos.json', 'r') as file:
	data = json.load(file)

output_array = []

with open('chiacon.csv', 'w') as csv_chia: #makes a new file named chiacon.csv but ehich we refer to while coding as csv_chia

	for entry in data[:5]:
		name = entry['name']
		output_array.append(name)
		html_url = entry['html_url']
		output_array.append(html_url)
		updated_at = entry['updated_at']
		output_array.append(updated_at)
		visibility = entry['visibility']
		output_array.append(visibility)

		one_line = f"{name},{html_url},{updated_at},{visibility}\n" #write in one string, with a new line after each

		
		csv_chia.write(one_line) #this writes to the text file we created


