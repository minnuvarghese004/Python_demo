class Login:
    username="admin"
    password="pwd123"

    def usrCheck(self):
        print("Valid username")

    def loginCheck(self,name):
        self.name=name
        print(f"{name} logged in successfully")

    def detail(self):
        print(f"{self.name} logged in successfully with valid username")



login1=Login()
print(login1.username)
login2=Login()
print(login2.password)

login1.email="xyz@gmail.com"
print(login1.email)
login1.usrCheck()
login2.usrCheck()

login1.loginCheck("Minnu")
login1.detail()







