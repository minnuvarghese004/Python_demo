#write a function to count vowels in a string
# def count_vowels(word):
#      count=0
#      vowels = "AEIOUaeiou"
#      for i in word:
#          if i in vowels:
#              count=count+1
#      print(count)
#
# word = input("Enter the word:")
# count_vowels(word)

#method 2
# def count_vowels(word):
#     count = 0
#     vowels = "aeiou"
#     for i in word:
#         if i.lower() in vowels:
#             count = count + 1
#     print(count)
#
#
# word = input("Enter the word:")
# count_vowels(word)

# create a function to check whether a test case has passed or failed
output_text1="12 tests passed"
output_text2="10 passed and 2 failed"
# def check_test_status(status):
#     if "failed" in status:
#         print("Tests are not completely passed,some are failed.please try again")
#     else:
#         print("All passed")
# check_test_status(output_text1)
# check_test_status(output_text1)
# # create a function to check whether a username is valid [length more than 5]
# username=input("Enter the username: ")
# def user_check(user):
#     if len(user)>5:
#         return True
#     else:
#         return False
# print(user_check(username))

# create a function to validate an email address
#can include characters,digits,.,com/in,gmail,@,Always starts with a character

email=input("Enter the email")
def email_check(email):
    first_character= email[0]
    if (type(first_character)!=int) and "@" in email and "gmail" in email or ".in" in email or ".com" in email:
        print(f"email is valid")
    else:
        print("email is invalid")
(email_check(email))

#method 2
# email=input("Enter the email: ")
# def email_check(email):
#     firstchar= email[0]
#     check=type(firstchar)
#     print(check.isdigit())
#     # if (not firstchar.isdigit()) and "@" in email and "gmail" in email or ".in" in email or ".com" in email:
#     #     print(f"email is valid")
#     # else:
#     #     print("email is invalid")
# email_check(email)


# create a function to convert a browser name into lowercase
# browser_name=input("Enter browser name: ")
# def name_lower(browser_name):
#     print(browser_name.lower())
# name_lower(browser_name)

#In case of strict check, Always use "=="
#In case of return statement, check all conditions are fullfilled in prior
#Always use return statement when we want to store the output
#execution continues - print
#execution exit - return

