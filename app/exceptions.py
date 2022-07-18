class DescricaoEmBrancoException(Exception):
  def __init__(self, payload, type, message='Dados obrigatórios em branco:'):
    blank_fields = []
    
    if type == 'acesso': # Dados em branco no fluxo de acesso
      if not payload.license_plate:
        blank_fields.append('placa do carro')
      if not payload.checkin:
        blank_fields.append('hora de entrada')
      if not payload.checkout:
        blank_fields.append('hora de saída')
    
    elif type == 'estacionamento': # Dados em branco no cadastro de estacionamento
      if not payload.name:
        blank_fields.append('nome do estacionamento')
      if not payload.opening_hour or not payload.closing_hour:
        blank_fields.append('horário de funcionamento')
      if not payload.fraction_value:
        blank_fields.append('valor fração')
      if not payload.fulltime_value:
        blank_fields.append('valor hora cheia')
      if not payload.daily_value_daytime:
        blank_fields.append('valor diária diurna')
      if not payload.daily_value_overnight:
        blank_fields.append('valor diária noturna')
      if not payload.subscription_access_value:
        blank_fields.append('valor acesso mensalista')
      if not payload.event_access_value:
        blank_fields.append('valor acesso evento')
      if not payload.daily_overnight_initial_hour or not payload.daily_overnight_end_hour:
        blank_fields.append('horário da diária noturna')
      if not payload.contractor_percentage_revenue:
        blank_fields.append('valor da porcentagem do contratante')
      if not payload.capacity:
        blank_fields.append('capacidade do estacionamento')

    self.message = message
    self.blank_fields = blank_fields

    super().__init__(self.message)
    
  def __str__(self):
    return f'{self.message} {self.blank_fields}'