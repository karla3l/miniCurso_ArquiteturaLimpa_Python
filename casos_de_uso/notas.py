from adaptadores.repositorio_aluno import RepositorioAluno
from entidades.aluno import Aluno
class GerenciarNotas:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def adicionar_nota(self, nome_aluno, nota):
        aluno = self.repositorio.obter_aluno(nome_aluno)
        if aluno is None:
            aluno = Aluno(nome_aluno)
        aluno.notas.append(nota)
        self.repositorio.salvar_aluno(aluno)

    def remover_nota(self, nome_aluno, nota):
        aluno = self.repositorio.obter_aluno(nome_aluno)
        if nota in aluno.notas:
            aluno.notas.remove(nota)
            self.repositorio.salvar_aluno(aluno)

    def calcular_aprovacao(self, nome_aluno, nota_minima=6):
        aluno = self.repositorio.obter_aluno(nome_aluno)
        media = sum(aluno.notas) / len(aluno.notas)
        aluno.aprovado = media >= nota_minima
        self.repositorio.salvar_aluno(aluno)
        return aluno.aprovado
