import secrets

def generate_secret_token():
    return secrets.token_hex(16)


if __name__ in "__main__":
    print(generate_secret_token())