import csv
import json

from modules.User.user import User
from modules.database.transferData import TransferData


class MasterData:
    __instance = None
    users = {}
    dc_index = {}
    tickets = {}

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MasterData.__instance is None:
            MasterData()
        return MasterData.__instance

    def __init__(self):
        if MasterData.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MasterData.__instance = self
            t = TransferData()
            t.downloadFile('data.json')
            t.downloadFile('index.json')
            with open('files/data.json', 'r') as fp:
                aux = json.load(fp)
                self.users = {key: User().decode(value) for key, value in aux.items()}
            with open('files/index.json', 'r') as fp:
                aux = json.load(fp)
                self.dc_index = {int(key): value for key, value in aux.items()}
            with open('files/file.csv', 'r') as f:
                reader = iter(csv.reader(f))
                next(reader)
                for row in reader:
                    if row[3] not in self.users:
                        self.users[row[3]] = User(name=row[1], last_name=row[2], email=row[3], has_team=row[7] == 'Yes',
                                                  team=row[8])

    def save_data(self):
        with open('files/data.json', 'w') as fp:
            aux = {key: val.__dict__ for key, val in self.users.items()}
            json.dump(aux, fp)
        with open('files/index.json', 'w') as fp:
            json.dump(self.dc_index, fp)
        t = TransferData()
        t.uploadFile('data.json')
        t.uploadFile('index.json')

    def get_user_email(self, email):
        if email in self.users:
            return self.users[email]
        return None

    def get_user_dc(self, dc_id):
        if dc_id in self.dc_index:
            return self.users[self.dc_index[dc_id]]
        return None

    def get_logged_emails(self):
        result = ""
        for value in self.dc_index.values():
            user = self.users[value]
            if user.is_fib():
                result += ("%s -> %s \n" % (user.email, user.email_uni))
            else:
                result += ("%s \n" % user.email)
        return result

    # Pre: user.email in self.users
    def login(self, dc_id, user):
        user.login(dc_id)
        self.dc_index[dc_id] = user.email
