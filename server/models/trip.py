from server.db import db

class Trip(db.Model):
    __tablename__ = 'Trip'

    id = db.Column(db.Integer, primary_key=True)
    departure_date = db.Column(db.Date, nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    seat_price = db.Column(db.Float, nullable=False)
    creation_timestamp = db.Column(db.DateTime, nullable=False)
    departure_address_id = db.Column(db.Integer, db.ForeignKey('Address.id'), nullable=False)
    arrival_address_id = db.Column(db.Integer, db.ForeignKey('Address.id'), nullable=False)
    vehicle_driver_id = db.Column(db.String(28), db.ForeignKey('Vehicle_Driver.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='active')

    departure_address = db.relationship('Address', foreign_keys=[departure_address_id])
    arrival_address = db.relationship('Address', foreign_keys=[arrival_address_id])
    vehicle_driver = db.relationship('Vehicle_Driver', foreign_keys=[vehicle_driver_id])

    def to_dict(self):
        return {
            'id': self.id,
            'departure_date': self.departure_date.strftime('%Y-%m-%d'),
            'departure_time': self.departure_time.strftime('%H:%M:%S'),
            'available_seats': self.available_seats,
            'seat_price': self.seat_price,
            'creation_timestamp': self.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'departure_address': self.departure_address.to_dict() if self.departure_address else None,
            'arrival_address': self.arrival_address.to_dict() if self.arrival_address else None,
            'vehicle_driver': self.vehicle_driver.to_dict() if self.vehicle_driver else None,
            'status': self.status
        }

    def to_dict_less(self):
        return {
            'id': self.id,
            'departure_date': self.departure_date.strftime('%Y-%m-%d'),
            'departure_time': self.departure_time.strftime('%H:%M:%S'),
            'available_seats': self.available_seats,
            'seat_price': self.seat_price,
            'creation_timestamp': self.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'departure_address': self.departure_address_id,
            'arrival_address': self.arrival_address_id,
            'vehicle_driver': self.vehicle_driver_id,
            'status': self.status
        }

    def to_dict_joined(self):
        return {
        'id': self.id,
        'departure_date': self.departure_date.strftime('%Y-%m-%d'),
        'departure_time': self.departure_time.strftime('%H:%M:%S'),
        'available_seats': self.available_seats,
        'seat_price': self.seat_price,
        'creation_timestamp': self.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'departure_address': {
            'id': self.departure_address.id,
            'street': self.departure_address.street,
            'number': self.departure_address.number,
            'longitude': self.departure_address.longitude,
            'latitude': self.departure_address.latitude,
            'locality': {
                'id': self.departure_address.locality.id,
                'name': self.departure_address.locality.name,
                'principal_subdivision': {
                    'id': self.departure_address.locality.principal_subdivision.id,
                    'name': self.departure_address.locality.principal_subdivision.name,
                    'country': {
                        'id': self.departure_address.locality.principal_subdivision.country.id,
                        'country': self.departure_address.locality.principal_subdivision.country.country
                    }
                }
            }
        } if self.departure_address else None,
        'arrival_address': {
            'id': self.arrival_address.id,
            'street': self.arrival_address.street,
            'number': self.arrival_address.number,
            'longitude': self.arrival_address.longitude,
            'latitude': self.arrival_address.latitude,
            'locality': {
                'id': self.arrival_address.locality.id,
                'name': self.arrival_address.locality.name,
                'principal_subdivision': {
                    'id': self.arrival_address.locality.principal_subdivision.id,
                    'name': self.arrival_address.locality.principal_subdivision.name,
                    'country': {
                        'id': self.arrival_address.locality.principal_subdivision.country.id,
                        'country': self.arrival_address.locality.principal_subdivision.country.country
                    }
                }
            }
        } if self.arrival_address else None,
        'vehicle_driver': {
            'driver_id': self.vehicle_driver.driver_id,
            'vehicle_id': self.vehicle_driver.vehicle_id,
            'vehicle': {
                'id': self.vehicle_driver.vehicle.id,
                'license_plate': self.vehicle_driver.vehicle.license_plate,
                'brand': self.vehicle_driver.vehicle.brand,
                'model': self.vehicle_driver.vehicle.model,
                'color': self.vehicle_driver.vehicle.color,
                'year': self.vehicle_driver.vehicle.year
                },
            'driver': {
                'user': {
                    'id': self.vehicle_driver.driver.user.id,
                    'first_name': self.vehicle_driver.driver.user.first_name,
                    'last_name': self.vehicle_driver.driver.user.last_name,
                    'email': self.vehicle_driver.driver.user.email,
                    'username': self.vehicle_driver.driver.user.username,
                    'creation_date': self.vehicle_driver.driver.user.creation_date,
                    'expo_push_token': self.vehicle_driver.driver.user.expo_push_token
                },
                'user_id': self.vehicle_driver.driver_id,
                'rating': self.vehicle_driver.driver.rating,
                'rating_count': self.vehicle_driver.driver.rating_count
            } if self.vehicle_driver.driver else None
        } if self.vehicle_driver else None,
        'status': self.status
    }

    def cancel_trip(self):
        self.status = 'cancelled'
        db.session.commit()

    def complete_trip(self):
        self.status = 'completed'
        db.session.commit()