from unittest import TestCase
from app.payloads import ParkingLot

from app.exceptions import DescricaoEmBrancoException


class TesteExcecao(TestCase):
    def test_criacao_em_branco_de_estacionamento(self) -> None:
        self.assertRaises(DescricaoEmBrancoException, ParkingLot, {}) # Dados em branco
    
    def test_entrada_em_branco_no_estacionamento(self):
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
        
        self.assertRaises(DescricaoEmBrancoException, self.parking_lot.register_parking_access, {}) # Dados de acesso em branco