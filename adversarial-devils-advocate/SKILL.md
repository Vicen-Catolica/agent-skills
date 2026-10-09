---
name: adversarial-devils-advocate
description: >-
  Use this skill during the planning or design phase, before writing code or finalizing a technical architecture. It assumes the role of a skeptical adversarial critic to stress-test the proposal against edge-cases, race conditions, memory leaks, security holes, and failure modes.
---

# Adversarial Devil's Advocate

O **Adversarial Devil's Advocate** é uma skill projetada para eliminar o viés do "caminho feliz" (*happy path bias*). Agentes de IA tendem a desenhar soluções que funcionam perfeitamente sob condições ideais, mas que quebram facilmente sob concorrência, timeouts ou dados inesperados.

## Quando Usar

- Após elaborar um `plan.md`, `roadmap.md` ou proposta de arquitetura.
- Antes de iniciar a implementação de tarefas críticas (pagamentos, autenticação, migrações de dados, concorrência).
- Quando o usuário pedir: "revise este plano", "encontre potenciais falhas", ou "faça uma auditoria de risco".

## Procedimento de Execução

1. **Assumir a Persona Adversária:**
   Suspenda temporariamente a postura de concordância. O seu objetivo deliberado nesta etapa é **encontrar defeitos, cenários de falha e premissas frágeis** na proposta.

2. **Aplicar o Checklist de Estresse:**
   Avalie a proposta contra os 5 eixos de [references/adversarial_checklist.md](./references/adversarial_checklist.md):
   - Concorrência e *race conditions*.
   - Falhas parciais e quedas de rede/dependências.
   - Vazamentos de memória e recursos.
   - Brechas de segurança e validação de entrada.
   - Degradação sob alta volumetria (N+1 queries).

3. **Gerar o Relatório de Riscos (Devil's Advocate Report):**
   Apresente o resultado em três seções diretas:
   - **Vulnerabilidades Críticas (Showstoppers):** Problemas que fatalmente quebrarão o sistema em produção se não forem tratados no plano antes da codificação.
   - **Cenários de Borda Não Tratados (Edge Cases):** Situações raras ou limites que necessitam de regras de fallback explícitas.
   - **Recomendações de Mitigação:** Ações concretas a serem incorporadas no `actions.md` antes de bater o martelo.
