from server.models import Address, City, Passager, Passager_trip, Province, Trip, User, Driver, VehicleDriver, Vehicle

class Database:
    users = [
        User(1, "Juan", "Pérez", "password123", "juan.perez@example.com", "juanperez", "2023-01-02", True),
        User(2, "María", "López", "maria123", "maria.lopez@example.com", "marialopez", "2023-10-17", False),
        User(3, "Carlos", "García", "carlos123", "carlos.garcia@example.com", "carlosgarcia", "2023-01-12", True),
        User(4, "Ana", "Martínez", "ana456", "ana.martinez@example.com", "anamartinez", "2023-04-01", False),
        User(5, "Luis", "Rodríguez", "luis789", "luis.rodriguez@example.com", "luisrodriguez", "2023-01-01", True),
        User(6, "Sofía", "Fernández", "sofia123", "sofia.fernandez@example.com", "sofiafernandez", "2023-06-01", True),
        User(7, "Pedro", "Gómez", "pedro987", "pedro.gomez@example.com", "pedrogomez", "2023-09-01", False),
        User(8, "Laura", "Díaz", "laura654", "laura.diaz@example.com", "lauradiaz", "2023-05-01", True),
        User(10, "Lucía", "Ramírez", "lucia321", "lucia.ramirez@example.com", "luciaramirez", "2023-02-14", False)
    ]
    drivers= [
        Driver(1, 5),
        Driver(2, 6),
        Driver(3, 8)
    ]
    passagers = [
        Passager(1, 1),
        Passager(2, 2),
        Passager(3, 3),
        Passager(4, 4),
        Passager(5, 5),
        Passager(6, 8),
        Passager(7, 10)
    ]
    province = [
        Province(1,'Buenos Aires')
    ]
    cities = [
        City(1, 'La Plata', 1), 
        City(2, 'Chascomús', 1)
    ]
    addresses = [
        Address(1, 'Calle 58', 607, 1),
        Address(2, 'Calle 3', 712, 2),
        Address(3, 'Av. 32', 1123, 1)
    ]
    vehicles= [
        Vehicle(1,"ABC-123", "Ford", "Fiesta", "Rojo", 2019),
    ]
    trips = [
        Trip(1, "2023-01-01", "08:00", 3, 500.0, 1, "2023-01-02", 2, 1),
    ]
    vehicle_drivers = [
        VehicleDriver(1, 2, 1)
    ]
    passager_trips = [
        Passager_trip(1, 1, 1),
        Passager_trip(2, 1, 2),
        Passager_trip(3, 2, 3),
        Passager_trip(4, 2, 4),
        Passager_trip(5, 3, 5),
        Passager_trip(6, 3, 6),
        Passager_trip(7, 3, 7)
    ]
