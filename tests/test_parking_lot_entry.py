import pytest
from app.payloads import ParkingLot

@pytest.mark.parametrize("parking_lot_entries", [
    [
        dict(
            license_plate="HI139",
            checkin='08:30:00',
            checkout='08:56:00',
        )
    ],
    [   dict(
            license_plate="HI139",
            checkin='08:30:00',
            checkout='08:56:00'
        ), 
        dict(
            license_plate="G49NG",
            checkin='15:12:00',
            checkout='16:00:00'
        )
    ],
    [   dict(
            license_plate="HI139",
            checkin='08:30:00',
            checkout='08:56:00'
        ), 
        dict(
            license_plate="G49NG",
            checkin='15:12:00',
            checkout='16:00:00'
        ),
        dict(
            license_plate="AC50M",
            checkin='08:00:00',
            checkout='18:00:00'
        )
    ],
])
class TestEntradasNoEstacionamento:        
    def test_entradas_no_estacionamento(self, parking_lot_entries):
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

        for entrada in parking_lot_entries:
            self.parking_lot.register_parking_access(parking_access=entrada)

        parking_accesses = self.parking_lot.get_parking_accesses()
        assert parking_accesses == parking_lot_entries