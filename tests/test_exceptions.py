from unittest import TestCase
from app.payloads import ParkingLot

from app.exceptions import DescricaoEmBrancoException, ValorAcessoInvalidoException


class TesteExcecao(TestCase):
    def test_criacao_em_branco_de_estacionamento(self) -> None:
        self.assertRaises(DescricaoEmBrancoException, ParkingLot, {}) # Dados em branco
    
    def test_entrada_em_branco_no_estacionamento(self) -> None:
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
        self.parking_lot = ParkingLot(payload=payload)
        
        self.assertRaises(DescricaoEmBrancoException, self.parking_lot.register_parking_access, {}) # Dados de acesso em branco
    
    def test_criacao_com_dados_invalidos_de_estacionamento(self) -> None:
        invalid_payload = dict(
            name="Estac. 1",
            fraction_value=-30,
            fulltime_value=-15,
            daily_value_daytime=- 120,
            daily_value_overnight=-45,
            daily_overnight_initial_hour="0008:00:00",
            daily_overnight_end_hour="19:00:000000",
            subscription_access_value=-600,
            event_access_value=-50,
            opening_hour="0008:00:00",
            closing_hour="19:00:00000",
            capacity=-300,
            contractor_percentage_revenue=-50.4
        ) # Dados inválidos(negativos e não inteiros)
        self.assertRaises(ValorAcessoInvalidoException, ParkingLot, invalid_payload)
        
    def test_criacao_de_entrada_com_dados_invalidos_no_estacionamento(self) -> None:
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
        self.parking_lot = ParkingLot(payload=payload)
        
        invalid_payload = dict(
            license_plate="0",
            checkin="08:30:0021231",
            checkout="08:56:00aaaa",
            type=None,
            expected_price=60
        ) # Dados inválidos (não string e tamanho inválido)
        self.assertRaises(ValorAcessoInvalidoException, self.parking_lot.register_parking_access, invalid_payload)
        
      