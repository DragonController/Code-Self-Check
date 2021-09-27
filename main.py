# Author: Grace Fowler
# This program prints out two lists of F1 drivers sorted by the last names of the drivers and the drivers' numbers respectively

# List of driver names, driver numbers, and sponsors
# "  YEET!" is added to the end of Lewis Hamilton's string
drivers = ["Max Verstappen 33 Red Bull", "Lewis Hamilton 44 Mercedes YEET!", "Valtteri Bottas 77 Mercedes",
           "Lando Norris 4 McLaren", "Sergio Perez 11 Red Bull", "Charles Leclerc 16 Ferrari",
           "Carlos Sainz 55 Ferrari", "Daniel Ricciardo 3 McLaren", "Pierre Gasly 10 AlphaTauri",
           "Fernando Alonso 14 Alpine", "Esteban Ocon 31 Alpine", "Esteban Ocon 31 Alpine",
           "Lance Stroll 18 Aston Martin", "Yuki Sonoda 22 AlphaTauri", "George Russell 63 Williams",
           "Nicholas Latifi 6 Williams", "Kimi Raikkonen 7 Alfa Romeo", "Antonio Giovinazzi 99 Alfa Romeo",
           "Mick Schumacher 47 Haas", "Nikita Mazepin 9 Haas"]

# Prints the header
print("2021 F1 Drivers")
print("===============")
print()

# Prints the list sorted in alphabetical order by the drivers' last names
drivers = sorted(drivers, key=lambda x: x.split(" ")[1])
for i in range(len(drivers)):
    print(drivers[i])
print()

# Prints the list sorted in order of the drivers' numbers
drivers = sorted(drivers, key=lambda x: int(x.split(" ")[2]))
print()
for i in range(len(drivers)):
    print(drivers[i])
