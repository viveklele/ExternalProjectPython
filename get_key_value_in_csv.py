import csv
reader = csv.DictReader(open("csv_file.csv"))

# Here, In (csv_file.csv) enter your file name, if the file is not present in the working directory, 
# Then give the full path of the file.						

user_input = input("Enter number: ")
for i in reader:
	if user_input in i['number']:
		print("name = ", i['name'])
		print("id = ", i['id']) 
		
