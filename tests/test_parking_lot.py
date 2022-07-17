from unittest import TestCase
from app.payloads import ParkingLot

class TestCaseParkingLot(TestCase):

    def test_create_parking_lot_a(self) -> None:
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

        self.parking_lot = ParkingLot(payload=payload)

        self.assertIsInstance(self.parking_lot, ParkingLot)
        self.assertEqual(self.parking_lot.__dict__, payload)
        self.assertIsNotNone(self.parking_lot)
    
    def test_create_parking_lot_b(self) -> None:
        payload = dict(
            name = "Estac. 2",
            fraction_value = 20,
            fulltime_value = 10,
            daily_value_daytime =  70,
            daily_value_overnight = 30,
            daily_overnight_initial_hour = 21,
            daily_overnight_end_hour = 7,
            subscription_access_value = 455,
            event_access_value = 60,
            opening_hour = 0,
            closing_hour = 24,
            capacity = 120,
            contractor_percentage_revenue = 60
        )

        self.parking_lot = ParkingLot(payload=payload)

        self.assertIsInstance(self.parking_lot, ParkingLot)
        self.assertEqual(self.parking_lot.__dict__, payload)
        self.assertIsNotNone(self.parking_lot)

    def test_create_parking_lot_c(self) -> None:
        payload = dict(
            name = "Estac. 3",
            fraction_value = 10,
            fulltime_value = 0,
            daily_value_daytime =  50,
            daily_value_overnight = 40,
            daily_overnight_initial_hour = 20,
            daily_overnight_end_hour = 8,
            subscription_access_value = 350,
            event_access_value = 40,
            opening_hour = 6,
            closing_hour = 22,
            capacity = 600,
            contractor_percentage_revenue = 70
        )

        self.parking_lot = ParkingLot(payload=payload)

        self.assertIsInstance(self.parking_lot, ParkingLot)
        self.assertEqual(self.parking_lot.__dict__, payload)
        self.assertIsNotNone(self.parking_lot)
