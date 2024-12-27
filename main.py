  
# Entrada dos dados pessoais
nome = str(input("Digite o seu nome completo: "))
curso = input("Digite seu curso: ")
disciplina = input("Digite a disciplina que você estudou: ")
escola = input("Digite o nome da escola: ")
idade = int(input("Digite sua idade: "))



# Entrada das notas do aluno
nota1 = float (input("Digite sua primeira nota: "))
nota2 = float (input("Digite sua segunda nota: "))

# Calculo da média das notas do aluno e aprovação
media = ( nota1 + nota2 ) / 2 
aprove = "Reprovado(a)" if media < 6 else "Aprovado(a)"

# Saída formatada apenas se não houver erros
print(f"Seu nome é: {nome}.")
print(f"Você esta matriculado no curso: {curso}.") 
print(f"Disciplina realizada: {disciplina}.") 
print(f"A escola que você estou é: {escola}.")
print(f"Sua média é: {media:.2f}.") 
print(f"Você está {aprove}.") 



