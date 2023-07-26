import csv
import datetime

class read_fileCSV:
    def __init__(self, file):
        self.__users = file
        self.__users_dict = {}

    def open_fileCSV(self):
        with open(self.__users, "r") as users_file:
            csvRead = csv.reader(users_file, delimiter=",")
            for row in csvRead:
                date = 2
                userENTRY = 3
                rating = 4
                listENTRY = [row[1]]

                for entry in range(int((len(row) - 2) / 3)):
                    listENTRY.append(row[date])
                    listENTRY.append(row[userENTRY])
                    listENTRY.append(row[rating])
                    date += 3
                    userENTRY += 3
                    rating += 3
                self.__users_dict[row[0]] = listENTRY

        users_file.close()
        return self.__users_dict



class SIGNUPCSV:
    def __init__(self, file, user_dict, username, password):
        self.__users = file
        self.__users_dict = user_dict
        self.__username = username
        self.__password = password

    def signup_validation(self):
        existing = False
        for k, v in self.__users_dict.items():
            if self.__username == k:
                existing = True
        return existing

    def signup_adding_record(self):
        with open("users.csv", "w", newline="") as users_file:
            add_file = csv.writer(users_file)
            self.__users_dict[self.__username] = self.__password
            for k, v in self.__users_dict.items():
                newUser = []
                newUser.append(k)
                if type(v) is not str:
                    for i in v:
                        newUser.append(i)
                else:
                    newUser.append(v)
                add_file.writerow(newUser)

        users_file.close()



class LOGINCSV:
    def __init__(self, file, user_dict, username, password):
        self.__users = file
        self.__users_dict = user_dict
        self.__username = username
        self.__password = password

    def signup_validation1(self):
        existing = False
        for k, v in self.__users_dict.items():
            if self.__username == k:
                if self.__password == v[0]:
                    existing = True
        return existing



class journalENTRY:
    def __init__(self, file, user_dict, username, entry, rating):
        self.__users = file
        self.__users_dict = user_dict
        self.__username = username
        self.__entry = entry
        self.__rating = rating

    def journal_save(self):
        with open("users.csv", "w", newline="") as users_file:
            add_file = csv.writer(users_file)
            for k, v in self.__users_dict.items():
                newUser = []
                newUser.append(k)
                if type(v) is not str:
                    for i in v:
                        newUser.append(i)
                else:
                    newUser.append(v)

                if k == self.__username:
                    tday = datetime.date.today()
                    date = tday.strftime("%Y-%m-%d")
                    if date not in newUser:
                        newUser.append(tday)
                        newUser.append(self.__entry)
                        newUser.append(self.__rating)
                    else:
                        index = newUser.index(date)
                        newUser[index + 1] = self.__entry
                        newUser[index + 2] = self.__rating
                add_file.writerow(newUser)



class journalSEARCH:
    def __init__(self, user_dict, username, date):
        self.__users_dict = user_dict
        self.__username = username
        self.__date = date

        self.entry = ""
        self.rating = ""

    def journal_search(self):
        for k, v in self.__users_dict.items():
            if k == self.__username:
                index = v.index(self.__date)
                self.entry = v[index + 1]
                self.rating = v[index + 2]

        return self.entry, self.rating