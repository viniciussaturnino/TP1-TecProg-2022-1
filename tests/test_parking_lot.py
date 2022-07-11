from unittest import TestCase
from app.payloads import ParkingLot


class TestCaseParkingLot(TestCase):

    def test_create_parking_lot(self) -> None:
        payload = dict(
            name="1",
            fraction_value="1",
            fulltime_value="1",
            daily_value_daytime="1",
            daily_value_overnight="1",
            subscription_access_value="1",
            event_access_value="1",
            opening_hours="1",
            capacity="1",
            contractor_percentage_revenue="1"
        )

        self.parking_lot = ParkingLot(parking_lot=payload)

        self.assertIsInstance(self.parking_lot, ParkingLot)
        self.assertEqual(self.parking_lot.__dict__, payload)
        self.assertIsNotNone(self.parking_lot)
