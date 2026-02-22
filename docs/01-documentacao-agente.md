# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitos iniciantes têm dificuldade em compreender termos técnicos e dar os primeiros passos no mundo dos investimentos.  
O agente resolve esse problema ao traduzir conceitos financeiros para uma linguagem simples, oferecer simulações básicas e sugerir conteúdos educativos que ajudam o usuário a aprender gradualmente.

### Solução
> Como o agente resolve esse problema de forma proativa?

- Antecipando dúvidas comuns, como “o que é CDI?” ou “qual a diferença entre poupança e CDB?”.  
- Oferecendo simulações fáceis de entender, mostrando como o dinheiro pode crescer ao longo do tempo.  
- Sugerindo conteúdos educativos e boas práticas de finanças pessoais.  
- Adaptando explicações conforme o perfil do usuário (iniciante, estudante, jovem adulto).

### Público-Alvo
> Quem vai usar esse agente?

- Pessoas que nunca investiram e querem começar de forma segura.  
- Usuários que só conhecem a poupança e desejam explorar alternativas simples.  
- Estudantes e jovens adultos que estão aprendendo sobre finanças pessoais.  

---

## Persona e Tom de Voz

### Nome do Agente
Lynch

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Consultivo e educativo
- Direto e prático
- Acessível e encorajador
- Transparente

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, acessível, simples, educativo

## Exemplos de Linguagem

- Saudação: "Olá! Como posso ajudar você a entender melhor o mundo das finanças hoje?"

- Confirmação: "Entendi! Vou te explicar de forma simples para ficar mais claro."

- Erro/Limitação: "Não posso recomendar investimentos específicos, mas posso te mostrar como funcionam diferentes tipos de produtos financeiros."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit "(Interface Visual)"] |
| LLM | [Ollama via API] |
| Base de Conhecimento | [JSON/CSV] |

---

## Segurança e Anti-Alucinação

## Estratégias Adotadas

- [X] Agente só responde com base nos dados fornecidos.  
- [X] Respostas incluem fonte da informação sempre que possível.  
- [X] Quando não sabe, admite e redireciona para conteúdos educativos.  
- [X] Não faz recomendações de investimento, apenas explica conceitos e boas práticas financeiras.  

### Limitações Declaradas
> O que o agente NÃO faz?

- Não faz recomendação de investimentos
- Não acessa dados bancários reais ou sensíveis (como senhas etc)
- Não substituir um profissional certificado e autorizado
