#tipos primitivos e saidas de dados

n1=int(input("Digite um numero: "))
print(type(n1))


n2=int(input("Digite outro numero: "))
print(type(n2))

s=n1+n2
media=s/2

print('A soma entre {} e {} vale {}'.format(n1,n2,s))
print('A media entre {} e {} vale {}'.format(n1,n2,media))

#testes de tipos
n3=input("Digite um numero de teste: ")
print(type(n3))
print(n3.isnumeric())
print(n3.isalnum())
print(n3.isalpha()) #alphabetic
print(n3.isdecimal())

text=input("Digite uma palavra: ")
print(text.isspace())
print(text.isupper())
print(text.islower())