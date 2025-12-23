class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль изменён")
    def check_password(self, password):
        return self.__password == password
user = UserAccount("Jane01", "jane01@gmail.com", "qwerty")
print("Проверка пароля:", user.check_password("qwerty"))
user.set_password("ytrewq")
print("Проверка нового пароля:", user.check_password("ytrewq"))
print("Проверка старого пароля после смены:", user.check_password("qwerty"))