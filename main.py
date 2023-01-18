
''' Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:


Lista1 = Funcionarios que tem carro e trabalham a noite
Lista2 = Funcionarios que tem carro e trabalham durante o dia
Lista3 = Funcionarios que não tem carro
'''

funcionarios = ['Ana', 'Marcos','Alice', 'Pedro', 'Sofia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sofia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

Lista1 = set(funcionarios)
Lista2 = set(turno_dia)
Lista3 = set(turno_noite)
Lista4 = set(tem_carro)

print(Lista3 & Lista4)
print(Lista2 & Lista4)
print(Lista1 - Lista4)