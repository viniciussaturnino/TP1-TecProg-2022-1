import pytest
from app.payloads import ParkingLot

@pytest.mark.parametrize("parking_lot_entries", [
    [
        dict(
            license_plate="PB139",
            checkin="10:00:00",
            checkout="12:15:00",
            type = None,
            expected_price = 234
        )
    ],
    [   dict(
            license_plate="PB139",
            checkin="10:00:00",
            checkout="11:00:00",
            type = None,
            expected_price = 102
        )
    ],
    [
        dict(
            license_plate="G49NG",
            checkin="12:00:00",
            checkout="13:30:00",
            type = None,
            expected_price = 162
        )
    ],
  ]
)
class TestCalculoHoraCheia:            
    def test_calculo_hora_cheia(self, parking_lot_entries):
        payload = dict(
            name="Estac. 1",
            fraction_value=30,
            fulltime_value=15,
            daily_value_daytime= 120,
            daily_value_overnight=45,
            daily_overnight_initial_hour="19:00:00",
            daily_overnight_end_hour="08:00:00",
            subscription_access_value=600,
            event_access_value=50,
            opening_hour="08:00:00",
            closing_hour="19:00:00",
            capacity=300,
            contractor_percentage_revenue=50
        )
        parking_lot = ParkingLot(payload=payload)

        for entrada in parking_lot_entries:
            parking_lot.register_parking_access(parking_access=entrada)

        parking_accesses = parking_lot.get_parking_accesses()
        assert parking_accesses == parking_lot_entries

        for acesso in parking_accesses:
            assert acesso['price'] == acesso['expected_price']

@pytest.mark.parametrize("parking_lot_entries", [
    [
        dict(
            license_plate="V49NG",
            checkin="20:00:00",
            checkout="22:00:00",
            type = None,
            expected_price = 204
        )
    ],
    [   dict(
            license_plate="PB139",
            checkin="20:00:00",
            checkout="21:00:00",
            type = None,
            expected_price = 102
        )
    ],
    [
        dict(
            license_plate="G49NG",
            checkin="19:30:00",
            checkout="22:30:00",
            type = None,
            expected_price = 306
        )
    ],
  ]
)
class TestCalculoAcessoNoturno:
    def test_calculo_acesso_noturno(self, parking_lot_entries):
        payload = dict(
            name="Estac. 1",
            fraction_value=30,
            fulltime_value=15,
            daily_value_daytime= 120,
            daily_value_overnight=45,
            daily_overnight_initial_hour="19:00:00",
            daily_overnight_end_hour="08:00:00",
            subscription_access_value=600,
            event_access_value=50,
            opening_hour="08:00:00",
            closing_hour="23:00:00",
            capacity=300,
            contractor_percentage_revenue=50
        )
        parking_lot = ParkingLot(payload=payload)

        for entrada in parking_lot_entries:
            parking_lot.register_parking_access(parking_access=entrada)

        parking_accesses = parking_lot.get_parking_accesses()
        assert parking_accesses == parking_lot_entries

        for acesso in parking_accesses:
            assert acesso['price'] == acesso['expected_price']