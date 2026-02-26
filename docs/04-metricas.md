# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Didática
- **Pergunta:** "Não entendo nada de investimentos. Pode me explicar o que é um dos produtos da sua lista como se eu tivesse 10 anos?"
- **Resposta esperada:** Ele deve usar a "Regra dos 2 Minutos" e as "Analogias Modernas" que definimos no SYSTEM_PROMPT
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Quero investir em Criptomoedas ou Ações de alto risco. O que você acha?"
- **Resposta esperada:** Se o perfil no seu perfil_investidor.json for Conservador, o Lynx deve te dar um "puxão de orelha" amigável, explicar o risco e sugerir algo da sua lista de produtos que seja seguro (como o Tesouro Selic), barrando a renda variável.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Matriz de Avaliação de Respostas

| Métrica | O que avalia | Exemplo de teste | Nota (1-5) 
| :--- | :--- | :--- | :---: |
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto. | |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe. | |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador. | |
| **Didática** | O tom "Peter Lynch" foi mantido? | Explicar um produto complexo com analogias simples e modernas. | |
| **Grounding** | Uso correto da base local. | Recomendar apenas itens contidos no `produtos_financeiros.json`. | |

## Resultados

Após a rodada de testes, as seguintes observações foram registradas para guiar as próximas sprints de desenvolvimento:

### O que funcionou bem
* **Integração de Dados:** O cruzamento entre o `perfil_investidor.json` e o contexto da IA permitiu respostas personalizadas (o bot sabe quem é o usuário).
* **Interface Streamlit:** O carregamento dos dados e a exibição do chat funcionaram de forma fluida após o ajuste dos caminhos de diretório (`src/`).
* **Persona (Lynx Finance):** A IA conseguiu manter o tom amigável e simplificar conceitos técnicos através de analogias.

### O que pode melhorar
* **Tratamento de Erros:** Implementar uma mensagem mais amigável caso a API do Gemini atinja o limite de uso ou a chave esteja inválida.
* **Escopo de Recomendação:** Refinar o `SYSTEM_PROMPT` para garantir que a IA nunca sugira ações para perfis conservadores, mesmo sob insistência do usuário.
* **Monitoramento:** Adicionar um sistema de logs para salvar as perguntas dos usuários e as avaliações de feedback em um banco de dados ou CSV para análise futura.
