import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('dados_financeiros.csv')

# Criar coluna de lucro
df['lucro'] = df['receita'] - df['despesas']

# Calcular totais
receita_total = df['receita'].sum()
despesa_total = df['despesas'].sum()
lucro_total = df['lucro'].sum()

# Exibir resumo no terminal
print("=== RELATÓRIO FINANCEIRO ===")
print(f"Receita Total: R$ {receita_total}")
print(f"Despesas Totais: R$ {despesa_total}")
print(f"Lucro Total: R$ {lucro_total}")

# Salvar novo arquivo com os resultados
df.to_csv('relatorio_final.csv', index=False)

print("\nRelatório gerado com sucesso: relatorio_final.csv")