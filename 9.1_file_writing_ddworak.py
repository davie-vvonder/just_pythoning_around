'''This program is designed to confirm the
existence of a directory, save a file with 
basic info to that directory, and display 
the information all based on user input'''
# Dave Dworak - owner/developer
# Developed on 8/3/2022
# CIS245-T304

# import os to verify directory/file existence
import os

# Define colors class
class Colors():
	Cyan = '\033[36m'
	Red = '\33[31m'
	Yellow = '\33[33m'
	Reset = '\33[0m'

# Define functions
def quit():
	'''To quit the program at user input'''
	print(f'\nThank you for stopping by!')
	print()

# Display welcome
print(f'\nLooking to save some stuff? You came to the right place!')

# Start loop with termination options
while True:
	print(f'\nEnter "q" to quit at any time')
	directory = input(f'\nEnter the directory: ')
	if directory == "q":
		quit()
		break
	elif os.path.isdir(directory): # Check for directory existence - required
		pass
	else:
		print(f'\n{Colors.Yellow}That is not a valid directory. Try again.' + Colors.Reset)
		continue
	file_name = input(f'\nEnter the file name: ')
	if file_name == "q":
		quit()
		break
	elif os.path.isfile(f'{directory}/{file_name}'): # Check for file existence - create new if none, or verify ok to OVERWRITE
		print(f'\n{Colors.Yellow}That file already exists.' + Colors.Reset)
		print(f'\nContinuing will {Colors.Red}OVERWRITE{Colors.Reset} all data in the file.')
		overwrite = input(f'\n\tWould you like to {Colors.Red}overwrite?{Colors.Reset} (y/n): ')
		if overwrite == "n":
			print(f'\nOk, we wont overwrite. Try a different file name')
			continue
		elif overwrite == "q":
			quit()
			break
		else:
			pass
	else:
		pass
	complete_path = f'{directory}/{file_name}' # Assign full file path to variable
	
	# Collect remaining user input to save to file
	name = input(f'\nEnter your name: ')
	if name == "q":
		quit()
		break
	address = input(f'\nEnter your address: ')
	if address == "q":
		quit()
		break
	phone = input(f'\nEnter your phone number: ')
	if phone == "q":
		quit()
		break
	
	# Open/create file, write to it, display it for validation
	with open(complete_path, 'w') as write_new:
		write_new.write(f'\n{name}, {address}, {phone}')
	with open(complete_path, 'r') as write_new:
		display_entries = write_new.read()
		print(f'\nWe have saved the following information in {complete_path}:')
		print(f'\n\tSaved: {Colors.Cyan}{display_entries.strip()}', Colors.Reset)

