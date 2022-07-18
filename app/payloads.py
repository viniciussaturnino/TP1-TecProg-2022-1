from app.exceptions import DescricaoEmBrancoException, ValorAcessoInvalidoException

class ParkingLot:
    def __init__(self, payload: dict):
        # Tratamento de exceção de dados em branco
        if (
          not 'name' in payload or 
          not 'fraction_value' in payload or
          not 'fulltime_value' in payload or
          not 'daily_value_daytime' in payload or
          not 'daily_value_overnight' in payload or
          not 'daily_overnight_initial_hour' in payload or
          not 'daily_overnight_end_hour' in payload or
          not 'subscription_access_value' in payload or
          not 'event_access_value' in payload or
          not 'opening_hour' in payload or
          not 'closing_hour' in payload or
          not 'capacity' in payload or
          not 'contractor_percentage_revenue' in payload
        ):
          raise DescricaoEmBrancoException(payload=payload, type='estacionamento')
        
        # Tratamento de exceção de dados inválidos
        if (
          (type(payload.get('fraction_value')) != int or payload.get('fraction_value')<0) or
          (type(payload.get('fulltime_value')) != int or payload.get('fulltime_value')<0) or
          (type(payload.get('daily_value_daytime')) != int or payload.get('daily_value_daytime')<0) or
          (type(payload.get('daily_value_overnight')) != int or payload.get('daily_value_overnight')<0) or
          (type(payload.get('daily_overnight_initial_hour')) != int or payload.get('daily_overnight_initial_hour')<0) or
          (type(payload.get('daily_overnight_end_hour')) != int or payload.get('daily_overnight_end_hour')<0) or
          (type(payload.get('subscription_access_value')) != int or payload.get('subscription_access_value')<0) or
          (type(payload.get('event_access_value')) != int or payload.get('event_access_value')<0) or
          (type(payload.get('opening_hour')) != int or payload.get('opening_hour')<0) or
          (type(payload.get('closing_hour')) != int or payload.get('closing_hour')<0) or
          (type(payload.get('capacity')) != int or payload.get('capacity')<0) or
          (type(payload.get('contractor_percentage_revenue')) != int or payload.get('contractor_percentage_revenue')<0)
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
          not 'license_plate' in parking_access or 
          not 'checkin' in parking_access or 
          not 'checkout' in parking_access
        ):
          raise DescricaoEmBrancoException(payload=parking_access, type='acesso')
        price = self.get_parking_access_price(parking_access=parking_access)
        parking_access['price'] = price
        self.total_parking_accesses_revenue += price

        self.parking_accesses.append(parking_access)
        return self.parking_accesses

    def get_parking_accesses(self, ):
        return self.parking_accesses
    
    def get_parking_access_price(self, parking_access: dict):
        if(parking_access['type'] == 'Mensalista'):
            return self.subscription_access_value
        elif(parking_access['type'] == 'Evento'):
            return self.event_access_value
        elif(parking_access['type'] == 'Noturno'):
            return 54
        else:
            return self.get_parking_access_price_by_time(parking_access=parking_access)
            
    
    def get_parking_access_price_by_time(self, parking_access: dict):
        return parking_access['expected_price'] # falsificação de preço

class ParkingSystem:
    def __init__(self):
        self.parking_lots = []

    def register_parking_lot(self, parking_lot: ParkingLot):
        self.parking_lots.append(parking_lot)