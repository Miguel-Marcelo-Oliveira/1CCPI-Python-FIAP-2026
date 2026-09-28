from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("Paulo", "123456", "Ciência da Computação")

# criar / instanciar 2 disciplinas
model_lin = Disciplina("Modelagem Linear", "Rodolfo")
dsa = Disciplina("Data Structures and Algorithms", "Erick")

# matricular o aluno1 nas duas disciplinas
aluno1.matricular(model_lin)
aluno1.matricular(dsa)

# adicionar notas do aluno referente a cada disciplina
aluno1.adicionar_nota(model_lin, 10)
aluno1.adicionar_nota(model_lin, 6)
aluno1.adicionar_nota(dsa, 5)
aluno1.adicionar_nota(dsa, 4)

# print(aluno1.media_por_d(model_lin))
# print(aluno1.media_por_d(dsa))
print(aluno1.media_geral())

# FAZER UM MÉTODO DE EXIBIR BOLETIM
