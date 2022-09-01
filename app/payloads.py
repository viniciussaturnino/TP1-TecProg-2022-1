from app.exceptions import DescricaoEmBrancoException, ValorAcessoInvalidoException

from datetime import datetime

class PayloadVariable:
    def __init__(self, value, required=True, custom_validation=None):
        self.value = value
        self.required = required
        self.custom_validation = custom_validation


class BasePayload:
    def __setattr__(self, name: str, variable: PayloadVariable):
        if not isinstance(variable, PayloadVariable):
            raise Exception('Value is not a PayloadVariable')

        if variable.required:
            if not variable.value:
                raise DescricaoEmBrancoException(name)

        if variable.custom_validation:
            variable.custom_validation(variable.value, name)

        super(BasePayload, self).__setattr__(name, variable.value)


class ParkingLot(BasePayload):
    def __init__(self, payload: dict) -> None:
        self.name = PayloadVariable(payload.get("name"))
        self.fraction_value = PayloadVariable(
            value=payload.get("fraction_value"),
            custom_validation=self.validate_if_variable_is_a_valid_int
        )
        self.fulltime_value = PayloadVariable(
            value=payload.get("fulltime_value"),
            required=False,
            custom_validation=self.validate_if_variable_is_a_valid_int
        )
        self.daily_value_daytime = PayloadVariable(
            value=payload.get("daily_value_daytime"),
            custom_validation=self.validate_if_variable_is_a_valid_int
        )
        self.daily_value_overnight = PayloadVariable(
            value=payload.get("daily_value_overnight"),
            custom_validation=self.validate_if_variable_is_a_valid_int
        )
        self.daily_overnight_initial_hour = PayloadVariable(
            value=payload.get("daily_overnight_initial_hour"),
            custom_validation=self.validate_if_variable_is_a_valid_str
        )
        self.daily_overnight_end_hour = PayloadVariable(
            value=payload.get("daily_overnight_end_hour"),
            custom_validation=self.validate_if_variable_is_a_valid_str
        )
        self.subscription_access_value = PayloadVariable(
            value=payload.get("subscription_access_value"),
            custom_validation=self.validate_if_variable_is_a_valid_int
        )
        self.event_access_value = PayloadVariable(
            value=payload.get("event_access_value"),
            custom_validation=self.validate_if_variable_is_a_valid_int
        )
        self.opening_hour = PayloadVariable(
            value=payload.get("opening_hour"),
            custom_validation=self.validate_if_variable_is_a_valid_str
        )
        self.closing_hour = PayloadVariable(
            value=payload.get("closing_hour"),
            custom_validation=self.validate_if_variable_is_a_valid_str
        )
        self.capacity = PayloadVariable(
            value=payload.get("capacity"),
            custom_validation=self.validate_if_variable_is_a_valid_int
        )
        self.contractor_percentage_revenue = PayloadVariable(
            value=payload.get("contractor_percentage_revenue"),
            custom_validation=self.validate_if_variable_is_a_valid_int
        )
        self.parking_accesses = PayloadVariable(
            value=[],
            required=False
        )
        self.total_parking_accesses_revenue = PayloadVariable(
            value=0,
            required=False,
            custom_validation=self.validate_if_variable_is_a_valid_int
        )

    def to_dict(self):
        return vars(self)

    def validate_if_variable_is_a_valid_str(self, variable, name):
        if not (isinstance(variable, str) and len(variable) == 8):
            raise ValorAcessoInvalidoException(name=name)

    def validate_if_variable_is_a_valid_int(self, variable, field):
        if not (isinstance(variable, int) and variable >= 0):
            raise ValorAcessoInvalidoException(field=field)
    
    def register_parking_access(self, parking_access: dict):
        # Tratamento de exceção de dados em branco
        keys = ["license_plate", "checkin", "checkout"]
        for key in keys:
            if key not in parking_access.keys():
                raise DescricaoEmBrancoException(parameter_name=key)
        
        # Tratamento de exceção de dados inválidos
        self.parking_access_data_is_valid(parking_access=parking_access)
        
        price = self.get_parking_access_price(parking_access=parking_access)
        parking_access['price'] = price
        self.total_parking_accesses_revenue = PayloadVariable(
            value=(self.total_parking_accesses_revenue + price),
            required=False,
            custom_validation=self.validate_if_variable_is_a_valid_int    
        )

        self.parking_accesses.append(parking_access)
        return price

    def parking_access_data_is_valid(self, parking_access: dict):
        for key, value in parking_access.items():
            if not isinstance(key, str):
                raise ValorAcessoInvalidoException(field=key)
            if key == "license_plate" and len(value) != 5:
                raise ValorAcessoInvalidoException(field=key)
            if key in ["checkin", "checkout"] and len(value) != 8:
                raise ValorAcessoInvalidoException(field=key)

    def get_parking_accesses(self):
        return self.parking_accesses
    
    def get_parking_access_price(self, parking_access: dict):
        if parking_access['type'] == 'Mensalista':
            return self.subscription_access_value
        elif parking_access['type'] == 'Evento':
            return self.event_access_value
        else:
            return self.get_parking_access_price_by_time(parking_access=parking_access)
             
    def get_parking_access_price_by_time(self, parking_access: dict):
        checkin = datetime.strptime(parking_access.get('checkin'), "%H:%M:%S")
        checkout = datetime.strptime(parking_access.get('checkout'), "%H:%M:%S")

        if checkin >= datetime.strptime(self.daily_overnight_initial_hour, "%H:%M:%S"
        ) and checkout <= datetime.strptime(self.daily_overnight_end_hour, "%H:%M:%S"):
            return self.daily_value_daytime*(self.daily_value_overnight/100)
        
        total_seconds = (checkout-checkin).seconds
        hours = int(total_seconds/3600)

        if hours >= 9:
            return self.daily_value_daytime

        
        minutes = int((total_seconds - (hours*3600))/60)
        hours_value = int(hours*((4*self.fraction_value)*(1 - (self.fulltime_value/100))))
        minutes_value = int(minutes/15)*self.fraction_value

        return hours_value+minutes_value

class ParkingSystem(BasePayload):
    def __init__(self):
        self.parking_lots = PayloadVariable(value=[], required=False)

    def to_dict(self):
        return vars(self)

    def register_parking_lot(self, parking_lot: ParkingLot):
        self.parking_lots.append(parking_lot)
