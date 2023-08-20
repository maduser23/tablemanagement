import pickle

def create_user(username, email, password):
    try:
        # Load existing user data from the binary file
        with open("user_data.bin", "rb") as file:
            users = pickle.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty dictionary
        users = {}

    # Check if the username already exists
    if username in users:
        return "Username already exists"

    # Add the user data to the dictionary
    users[username] = [password, email]

    # Save the updated user data to the binary file
    with open("user_data.bin", "wb") as file:
        pickle.dump(users, file)

    return "User created successfully"

