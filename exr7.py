import csv

class Client:
    def __init__(self, name, device_type, browser, sex, age, bill, region):
        self.name = name
        self.device_type = device_type
        self.browser = browser
        self.age = age
        self.bill = bill
        self.region = region

        if sex == "female":
            self.sex = "женского пола"
        elif sex == "male":
            self.sex = "мужского пола"
        else:
            raise IOError("Invalid input")
    
    def get_information(self):
        return "Пользователь {} {}, {} лет совершил(а) покупку на {} у.е. с устройства \"{}\", браузера {}. Регион, из которого совершалась покупка: {}.".format(self.name, self.sex, self.age, self.bill, self.device_type, self.browser, self.region)

    

test = Client("Simon", "mobile", "ChromeForAndroid", "male", 22, 10, "Russia")
print(test.get_information())