class Aluno:
    def __init__(self, nome, notas=None):
        self.nome = nome
        self.notas = notas or []
        self.aprovado = None