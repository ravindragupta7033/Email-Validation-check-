#g@g.co
k, j, d = 0,0,0
email = input("Enter your email:")
# Email have more than 6 characters
if len(email) >= 6:
    # first character should be alphabatic
    if email[0].isalpha():
        # email have one '@' character
        if ('@' in email) and (email.count("@") == 1):
            # email have dot character from last to 2 or 3 position
            if (email[-4] == ".") ^ (email[-3] == "."):
                # check every character of email
                for i in email:
                    # email should not have space
                    if i == i.isspace():
                        k=1,
                    elif i.isalpha():
                        # Email should not have upper character
                        if i.upper():
                            j=1,
                            # Email have digit character
                    elif i.isdigit():

                        continue
                        # Email have some special character
                    elif i == "." or i =="_" or i == "@":
                        continue
                    else:
                        d=1,
                if k == 1 or j == 1 or d == 1:
                    print("Invalid Email5")
                else:
                    print("Email is correct 😂 ✉ 📧 📨 📩 ")
            else:
                print("Invalid Email4")
        else:
            print("Invalid Email3")

    else:
        print("Invalid Email2")
else:
    print("Invalid Email 1")