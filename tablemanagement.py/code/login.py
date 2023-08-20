import pickle

def check_user(username, password):
    try:
        # Load user data from the binary file
        with open("user_data.bin", "rb") as file:
            users = pickle.load(file)
            print(users)
    except FileNotFoundError:
        return "User does not exist"

    if username not in users:
        return "User does not exist"

    stored_password = users[username][0]
    print(stored_password)
    if password == stored_password:
        return True
    else:
        return False

