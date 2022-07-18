from unittest import TestCase
from app.payloads import ParkingLot

from app.exceptions import DescricaoEmBrancoException


class TesteExcecao(TestCase):
    def test_create_blank_parking_lot(self) -> None:
        self.assertRaises(DescricaoEmBrancoException, ParkingLot, {}) # Dados em branco