total = 0
for i in range(2):
    item = input().split(" ")
    cod = int(item[0])
    quant = int(item[1])
    valor = float(item[2])
    total += quant * valor

print(f"VALOR A PAGAR: R$ {total:.2f}")