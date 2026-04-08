cont = 1
total = 0

while cont <= 15:
    n = int(input(f"Digite o {cont}° número: "))
    if n % 2 != 0:
        total += n         # total = total + n
    cont += 1              # cont = cont + 1 
    
print(f"A soma de todos os ímpares é {total}.")