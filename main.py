import subprocess

def check_email(email):
    result = subprocess.run(["holehe", email], capture_output=True, text=True)

    return result.stdout

email = input("Enter your email: ")
response = check_email(email)
print(response)