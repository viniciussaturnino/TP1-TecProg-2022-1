from unittest import TestCase
from app.payloads import ParkingLot


class TestCaseParkingLot(TestCase):

    def test_create_parking_lot(self) -> None:
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
