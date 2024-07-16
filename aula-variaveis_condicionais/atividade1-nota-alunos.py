import sys

nome = input("Qual o seu nome? ")
try:
  total_notas = int(input("Quantas notas você deseja somar? "))
except ValueError:
  print("Por favor, utilize apenas números!")
  sys.exit()

notas = []
try:
  for i in range(total_notas):
    notas.append(int(input(f"Qual a nota {i+1}? ")))
except ValueError:
  print("Por favor, utilize apenas números!")
  sys.exit()

total = 0
for nota in notas:
  total += nota

print(f"Olá {nome.capitalize()}, sua média é {total/total_notas}.")