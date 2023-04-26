
# Fibo 
numero = int(input("Digite um número: "))


fibonacci_antecessor = 0
fibonacci_atual = 1


while fibonacci_atual < numero:
    fibonacci_proximo = fibonacci_antecessor + fibonacci_atual
    fibonacci_antecessor = fibonacci_atual
    fibonacci_atual = fibonacci_proximo

if fibonacci_atual == numero:
    print(f"O número {numero} pertence à sequência de Fibonacci!")
else:
 print(f"O número {numero} não pertence à sequência de Fibonacci!")

 # Inversão de Strings

 texto = "Inversão de String Teste"

texto_invertido = texto[::-1]

print(texto_invertido)
