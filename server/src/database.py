from server.models import *
class Database:
    users: list[User] = [
        User(1, "Juan", "Pérez", "password123", "juan.perez@example.com", "juanperez", "2023-01-01", True),
        User(2, "María", "López", "maria123", "maria.lopez@example.com", "marialopez", "2023-02-01", False),
        User(3, "Carlos", "García", "carlos123", "carlos.garcia@example.com", "carlosgarcia", "2023-03-15", True),
        User(4, "Ana", "Martínez", "ana456", "ana.martinez@example.com", "anamartinez", "2023-04-10", False),
        User(5, "Luis", "Rodríguez", "luis789", "luis.rodriguez@example.com", "luisrodriguez", "2023-05-05", True),
        User(6, "Sofía", "Fernández", "sofia123", "sofia.fernandez@example.com", "sofiafernandez", "2023-06-20", True),
        User(7, "Pedro", "Gómez", "pedro987", "pedro.gomez@example.com", "pedrogomez", "2023-07-07", False),
        User(8, "Laura", "Díaz", "laura654", "laura.diaz@example.com", "lauradiaz", "2023-08-15", True),
        User(10, "Lucía", "Ramírez", "lucia321", "lucia.ramirez@example.com", "luciaramirez", "2023-09-20", False)
    ]
    vehicles = [
        Vehicle(1, 'AB 123 CD', 'Nissan', 'Kicks', 'Blanco', '2020')
    ]
    drivers: list[Driver] = [
        Driver(1, users[5]),
        Driver(2, users[6]),
        Driver(3, users[7]),
        Driver(4, users[8]),
    ]
    vehicle_drivers = [
        VehicleDriver(1, drivers[0], vehicles[0])
    ]
    province: list[Province] = [
        Province(1, 'Buenos Aires')
    ]
    cities: list[City] = [
        City(1, 'La Plata', province[0]), 
        City(1, 'Chascomús', province[0])
    ]
    addresses: list[Address] = [
        Address(1, 'Calle 58', 607, cities[0]),
        Address(1, 'Calle 3', 712, cities[0]),
        Address(1, 'Av. 32', 1123, cities[0])
    ]
    vehicle_drivers: list[VehicleDriver] = [
        VehicleDriver(1, drivers[0], vehicles[0])
    ]
    Passengers = [
        Passenger(1, users[0]),
        Passenger(2, users[1]),
        Passenger(3, users[2]),
        Passenger(4, users[3]),
        Passenger(5, users[4]),
        Passenger(6, users[7]),
        Passenger(7, users[8])
    ]
    trips = [
        Trip(1, 1, "2023-01-01", "08:00", 3, 500.0, 25692, addresses[1], addresses[0], vehicle_drivers[0]),
        Trip(2, 1, "2023-04-06", "19:30", 3, 500.0, 245, addresses[1], addresses[0], vehicle_drivers[0]),
    ]
    PassengerTrips = [
        PassengerTrip(1, Passengers[0], trips[0]),
        PassengerTrip(2, Passengers[1], trips[0]),
        PassengerTrip(3, Passengers[2], trips[0]),
        PassengerTrip(4, Passengers[3], trips[0]),
        PassengerTrip(5, Passengers[4], trips[0]),
        PassengerTrip(6, Passengers[5], trips[0]),
        PassengerTrip(7, Passengers[6], trips[0])
    ]
