class Streaming:
    def __init__(self, name, films):
        self.name = name
        self.films = films.split(', ')

    def watch(self, user, film):
        self.films.remove(film)
        user.films.append(film)
        print(f"{user.login} watched \"{film}\" on {self.name}")
        print(f"These films are also available in \"{self.name}\": {self.films}.")


class User:
    def __init__(self, login):
        self.login = login
        self.films = []



user1 = User("Olga")
streaming1 = Streaming("Kinopoisk", "Everything Everywhere All at Once, La La Land, Vice")
streaming2 = Streaming("Okko", "Fight Club, Triangle of Sadness")

streaming2.watch(user1, "Fight Club")
streaming2.watch(user1, "Triangle of Sadness")