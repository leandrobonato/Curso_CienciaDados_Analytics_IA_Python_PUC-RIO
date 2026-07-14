import plotly.express as px
import pandas as pd

# 🔹 Executa a consulta SQL
df = spark.sql("""
WITH ultimos_25_anos AS (
  SELECT 
    p.id_pais,
    a.ano,
    p.pib_pais
  FROM workspace.pucrio.PIB_PAIS p
  JOIN workspace.pucrio.ano a ON p.ID_ANO = a.id_ano
  WHERE a.ano BETWEEN 2000 AND 2024
    AND p.pib_pais IS NOT NULL
    AND p.pib_pais > 0
),
media_pib AS (
  SELECT 
    id_pais,
    AVG(pib_pais) AS pib_medio
  FROM ultimos_25_anos
  GROUP BY id_pais
  ORDER BY pib_medio DESC
  LIMIT 10
)
SELECT 
  u.id_pais,
  pa.nome_pais,
  u.ano,
  u.pib_pais
FROM ultimos_25_anos u
JOIN media_pib m ON u.id_pais = m.id_pais
JOIN workspace.pucrio.pais pa ON u.id_pais = pa.id_pais
ORDER BY m.pib_medio DESC, u.ano
""").toPandas()

# 🔹 Verificação
if df.empty:
    raise ValueError("⚠️ Nenhum dado encontrado em PIB_PAIS para 2000–2024.")
print(f"✅ Top 10 países carregados | Anos: {df['ano'].min()}–{df['ano'].max()}")

# ✅ Gráfico interativo: linhas por país, eixo Y = PIB (USD)
fig = px.line(
    df,
    x='ano',
    y='pib_pais',
    color='nome_pais',
    title='<b>Top 10 Maiores Economias (PIB nominal em USD) — 2000–2024</b>',
    labels={
        'ano': 'Ano',
        'pib_pais': 'PIB (USD)',
        'nome_pais': 'País'
    },
    height=700,
    markers=True
)

# 🔧 Melhorias de layout
fig.update_layout(
    hovermode='x unified',
    legend_title='País',
    legend=dict(
        orientation='v',
        yanchor='top',
        y=1.0,
        xanchor='left',
        x=1.02,
        font=dict(size=10)
    ),
    xaxis=dict(dtick=2),
    yaxis=dict(
        title='PIB (USD)',
        tickformat='$,.0f',  # ex: $2,000,000,000,000
        rangemode='tozero'
    ),
    margin=dict(l=60, r=200, t=70, b=60)
)

# ✅ Exibir
fig.show()