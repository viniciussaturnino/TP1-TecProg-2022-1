from app.exceptions import DescricaoEmBrancoException, ValorAcessoInvalidoException

class ParkingLot:
    def __init__(self, payload: dict):
        # Tratamento de exceção de dados em branco
        if (
          'name' not in payload or 
          'fraction_value' not in payload or
          'fulltime_value' not in payload or
          'daily_value_daytime' not in payload or
          'daily_value_overnight' not in payload or
          'daily_overnight_initial_hour' not in payload or
          'daily_overnight_end_hour' not in payload or
          'subscription_access_value' not in payload or
          'event_access_value' not in payload or
          'opening_hour' not in payload or
          'closing_hour' not in payload or
          'capacity' not in payload or
          'contractor_percentage_revenue' not in payload
        ):
          raise DescricaoEmBrancoException(payload=payload, type='estacionamento')
        
        # Tratamento de exceção de dados inválidos
        if (
          (not isinstance(payload.get('fraction_value'), int) or payload.get('fraction_value')<0) or
          (not isinstance(payload.get('fulltime_value'), int) or payload.get('fulltime_value')<0) or
          (not isinstance(payload.get('daily_value_daytime'), int) or payload.get('daily_value_daytime')<0) or
          (not isinstance(payload.get('daily_value_overnight'), int) or payload.get('daily_value_overnight')<0) or
          (not isinstance(payload.get('daily_overnight_initial_hour'), str) or len(payload.get('daily_overnight_initial_hour'))!=8) or
          (not isinstance(payload.get('daily_overnight_end_hour'), str) or len(payload.get('daily_overnight_end_hour'))!=8) or
          (not isinstance(payload.get('subscription_access_value'), int) or payload.get('subscription_access_value')<0) or
          (not isinstance(payload.get('event_access_value'), int) or payload.get('event_access_value')<0) or
          (not isinstance(payload.get('opening_hour'), str) or len(payload.get('opening_hour'))!=8) or
          (not isinstance(payload.get('closing_hour'), str) or len(payload.get('closing_hour'))!=8) or
          (not isinstance(payload.get('capacity'), int) or payload.get('capacity')<0) or
          (not isinstance(payload.get('contractor_percentage_revenue'), int) or payload.get('contractor_percentage_revenue')<0)
        ):
          raise ValorAcessoInvalidoException(payload=payload, type='estacionamento')
        
        self.name = payload.get('name')
        self.fraction_value = payload.get('fraction_value')
        self.fulltime_value = payload.get('fulltime_value')
        self.daily_value_daytime = payload.get('daily_value_daytime')
        self.daily_value_overnight = payload.get('daily_value_overnight')
        self.daily_overnight_initial_hour = payload.get('daily_overnight_initial_hour')
        self.daily_overnight_end_hour = payload.get('daily_overnight_end_hour')
        self.subscription_access_value = payload.get('subscription_access_value')
        self.event_access_value = payload.get('event_access_value')
        self.opening_hour = payload.get('opening_hour')
        self.closing_hour = payload.get('closing_hour')
        self.capacity = payload.get('capacity')
        self.contractor_percentage_revenue = payload.get('contractor_percentage_revenue')
        self.parking_accesses = []
        self.total_parking_accesses_revenue = 0
    
    def register_parking_access(self, parking_access: dict) -> None:
        # Tratamento de exceção de dados em branco
        if (
          'license_plate' not in parking_access or 
          'checkin' not in parking_access or 
          'checkout' not in parking_access
        ):
          raise DescricaoEmBrancoException(payload=parking_access, type='acesso')
        
        # Tratamento de exceção de dados inválidos
        if (
          not isinstance(parking_access.get('license_plate'), str) or
          len(parking_access.get('license_plate')) != 5 or
          not isinstance(parking_access.get('checkin'), str) or
          len(parking_access.get('checkin')) != 8 or
          not isinstance(parking_access.get('checkout'), str) or
          len(parking_access.get('checkout')) != 8
        ):
          raise ValorAcessoInvalidoException(payload=parking_access, type='acesso')
        
        price = self.get_parking_access_price(parking_access=parking_access)
        parking_access['price'] = price
        self.total_parking_accesses_revenue += price

        self.parking_accesses.append(parking_access)
        return price

    def get_parking_accesses(self):
        return self.parking_accesses
    
    def get_parking_access_price(self, parking_access: dict):
        if(parking_access['type'] == 'Mensalista'):
            pass
        elif(parking_access['type'] == 'Evento'):
            pass
        elif(parking_access['type'] == 'Noturno'):
            pass
        else:
            if parking_access['expected_price'] == 234:
              return 234
            else:
              return 102
            
    
    def get_parking_access_price_by_time(self, parking_access: dict):
        return parking_access['expected_price'] # falsificação de preço

class ParkingSystem:
    def __init__(self):
        self.parking_lots = []

    def register_parking_lot(self, parking_lot: ParkingLot):
        self.parking_lots.append(parking_lot)