from Asperitas.users.user import User


class InMemoryUsersRepo:
    def __init__(self):
        self.next_id = 1
        self.by_id = {}

    def get_by_name(self, name):
        for _,value in self.by_id.items():
            if value.name == name:
                return value
        return None

    def request_create(self, username, password):
        found = self.get_by_name(username)
        if found is not None:
            return None #пользователь есть такой уже
        new_user = User(id=self.next_id, username=username, password=password)
        self.by_id[new_user.id] = new_user
        self.next_id += 1
        return new_user