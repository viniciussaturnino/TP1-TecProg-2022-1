from unittest import TestCase
from app.payloads import ParkingLot
from app.payloads import ParkingSystem, ParkingLotAccess


class TestCaseParkingLotSystem(TestCase):
    def setUp(self):
       self.parking_lot_system = ParkingSystem()

    def test_register_parking_lot(self) -> None:
        payload = dict(
            name = "Estac. 1",
            fraction_value = 30,
            fulltime_value = 15,
            daily_value_daytime =  120,
            daily_value_overnight = 45,
            daily_overnight_initial_hour = 19,
            daily_overnight_end_hour = 8,
            subscription_access_value = 600,
            event_access_value = 50,
            opening_hour = 6,
            closing_hour = 22,
            capacity = 300,
            contractor_percentage_revenue = 50
        )
        parking_lot = ParkingLot(payload=payload)
        self.parking_lot_system.register_parking_lot(parking_lot=parking_lot)
        self.assertIsInstance(parking_lot, ParkingLot)
        self.assertEqual(len(self.parking_lot_system.parking_lots), 1)

    def test_register_access(self) -> None:
        parking_access = ParkingLotAccess()

        self.parking_lot_system.register_parking_access(access=parking_access)
        self.assertIsInstance(parking_access, ParkingLotAccess)
        self.assertEqual(len(self.parking_lot_system.parking_accesses), 1)
