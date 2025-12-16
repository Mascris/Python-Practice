import bcrypt

raw_password = "mopo123"

hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

print(f"stored in db: {hashed_password}")

login_attempt = input("enter password: ")

is_correct = bcrypt.checkpw(login_attempt.encode('utf-8'), hashed_password)

if is_correct:
    print("access granted")
else:
    print("access denied")
