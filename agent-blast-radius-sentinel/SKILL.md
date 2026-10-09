---
name: agent-blast-radius-sentinel
description: >-
  Use this skill before refactoring, renaming, altering signatures, or modifying shared functions, database models, or core utilities. It evaluates the blast radius across the repository, identifying all callers, dependents, and tests that could break.
---

# Agent Blast Radius Sentinel

O **Agent Blast Radius Sentinel** é uma skill preventiva essencial para evitar regressões e quebras em cascata no projeto. Antes de realizar qualquer alteração estrutural, o agente mapeia o alcance de impacto ("raio de destruição") do símbolo ou módulo afetado.

## Quando Usar

- Antes de renomear funções, métodos ou parâmetros em classes compartilhadas.
- Antes de alterar o tipo de retorno ou assinatura de contratos existentes.
- Antes de refatorar código legado onde testes automatizados podem não ter 100% de cobertura.
- Para gerar relatórios de impacto (como o `legacy-impact.md` do Reversa).

## Procedimento de Execução

1. **Identificar o Símbolo ou Contrato Alvo:**
   Descubra o nome da função, classe, método ou constante que sofrerá alteração (ex: `calculate_discount`, `UserSession`, `IOrderRepository`).

2. **Calcular o Raio de Destruição:**
   Execute a ferramenta auxiliar apontando para a raiz do repositório:
   ```bash
   python "C:/Users/vicenzo.mori/.gemini/config/skills/agent-blast-radius-sentinel/scripts/calc_blast_radius.py" "<caminho_do_repo>" "<nome_do_simbolo>"
   ```

3. **Avaliar Nível de Risco:**
   - **LOW RISK (0 dependentes externos):** Mudança segura e localizada. Prossiga com a implementação normal.
   - **MODERATE RISK (1 a 3 arquivos afetados):** O agente deve atualizar diretamente os arquivos chamadores no mesmo commit e validar com testes.
   - **HIGH RISK (> 3 arquivos afetados):** Risco crítico. O agente deve:
     - Documentar os pontos de quebra antes de alterar o código.
     - Avaliar retrocompatibilidade (ex: manter assinatura legada com `@deprecated` ou criar overload/adaptador).
     - Executar a suíte de testes de todos os módulos dependentes após a edição.
