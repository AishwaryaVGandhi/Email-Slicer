def username(email):
    return email[:email.index("@")]


def domain(email):
    return email[email.index("@") + 1:]


print("Email Slicer !!\n")

email = input("Enter your Email Id : ").strip()
print("Username : ", username(email))
print("Domain : ", domain(email))
