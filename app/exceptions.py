class DescricaoEmBrancoException(Exception):
  def __init__(self, payload, type, message='Dados obrigatórios em branco:'):
    blank_fields = []
    
    if type == 'acesso': # Dados em branco no fluxo de acesso
      if not 'license_plate' in payload:
        blank_fields.append('placa do carro')
      if not 'checkin' in payload:
        blank_fields.append('hora de entrada')
      if not 'checkout' in payload:
        blank_fields.append('hora de saída')
    
    elif type == 'estacionamento': # Dados em branco no cadastro de estacionamento
      if not 'name' in payload:
        blank_fields.append('nome do estacionamento')
      if not 'opening_hour' in payload or not 'closing_hour' in payload:
        blank_fields.append('horário de funcionamento')
      if not 'fraction_value' in payload:
        blank_fields.append('valor fração')
      if not 'fulltime_value' in payload:
        blank_fields.append('valor hora cheia')
      if not 'daily_value_daytime' in payload:
        blank_fields.append('valor diária diurna')
      if not 'daily_value_overnight' in payload:
        blank_fields.append('valor diária noturna')
      if not 'subscription_access_value' in payload:
        blank_fields.append('valor acesso mensalista')
      if not 'event_access_value' in payload:
        blank_fields.append('valor acesso evento')
      if not 'daily_overnight_initial_hour' in payload or not 'daily_overnight_end_hour' in payload:
        blank_fields.append('horário da diária noturna')
      if not 'contractor_percentage_revenue' in payload:
        blank_fields.append('valor da porcentagem do contratante')
      if not 'capacity' in payload:
        blank_fields.append('capacidade do estacionamento')

    self.message = message
    self.blank_fields = blank_fields

    super().__init__(self.message)
    
  def __str__(self):
    return f'{self.message} {self.blank_fields}'
  
class ValorAcessoInvalidoException(Exception):
  def __init__(self, payload, type, message='Dados de acesso inválidos:'):
    invalid_fields = []
    
    if type == 'acesso': # Dados em branco no fluxo de acesso
      license_plate = payload.get('license_plate')
      if type(license_plate) != str or len(license_plate) != 5:
        invalid_fields.append('placa do carro')
      checkin = payload.get('checkin')
      if type(checkin) != str or len(checkin) != 8:
        invalid_fields.append('hora de entrada')
      checkout = payload.get('checkout')
      if type(checkout) != str or len(checkout) != 8:
        invalid_fields.append('hora de saída')
    
    elif type == 'estacionamento': # Dados em branco no cadastro de estacionamento
        fraction_value = payload.get('fraction_value')
        if type(fraction_value) != int or fraction_value<0:
          invalid_fields.append('valor fração')
        fulltime_value = payload.get('fulltime_value')
        if type(fulltime_value) != int or fulltime_value<0:
          invalid_fields.append('valor hora cheia')
        daily_value_daytime = payload.get('daily_value_daytime')
        if type(daily_value_daytime) != int or daily_value_daytime<0:
          invalid_fields.append('valor diária diurna')
        daily_value_overnight = payload.get('daily_value_overnight')
        if type(daily_value_overnight) != int or daily_value_overnight<0:
          invalid_fields.append('valor diária noturna')
        daily_overnight_initial_hour = payload.get('daily_overnight_initial_hour')
        if type(daily_overnight_initial_hour) != int or daily_overnight_initial_hour<0:
          invalid_fields.append('horário inicial da diária noturna')
        daily_overnight_end_hour = payload.get('daily_overnight_end_hour')
        if type(daily_overnight_end_hour) != int or daily_overnight_end_hour<0:
          invalid_fields.append('horário final da diária noturna')
        subscription_access_value = payload.get('subscription_access_value')
        if type(subscription_access_value) != int or subscription_access_value<0:
          invalid_fields.append('valor acesso mensalista')
        event_access_value = payload.get('event_access_value')
        if type(event_access_value) != int or event_access_value<0:
          invalid_fields.append('valor acesso evento')
        opening_hour = payload.get('opening_hour')
        if type(opening_hour) != int or opening_hour<0:
          invalid_fields.append('horário de abertura')
        closing_hour = payload.get('closing_hour')
        if type(closing_hour) != int or closing_hour<0:
          invalid_fields.append('horário de fechamento')
        capacity = payload.get('capacity')
        if type(capacity) != int or capacity<0:
          invalid_fields.append('capacidade do estacionamento')
        contractor_percentage_revenue = payload.get('contractor_percentage_revenue')
        if type(contractor_percentage_revenue) != int or contractor_percentage_revenue<0:
          invalid_fields.append('valor da porcentagem do contratante')

    self.message = message
    self.invalid_fields = invalid_fields

    super().__init__(self.message)
    
  def __str__(self):
    return f'{self.message} {self.invalid_fields}'