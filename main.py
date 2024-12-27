nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
nota1 = float (input  ("Digite sua primeira nota: "))
nota2 = float (input  ("Digite sua segunda nota2: "))
media = ( nota1 + nota2 ) / 2 
aprove = "Reprovado" if media < 6 else "Aprovado"
print(f"Seu nome é {nome}, \nSua média é {media:.2f}. \nVocê está {aprove}." ) 
