import pytest
from app.payloads import ParkingLot

@pytest.mark.parametrize("parking_lot_payload", [
    dict(
        name="Estac. 1",
        fraction_value=30,
        fulltime_value=15,
        daily_value_daytime= 120,
        daily_value_overnight=45,
        daily_overnight_initial_hour ="19:00:00",
        daily_overnight_end_hour="08:00:00",
        subscription_access_value=600,
        event_access_value=50,
        opening_hour="08:00:00",
        closing_hour="19:00:00",
        capacity=300,
        contractor_percentage_revenue=50
    ),
    dict(
        name="Estac. 2",
        fraction_value=20,
        fulltime_value=10,
        daily_value_daytime= 70,
        daily_value_overnight=30,
        daily_overnight_initial_hour ="19:00:00",
        daily_overnight_end_hour="08:00:00",
        subscription_access_value=455,
        event_access_value=60,
        opening_hour="08:00:00",
        closing_hour="19:00:00",
        capacity=120,
        contractor_percentage_revenue=60
    ),
    dict(
        name="Estac. 3",
        fraction_value=10,
        fulltime_value=0,
        daily_value_daytime= 50,
        daily_value_overnight=40,
        daily_overnight_initial_hour ="19:00:00",
        daily_overnight_end_hour="08:00:00",
        subscription_access_value=350,
        event_access_value=40,
        opening_hour="08:00:00",
        closing_hour="19:00:00",
        capacity=600,
        contractor_percentage_revenue=70
    )
])
class TestParkingLot:
    def test_create_parking(self, parking_lot_payload):
        parking_lot=ParkingLot(payload=parking_lot_payload)
        assert isinstance(parking_lot, ParkingLot)
