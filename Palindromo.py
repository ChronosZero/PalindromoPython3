#Verificação de palavas ou frases sao palindromos

palindromo = input('Digite uma palavra: ')

palindromo = ''.join(palindromo.lower().split())
inverso = palindromo[::-1]

if palindromo == inverso:
    print('A Palavra/frase digitada é um palindromo')
else:
    print('A palavra/frase digitada nao é um paalindromo')