from adaptadores.repositorio_aluno import RepositorioAluno
from casos_de_uso.notas import GerenciarNotas

def main():
    repositorio = RepositorioAluno()
    gerenciador = GerenciarNotas(repositorio)

    nome_aluno = 'João'
    notas = [8.5, 7.0, 9.0]
    for nota in notas:
        gerenciador.adicionar_nota(nome_aluno, nota)

    gerenciador.remover_nota(nome_aluno, 7.0)

    aprovado = gerenciador.calcular_aprovacao(nome_aluno)
    status = 'aprovado' if aprovado else 'reprovado'
    print(f'O aluno {nome_aluno} foi {status}.')

    aluno = repositorio.obter_aluno(nome_aluno)
    print(f'Notas do aluno {aluno.nome}: {aluno.notas}')
    print(f'Status: {"Aprovado" if aluno.aprovado else "Reprovado"}')
    print("Aulas concluídas com sucesso!")

if __name__ == '__main__':
    main()