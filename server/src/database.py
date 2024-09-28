class Database:
    users = [
        {'id': 1, 'first_name': 'Juan', 'last_first_name': 'Pérez', 'password': 'password123', 'email': 'juan.perez@example.com', 'username': 'juanperez', 'creation_date': '2023-01-01', 'email_validation': 1},
        {'id': 2, 'first_name': 'María', 'last_first_name': 'López', 'password': 'maria123', 'email': 'maria.lopez@example.com', 'username': 'marialopez', 'creation_date': '2023-02-01', 'email_validation': 0},
        {'id': 3, 'first_name': 'Carlos', 'last_first_name': 'García', 'password': 'carlos123', 'email': 'carlos.garcia@example.com', 'username': 'carlosgarcia', 'creation_date': '2023-03-15', 'email_validation': 1},
        {'id': 4, 'first_name': 'Ana', 'last_first_name': 'Martínez', 'password': 'ana456', 'email': 'ana.martinez@example.com', 'username': 'anamartinez', 'creation_date': '2023-04-10', 'email_validation': 0},
        {'id': 5, 'first_name': 'Luis', 'last_first_name': 'Rodríguez', 'password': 'luis789', 'email': 'luis.rodriguez@example.com', 'username': 'luisrodriguez', 'creation_date': '2023-05-05', 'email_validation': 1},
        {'id': 6, 'first_name': 'Sofía', 'last_first_name': 'Fernández', 'password': 'sofia123', 'email': 'sofia.fernandez@example.com', 'username': 'sofiafernandez', 'creation_date': '2023-06-20', 'email_validation': 1},
        {'id': 7, 'first_name': 'Pedro', 'last_first_name': 'Gómez', 'password': 'pedro987', 'email': 'pedro.gomez@example.com', 'username': 'pedrogomez', 'creation_date': '2023-07-07', 'email_validation': 0},
        {'id': 8, 'first_name': 'Laura', 'last_first_name': 'Díaz', 'password': 'laura654', 'email': 'laura.diaz@example.com', 'username': 'lauradiaz', 'creation_date': '2023-08-15', 'email_validation': 1},
        {'id': 9, 'first_name': 'Diego', 'last_first_name': 'Torres', 'password': 'diego321', 'email': 'diego.torres@example.com', 'username': 'diegotorres', 'creation_date': '2023-09-01', 'email_validation': 1},
        {'id': 10, 'first_name': 'Lucía', 'last_first_name': 'Ramírez', 'password': 'lucia321', 'email': 'lucia.ramirez@example.com', 'username': 'luciaramirez', 'creation_date': '2023-09-20', 'email_validation': 0}
    ]
    drivers = [
        {'user_id': 1}
    ]
    vehicle_driver = [
        {'id': 1, 'driver_id': 1, 'vehicle_id': 1},
    ]
    vehicle = [
        {'id': 1, 'licence_plate': 'ABC123', 'brand': 'Toyota', 'model': 'Corolla', 'year': 2020, 'color': 'Rojo'},
    ]
    passenger = [
        {'user_id': 2},
        {'user_id': 5},
        {'user_id': 8},
    ]
    passenger_trip = [
        {'id':1,'id_trip': 1, 'passenger_id': 2},
        {'id':2, 'id_trip': 1, 'passenger_id': 5},
    ]
    trip = [
        {'id': 1, 'departure_date': '2023-10-01', 'departure_time': '08:00','available_seats': 2,'seat_price':2600, 'creation_timestamp':'2024-09-11' ,'deaparture_address_id': 1, 'arrival_address_id': 2, 'driver_id': 1, 'passenger_id': 2},
        {'id': 2, 'departure_date': '2023-10-01', 'departure_time': '08:00','available_seats': 2,'seat_price':2600, 'creation_timestamp':'2024-09-11' ,'deaparture_address_id': 1, 'arrival_address_id': 2, 'driver_id': 1, 'passenger_id': 2}
    ]
    address = [
        {'id': 1, 'address': 'Calle 1, Ciudad 1'},
        {'id': 2, 'address': 'Calle 2, Ciudad 2'},
    ]
 