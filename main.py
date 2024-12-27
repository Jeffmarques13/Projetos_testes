    
    nome = str (input("Digite o seu nome completo: "))
    curso = input ("Digite seu curso: ")
    disciplina = input("Digite a disciplina que você estudou: ")
    idade = int (input("Digite sua idade: "))

    nota1 = float (input  ("Digite sua primeira nota: "))
    nota2 = float (input  ("Digite sua segunda nota: "))

    media = ( nota1 + nota2 ) / 2 
    aprove = "Reprovado(a)" if media < 6 else "Aprovado(a)"

print(f"
      Seu nome é: {nome}. 
      Você esta matriculado no curso: {curso}. 
      Disciplina realizada: {disciplina}. 
      Sua média é: {media:.2f}. 
      Você está {aprove}." ) 



