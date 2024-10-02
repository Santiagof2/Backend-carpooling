from server.models import User, Address, City, Province, Driver, Vehicle, VehicleDriver

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
        Vehicle(1, 'AB 123 CD', 'Nissan', 'Kicks')
    ]
    drivers: list[Driver] = [
        Driver(9, "Diego", "Torres", "diego321", "diego.torres@example.com", "diegotorres", "2023-09-01", True)
    ]
    vehicle_drivers = [
        VehicleDriver(1, 2, 1)
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
    passagers = [
        Passager(1, 1),
        Passager(2, 2),
        Passager(3, 3),
        Passager(4, 4),
        Passager(5, 5),
        Passager(6, 8),
        Passager(7, 10)
    ]
    trips = [
        Trip(1, "2023-01-01", "08:00", 3, 500.0, 1, "2023-01-02", 2, 1),
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

    @classmethod
    def get_address(cls, id: int) -> Address:
        for address in cls.addresses:
            if address.get_id() == id:
                return address
    
    @classmethod
    def get_vehicle_driver(cls, id: int) -> VehicleDriver:
        for vehicle_driver in cls.vehicle_drivers:
            if vehicle_driver.get_id() == id:
                return vehicle_driver
