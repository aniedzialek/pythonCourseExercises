emails = ['abc@gmail.com','def@yahoo.com','ghi@gmail.com']

for email in emails:
    if 'gmail' in email:
        print(email)
    else:
        print('No gmail')

# --------------------------------

password = ''
expectedPassword = 'python123'

while password != expectedPassword:
    password = input("Please enter password: ")
    if password == expectedPassword:
        print('You are logged in!')
    else:
        print('Sorry, try again')

# --------------------------------
# Multiple lists
names = ['Tim', 'Jerry', 'Elvis']
email_domains = ['gmail', 'hotmail', 'yahoo']

for i,j in zip(names, email_domains):
    print(i,j)
