# email = "a@gmail.uk"
name = "G1Gy"
password = "rasd"
top_level_domain = ['.org', '.net', '.edu', '.ac', '.uk', '.com']
# def validate_name(name):
#     if not isinstance(name, str) or len(name) <= 2:
#         raise ValueError("Enter valid name address")
#     if not name[0].isalpha():
#         raise ValueError("Enter an alphabetic character")
#     else:
#         return True  #complete
# i = len(email)
# print(email[(i - 4):])
# def validate_email(email):
#     if '@' not in email or not email[0].isalpha() :
#         raise ValueError("Email must start with an alphabetic character and contain \"@\" ")
#     if not any(email.endswith(tld) for tld in top_level_domain) not in top_level_domain:
#         raise ValueError("Enter valid email domain1")
#     prefix = email.split("@")[0]
#     if prefix <= 2:
#         raise ValueError("Enter a valid email address")
#
# validate_email(email) # complete


# def validate_password(password):
#     if not isinstance(password, str):
#         raise ValueError("Password isn't a string.")
#     if not any(char.isupper() for char in password):
#         raise ValueError("Password doesn't contain an uppercase character.")
#
# validate_password(password)
# def validate_email(email):
#     if email.loc["@"]
#
# validate_email(email)
# email = "adadasd@gmail.com"
# def validate_email(email):
#     if not isinstance(email, str) or  not "@" in email:
#         raise ValueError("Enter valid email")
#
#
# validate_email(email)

# # # Datacamp first trial version
# Start coding here
# Use as many cells as you need
top_level_domain = ['.org', '.net', '.edu', '.ac', '.uk', '.com']
def validate_name(name):
    if not isinstance(name, str) or len(name) <= 2:
        raise ValueError("Enter name with more than 2 character")
    return True

def validate_email(email):
    if not isinstance(email, str) or "@" not in email:
        raise ValueError("Enter valid email")
    if not any(email.endswith(tld) for tld in top_level_domain):
        raise ValueError("Enter valid email domain")
    email_prefix = email.split("@")[0]
    if len(email_prefix) <= 2:
        raise ValueError("Email username must be more than 2 alphabetic characters")
    return True

def validate_password(password):
    if len(password) <= 8 or not isinstance(password, str):
        raise ValueError("Password must be longer than 8 and saved in a string ")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase character")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one numeric digit")
    return True

def validate_user(name, email, password):
    validate_name(name)
    validate_email(email)
    validate_password(password)
    return True

def register_user(name, email, password):
    try:
        validate_user(name, email, password)
    except ValueError as e:
        print(e)
        return False
    user =  {"name": name, "email": email, "password": password}
    return user
# # # AI corrected validator
top_level_domain = ['.org', '.net', '.edu', '.ac', '.uk', '.com']

def validate_name(name):
    if isinstance(name, str) and len(name) > 2:
        return True
    return False

def validate_email(email):
    if not isinstance(email, str):
        return False
    if "@" not in email:
        return False
    if not any(email.endswith(tld) for tld in top_level_domain):
        return False
    email_prefix = email.split("@")[0]
    if len(email_prefix) <= 1:  # username must be >1
        return False
    return True

def validate_password(password):
    if not isinstance(password, str):
        return False
    if len(password) <= 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def validate_user(name, email, password):
    if not validate_name(name):
        raise ValueError("Invalid name")
    if not validate_email(email):
        raise ValueError("Invalid email")
    if not validate_password(password):
        raise ValueError("Invalid password")
    return True

def register_user(name, email, password):
    try:
        validate_user(name, email, password)
    except ValueError:
        return False
    return {"name": name, "email": email, "password": password}





# # kwargs = ""
# def concat(*key):
#     kwargs = ""
#     for words in key:
#         kwargs += " " + words
#     return kwargs
#
# sentence = concat("Learning", "With", "Chatgpt")
# print(sentence)

#Quite a mess right 😂😂😂, will clean up later when i build version 1.1