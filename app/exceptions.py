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
      if not 'value_daytime' in payload:
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