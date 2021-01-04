from get_enviroment import UNIVERSITY_EMAIL


class User:
    dc_id = -1
    name = ""
    last_name = ""
    email = ""
    email_uni = ""
    has_team = False
    team = ""

    def __init__(self, name="", last_name="", email="", has_team="", team=""):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.has_team = has_team
        self.team = ""
        self.email_uni = ""
        self.dc_id = -1
        if self.has_team:
            self.team = team
        if UNIVERSITY_EMAIL in self.email:
            self.email_uni = self.email

    def decode(self, dict):
        self.name = dict["name"]
        self.last_name = dict["last_name"]
        self.email = dict["email"]
        self.has_team = dict["has_team"]
        self.team = dict["team"]
        self.email_uni = dict["email_uni"]
        self.dc_id = dict["dc_id"]
        return self

    def login(self, dc_id):
        self.dc_id = dc_id

    def is_fib(self):
        return self.email_uni != ""

    def add_fib_mail(self, email_uni):
        self.email_uni = email_uni

    def is_logged(self):
        return self.dc_id != -1

    def add_team(self, team):
        self.team = team
        self.has_team = True

    def leave_team(self):
        self.team = ""
        self.has_team = False
