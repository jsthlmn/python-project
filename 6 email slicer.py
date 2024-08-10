def main():
    print("Welcome to email slicer")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extention) = domain.split(".")

    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension :", extention)

while True:
    main()