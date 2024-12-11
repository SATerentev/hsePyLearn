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
        elif sex == "sex":
            print("pizdec chel...")
        else:
            raise IOError("Invalid input")
    
    def get_information(self):
        return "Пользователь {} {}, {} лет совершил(а) покупку на {} у.е. с устройства \"{}\", браузера {}. Регион, из которого совершалась покупка: {}.".format(self.name, self.sex, self.age, self.bill, self.device_type, self.browser, self.region)

    
clients = []

with open("web_clients_correct.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for str in reader:
        clients.append(Client(str[0], str[1], str[2], str[3], str[4], str[5], str[6]))

test = Client("Simon", "mobile", "ChromeForAndroid", "male", 22, 10, "Russia")
#print(test.get_information())
print(clients[1].get_information())
