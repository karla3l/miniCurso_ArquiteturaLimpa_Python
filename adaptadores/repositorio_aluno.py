class RepositorioAluno:
    def __init__(self):
        self.alunos = {}

    def obter_aluno(self, nome):
        return self.alunos.get(nome)

    def salvar_aluno(self, aluno):
        self.alunos[aluno.nome] = aluno