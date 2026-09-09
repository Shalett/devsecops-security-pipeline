import subprocess


def run_command(user_input):
    subprocess.call(user_input, shell=True)


password = "SuperSecretPassword123"


def get_user(user):
    query = "SELECT * FROM users WHERE name = '" + user + "'"
    print(query)