class ParkingLot:
    def __init__(self, payload: dict):
        self.name = payload.get('name')
        self.fraction_value = payload.get('fraction_value')
        self.fulltime_value = payload.get('fulltime_value')
        self.daily_value_daytime = payload.get('daily_value_daytime')
        self.daily_value_overnight = payload.get('daily_value_overnight')
        self.daily_overnight_initial_hour = payload.get('daily_overnight_initial_hour')
        self.daily_overnight_end_hour = payload.get('daily_overnight_end_hour')
        self.subscription_access_value = payload.get('subscription_access_value')
        self.event_access_value = payload.get('event_access_value')
        self.opening_hour = payload.get('opening_hour')
        self.closing_hour = payload.get('closing_hour')
        self.capacity = payload.get('capacity')
        self.contractor_percentage_revenue = payload.get('contractor_percentage_revenue')

class ParkingLotAccess:
    def __init__(self, payload: dict):
        self.license_plate = payload.get('license_plate')
        self.checkin = payload.get('checkin')
        self.checkout = payload.get('checkout')

class ParkingSystem:
    def __init__(self):
        self.parking_lots = []
        self.parking_accesses = []

    def register_parking_lot(self, parking_lot: ParkingLot):
        self.parking_lots.append(parking_lot)

    def register_parking_access(self, access: ParkingLotAccess):
        self.parking_accesses.append(access)