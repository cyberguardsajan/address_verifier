import re

print("""

  ___      _     _                                    _  __ _           
 / _ \    | |   | |                                  (_)/ _(_)          
/ /_\ \ __| | __| |_ __ ___  ___ ___  __   _____ _ __ _| |_ _  ___ _ __ 
|  _  |/ _` |/ _` | '__/ _ \/ __/ __| \ \ / / _ \ '__| |  _| |/ _ \ '__|
| | | | (_| | (_| | | |  __/\__ \__ \  \ V /  __/ |  | | | | |  __/ |   
\_| |_/\__,_|\__,_|_|  \___||___/___/   \_/ \___|_|  |_|_| |_|\___|_|   
                                                                        
                                                                        

""")

def validate_email(email):
    # Define a regex pattern for validating an email address
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use the match function to check if the email fits the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False


email = input("Enter an email address to verify: ")

if validate_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is an invalid email address.")
