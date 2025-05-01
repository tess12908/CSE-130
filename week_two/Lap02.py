# 1. Name:
#      Tess Hollinger
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program is made to read a Json file full of passwords and user names and turn it into a new object to be indexed
# 4. What was the hardest part? Be as specific as possible.
#     Thee hardest part about this assignment was making the for loop. I have found that for loops are confusing for me. 
# 5. How long did it take for you to complete the assignment?
#      To complete this, it took me 30 minutes to program it, 15 to film it and 5 to submit. So all in all it took less then 1 hour


import json 

with open('Lab02.json', 'rt') as filehandle: 
    json_data = filehandle.read() # reads the file in one line 
    dictionary_data = json.loads(json_data) # converts into a json object

saved_username = dictionary_data['username'] # saves usernames as var 
saved_password = dictionary_data['password'] # saves passwords as var 


entered_user = input("Username: ") # user entered username 
entered_password = input("Password: ") # user entered password 

# find the index and check if they match
authenticated = False
for i in range(len(saved_username)):
    if saved_username[i] == entered_user and saved_password[i] == entered_password:
        authenticated = True

# Check result 
if authenticated:
    print("Authentication successful!")
else:
    print("Authentication failed.")
