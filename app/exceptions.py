class DescricaoEmBrancoException(Exception):
    def __init__(self, parameter_name):
        self.message = f"{parameter_name} is missing."
        super().__init__(self.message)

  
class ValorAcessoInvalidoException(Exception):
    def __init__(self, field):
        super().__init__(f"Invalid {field} field")
