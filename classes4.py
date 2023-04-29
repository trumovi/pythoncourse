class Ticket:
    def __init__(self, station, place, price, time):
        self.departure = station.loc
        self.place = place
        self.price = price
        self.time = time


class Passenger:
    def __init__(self, name, station, money):
        self.name = name
        self.station = station
        self.money = money


class Station:
    def __init__(self, location):
        self.loc = location

    def sell(self, passenger, ticket):
        if passenger.money >= ticket.price:
            print(f"{passenger.name} has bought a ticket from {self.loc} to {ticket.place} for {ticket.price} at {ticket.time}.")
            passenger.money -= ticket.price
            print(f"{passenger.name} now has {passenger.money} left.")
            passenger.station = ticket.place
            print(f"{passenger.name} is at {passenger.station}")
        else:
            print(f"{passenger.name} doesn't have enough money to buy this ticket :(")
            print("\n_______________\n")

omsk = Station("Омск")
omsk_novosib = Ticket(omsk, "Новосибирск", 2217, "02:46")
omsk_kemerovo = Ticket(omsk, "Кемерово", 1546, "14:23")
omsk_tomsk = Ticket(omsk, "Томск", 1768, "12:58")

novosibirsk = Station("Новосибирск")
novosib_omsk = Ticket(novosibirsk, "Омск", 2217, "12:45")
novosib_vlad = Ticket(novosibirsk, "Владивосток", 4926, "13:34")
novosib_hab = Ticket(novosibirsk, "Хабаровск", 6239, "18:06")

person_1 = Passenger("Anya", "Омск", 4000)

omsk.sell(person_1, omsk_novosib)
novosibirsk.sell(person_1, novosib_hab)