  

nome = str(input("Digite o seu nome completo: "))
curso = input ("Digite seu curso: ")
disciplina = input("Digite a disciplina que você estudou: ")
idade = int(input("Digite sua idade: "))

nota1 = float (input("Digite sua primeira nota: "))
nota2 = float (input("Digite sua segunda nota: "))

media = ( nota1 + nota2 ) / 2 
aprove = "Reprovado(a)" if media < 6 else "Aprovado(a)"

print(f"Seu nome é: {nome}.")
print(f"Você esta matriculado no curso: {curso}.") 
print(f"Disciplina realizada: {disciplina}.") 
print(f"Sua média é: {media:.2f}.") 
print(f"Você está {aprove}.") 



