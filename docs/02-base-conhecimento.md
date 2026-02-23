# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve no Lynch |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e ajudar a dar continuidade ao atendimento |
| `perfil_investidor.json` | JSON | Personalizar recomendações com base no perfil do investidor |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |

- Datasets públicos do Hugging Face, como:
  - **Financial Phrasebank**: frases financeiras para treinar explicações educativas.  
  - **FinanceBench**: perguntas e respostas financeiras para simular interações educativas.  

---

## Adaptações nos Dados

# Alterações no produtos_financeiros.json

## Novos produtos adicionados
| Produto                     | Categoria       |
|-----------------------------|-----------------|
| LCI                         | renda_fixa      |
| Ações                       | renda_variavel  |
| Fundos Imobiliários (FIIs)  | renda_variavel  |
| ETFs                        | renda_variavel  |
| Fundos Multimercado         | fundos          |
| Previdência Privada (PGBL/VGBL) | previdencia |
| Criptomoedas                | alternativos    |
| Commodities                 | alternativos    |

## Atualização dos aportes mínimos
| Produto                     | Aporte mínimo (R$) | Observação                          |
|-----------------------------|--------------------|-------------------------------------|
| Tesouro Selic               | 30,00              | Valor oficial do Tesouro Direto     |
| CDB                         | 1.000,00           | Média em bancos                     |
| LCI/LCA                     | 1.000,00           | Carência mínima de 9 meses          |
| Ações                       | ~10,00             | Valor médio por cota                |
| Fundos Imobiliários (FIIs)  | ~10,00             | Valor médio por cota                |
| ETFs                        | ~50,00             | Valor médio por cota                |
| Fundos Multimercado         | 500,00             | Média de entrada em fundos          |
| Previdência Privada (PGBL/VGBL) | 100,00         | Média de planos                     |
| Criptomoedas                | ~50,00             | Exchanges permitem valores baixos   |
| Commodities                 | ~100,00            | Ex.: ouro em corretoras             |

## Categorias expandidas
| Categoria       | Exemplos incluídos                          |
|-----------------|---------------------------------------------|
| renda_fixa      | Tesouro Selic, CDB, LCI/LCA                 |
| renda_variavel  | Ações, FIIs, ETFs                           |
| fundos          | Fundos Multimercado                         |
| previdencia     | PGBL, VGBL                                  |
| alternativos    | Criptomoedas, Commodities                   |

## Resumo
O arquivo foi expandido para incluir mais produtos financeiros, com aportes mínimos atualizados conforme valores médios de mercado em 2026 e categorias mais detalhadas para organização.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades que é injetar diretamente no prompt (CTRL + C, CTRL V) ou carregar os arquivos via código

```python
import pandas as pd
import json

# Carregando o histórico de atendimento (CSV)
historico = pd.read_csv('historico_atendimento.csv')

# Carregando o perfil do investidor (JSON)
with open('perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

# Carregando o catálogo de produtos financeiros (JSON)
with open('produtos_financeiros.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, garantindo que a gente tenha o melhor contexto possível. Lembrando que em soluções mais robustas, o ideal é que essas informações sejam carregas dinamicamente para que possamos ganhar flexibilidade.

```text
PERFIL DO INVESTIRO: data/perfil_investidor.json
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

HISTÓRICO DE ATENDIMENTO: data/historico_atendimento.csv
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS FINANCEIROS: data/produtos_financeiros.json
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "varia conforme emissor, geralmente próximo à Selic",
    "aporte_minimo": 1000.00,
    "indicado_para": "Investidores iniciantes e objetivos de curto a médio prazo"
  },
  {
    "nome": "LCI",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "atrelada ao CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Investidores que buscam isenção de IR e segurança"
  },
  {
    "nome": "Ações",
    "categoria": "renda_variavel",
    "risco": "alto",
    "rentabilidade": "varia conforme desempenho da empresa e mercado",
    "aporte_minimo": 10.00,
    "indicado_para": "Investidores experientes e objetivos de longo prazo"
  },
  {
    "nome": "Fundos Imobiliários (FIIs)",
    "categoria": "renda_variavel",
    "risco": "moderado",
    "rentabilidade": "distribuição de rendimentos e valorização das cotas",
    "aporte_minimo": 10.00,
    "indicado_para": "Investidores que buscam renda passiva e diversificação"
  },
  {
    "nome": "ETFs",
    "categoria": "renda_variavel",
    "risco": "moderado",
    "rentabilidade": "replica índices de mercado",
    "aporte_minimo": 50.00,
    "indicado_para": "Investidores que buscam diversificação com baixo custo"
  },
  {
    "nome": "Fundos Multimercado",
    "categoria": "fundos",
    "risco": "variável",
    "rentabilidade": "depende da estratégia do gestor",
    "aporte_minimo": 500.00,
    "indicado_para": "Investidores que aceitam risco moderado e diversificação"
  },
  {
    "nome": "Previdência Privada (PGBL/VGBL)",
    "categoria": "previdencia",
    "risco": "variável",
    "rentabilidade": "depende do fundo escolhido",
    "aporte_minimo": 100.00,
    "indicado_para": "Planejamento de aposentadoria e longo prazo"
  },
  {
    "nome": "Criptomoedas",
    "categoria": "alternativos",
    "risco": "alto",
    "rentabilidade": "alta volatilidade, depende do mercado",
    "aporte_minimo": 50.00,
    "indicado_para": "Investidores que aceitam risco elevado e buscam inovação"
  },
  {
    "nome": "Commodities",
    "categoria": "alternativos",
    "risco": "moderado",
    "rentabilidade": "varia conforme preço internacional",
    "aporte_minimo": 100.00,
    "indicado_para": "Proteção contra inflação e diversificação"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O contexto mostrado abaixo se baseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relevantes, otimizando assim o consumo de tokens. Entretanto vale lembrar que mais importante do que economizar tokens é ter todas as informações relevantes disponíveis em seu contexto.

```
DADOS DO CLIENTE:
- **Nome:** João Silva
- **Perfil de Risco:** Moderado
- **Saldo Atual:** R$ 5.500,00

HISTÓRICO RECENTE (Últimas 3 interações):
1. Usuário: "Como começar a investir com pouco dinheiro?"
2. Lynch: "Você pode começar pelo Tesouro Direto com apenas R$ 30,00."
3. Usuário: "E se eu tiver 5 mil reais hoje?"

PRODUTOS RECOMENDADOS (Filtrados por Saldo e Perfil):
- [Renda Fixa] Tesouro Selic - Mínimo: R$ 30,00
- [Renda Fixa] CDB Bancário - Mínimo: R$ 1.000,00
- [Renda Fixa] LCI (Isento de IR) - Mínimo: R$ 1.000,00
- [Fundos] Fundo Multimercado Estável - Mínimo: R$ 500,00

DIRETRIZES DE RESPOSTA:
- Use um tom educativo e profissional.
- Priorize a reserva de emergência se o histórico indicar que o cliente está começando.
- NÃO sugira produtos de Renda Variável, pois o perfil é Moderado e o saldo é inicial.
...
```
