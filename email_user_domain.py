email = str(input('Enter Your Email: ')).strip()

user = email[:email.index('@')]
domaimn = email[email.index('@')+1:]

print(' user: {}\n domain: {}'.format(user, email))