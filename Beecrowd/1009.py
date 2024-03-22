nome = str(input())
salario_fixo = float(input())
valor_total_vendas = float(input())

salario_bonificado = salario_fixo + ((valor_total_vendas * 15) / 100)

print(f"TOTAL = R$ {salario_bonificado:.2f}")