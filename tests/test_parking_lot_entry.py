import pytest
from unittest import TestCase
from app.payloads import ParkingLot, ParkingSystem

class TestEntradasNoEstacionamento(TestCase):
    def setUp(self):
        payload = dict(
            name="Estac. 1",
            fraction_value=30,
            fulltime_value=15,
            daily_value_daytime= 120,
            daily_value_overnight=45,
            daily_overnight_initial_hour=19,
            daily_overnight_end_hour=8,
            subscription_access_value=600,
            event_access_value=50,
            opening_hour=6,
            closing_hour=22,
            capacity=300,
            contractor_percentage_revenue=50
        )
        self.parking_lot = ParkingLot(payload=payload)
        

    def test_entrada_no_estacionamento(self):
        payload = dict(
            license_plate="HI139",
            checkin='08:30:00',
            checkout='08:56:00'
        )
        parking_access = self.parking_lot.register_parking_access(parking_access=payload)

        assert parking_access == payload
    
    def test_entrada_no_estacionamento_b(self):
        payload1 = dict(
            license_plate="HI139",
            checkin='08:30:00',
            checkout='08:56:00'
        )
        payload2 = dict(
            license_plate="HI139",
            checkin='08:30:00',
            checkout='08:56:00'
        )

        self.parking_lot.register_parking_access(parking_access=payload1)

        parking_accesses = self.parking_lot.register_parking_access(parking_access=payload2)

        assert parking_accesses[0] == payload1
        assert parking_accesses[1] == payload2

      
      
