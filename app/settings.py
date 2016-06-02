class Settings():

    def __init__(self, username):
        self.username = username
        self.accesskey = None
        self.accesssecret = None
        self.consumerkey = None
        self.consumersecret = None

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)