import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Gerar um conjunto de dados fictício
np.random.seed(0)
n_records = 100000  # Simular 100 mil registros
dates = pd.date_range(start='2024-01-01', periods=n_records, freq='T')  # Datas por minuto
amounts = np.random.exponential(scale=50, size=n_records)  # Transações com distribuição exponencial
categories = np.random.choice(['Eletronicos', 'Roupas', 'Compras', 'Casa'], size=n_records)  # Categorias

# Criar um DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Amount': amounts,
    'Category': categories
})

# Visualizar as primeiras linhas do DataFrame
print(data.head())

# Análise: total gasto por categoria
category_totals = data.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print("\nTotal gasto por categoria:")
print(category_totals)

# Visualização: gráfico de barras do total gasto por categoria
plt.figure(figsize=(10, 6))
category_totals.plot(kind='bar', color='skyblue')
plt.title('Total Gasto por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Total Gasto (em Reais)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Análise: média de gasto por dia
data['Date'] = data['Date'].dt.date  # Extrair apenas a data (sem hora)
daily_totals = data.groupby('Date')['Amount'].sum()
daily_totals = daily_totals.rolling(window=7).mean()  # Média móvel de 7 dias

# Visualização: gráfico da média móvel de gastos diários
plt.figure(figsize=(12, 6))
daily_totals.plot(color='green')
plt.title('Média Móvel de Gasto Diário')
plt.xlabel('Data')
plt.ylabel('Gasto Médio (em Reais)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
