# 一个密码本，每一页有一个密码
# 所有密码都是 26 位小写字母组成
# 每一个密码都不同，找出满足下面条件的最长的密码
# 从它的末尾开始去掉一位，得到新密码也在密码本中
# 多个满足条件的密码，输出字典序最大的那个

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