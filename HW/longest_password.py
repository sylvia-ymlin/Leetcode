# A password book, each page has a password
# All passwords consist of 26 lowercase letters
# Each password is different. Find longest password satisfying condition:
# Removing one char from its end results in a new password that is also in the book
# If multiple satisfying passwords exist, output the one with largest lexicographical order

passwords = map(str, input().split())

password_set = set(passwords)

max_password = ""

for password in password_set:
    current_password = password
    valid = True

    while len(current_password) > 0:
        if current_password not in password_set:
            valid = False
            break
        current_password = current_password[:-1]

    if valid:
        if (len(password) > len(max_password)) or (len(password) == len(max_password) and password > max_password):
            max_password = password

print(max_password)