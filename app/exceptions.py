class DescricaoEmBrancoException(Exception):
  def __init__(self, payload, type, message='Dados obrigatórios em branco:'):
    blank_fields = []
    
    if type == 'acesso': # Dados em branco no fluxo de acesso
      if 'license_plate' not in payload:
        blank_fields.append('placa do carro')
      if 'checkin' not in payload:
        blank_fields.append('hora de entrada')
      if 'checkout' not in payload:
        blank_fields.append('hora de saída')
    
    elif type == 'estacionamento': # Dados em branco no cadastro de estacionamento
      if 'name' not in payload:
        blank_fields.append('nome do estacionamento')
      if 'opening_hour' not in payload or 'closing_hour' not in payload:
        blank_fields.append('horário de funcionamento')
      if 'fraction_value' not in payload:
        blank_fields.append('valor fração')
      if 'fulltime_value' not in payload:
        blank_fields.append('valor hora cheia')
      if 'daily_value_daytime' not in payload:
        blank_fields.append('valor diária diurna')
      if 'daily_value_overnight' not in payload:
        blank_fields.append('valor diária noturna')
      if 'subscription_access_value' not in payload:
        blank_fields.append('valor acesso mensalista')
      if 'event_access_value' not in payload:
        blank_fields.append('valor acesso evento')
      if 'daily_overnight_initial_hour' not in payload or 'daily_overnight_end_hour' not in payload:
        blank_fields.append('horário da diária noturna')
      if 'contractor_percentage_revenue' not in payload:
        blank_fields.append('valor da porcentagem do contratante')
      if 'capacity' not in payload:
        blank_fields.append('capacidade do estacionamento')

    self.message = message
    self.blank_fields = blank_fields

    super().__init__(self.message)
    
  def __str__(self):
    return f'{self.message} {self.blank_fields}'
  
class ValorAcessoInvalidoException(Exception):
  def __init__(self, payload, type, message='Dados de acesso inválidos:'):
    invalid_fields = []
    
    if type == 'acesso': # Dados inválidos no fluxo de acesso
      license_plate = payload.get('license_plate')
      if not isinstance(license_plate, str) or len(license_plate) != 5:
        invalid_fields.append('placa do carro')
      checkin = payload.get('checkin')
      if not isinstance(checkin, str) or len(checkin) != 8:
        invalid_fields.append('hora de entrada')
      checkout = payload.get('checkout')
      if not isinstance(checkout, str) or len(checkout) != 8:
        invalid_fields.append('hora de saída')
    
    elif type == 'estacionamento': # Dados inválidos no cadastro de estacionamento
        fraction_value = payload.get('fraction_value')
        if not isinstance(fraction_value, int) or fraction_value<0:
          invalid_fields.append('valor fração')
        fulltime_value = payload.get('fulltime_value')
        if not isinstance(fulltime_value, int) or fulltime_value<0:
          invalid_fields.append('valor hora cheia')
        daily_value_daytime = payload.get('daily_value_daytime')
        if not isinstance(daily_value_daytime, int) or daily_value_daytime<0:
          invalid_fields.append('valor diária diurna')
        daily_value_overnight = payload.get('daily_value_overnight')
        if not isinstance(daily_value_overnight, int) or daily_value_overnight<0:
          invalid_fields.append('valor diária noturna')
        daily_overnight_initial_hour = payload.get('daily_overnight_initial_hour')
        if not isinstance(daily_overnight_initial_hour, str) or len(daily_overnight_initial_hour) != 8:
          invalid_fields.append('horário inicial da diária noturna')
        daily_overnight_end_hour = payload.get('daily_overnight_end_hour')
        if not isinstance(daily_overnight_end_hour, str) or len(daily_overnight_end_hour) != 8:
          invalid_fields.append('horário final da diária noturna')
        subscription_access_value = payload.get('subscription_access_value')
        if not isinstance(subscription_access_value, int) or subscription_access_value<0:
          invalid_fields.append('valor acesso mensalista')
        event_access_value = payload.get('event_access_value')
        if not isinstance(event_access_value, int) or event_access_value<0:
          invalid_fields.append('valor acesso evento')
        opening_hour = payload.get('opening_hour')
        if not isinstance(opening_hour, str) or len(opening_hour) != 8:
          invalid_fields.append('horário de abertura')
        closing_hour = payload.get('closing_hour')
        if not isinstance(closing_hour, str) or len(closing_hour) != 8:
          invalid_fields.append('horário de fechamento')
        capacity = payload.get('capacity')
        if not isinstance(capacity, int) or capacity<0:
          invalid_fields.append('capacidade do estacionamento')
        contractor_percentage_revenue = payload.get('contractor_percentage_revenue')
        if not isinstance(contractor_percentage_revenue, int) or contractor_percentage_revenue<0:
          invalid_fields.append('valor da porcentagem do contratante')

    self.message = message
    self.invalid_fields = invalid_fields

    super().__init__(self.message)
    
  def __str__(self):
    return f'{self.message} {self.invalid_fields}'