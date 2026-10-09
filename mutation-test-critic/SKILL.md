---
name: mutation-test-critic
description: >-
  Use this skill after writing or updating automated unit/integration tests to ensure they are robust and not merely "coverage theater". It guides introducing deliberate mutations in the code to verify that the tests fail when logic is corrupted.
---

# Mutation Test Critic

O **Mutation Test Critic** é o antídoto contra o "teatro de testes". Agentes de IA frequentemente escrevem testes superficiais que atingem alta cobertura de linhas (`line coverage`), mas que não contêm asserções rígidas sobre os valores e regras de negócio.

## Quando Usar

- Sempre após escrever uma nova suíte de testes unitários ou de integração.
- Antes de considerar uma funcionalidade ou bugfix como concluído.
- Para validar se um teste de regressão é capaz de capturar o defeito original.

## Procedimento de Execução

1. **Garantir a Linha de Base (Baseline Verde):**
   Execute a suíte de testes original e certifique-se de que todos os testes estão passando:
   ```bash
   pytest / npm test / dotnet test / go test ./...
   ```

2. **Selecionar 2 a 3 Mutantes Críticos:**
   Consulte [references/mutation_strategies.md](./references/mutation_strategies.md) e aplique uma mutação temporária manual ou assistida no arquivo sob teste:
   - *Mutante 1:* Inverter uma condicional chave (ex: trocar `if total >= 100:` por `if total > 100:` ou `if False:`).
   - *Mutante 2:* Trocar o valor de retorno de um cálculo por um valor estático (ex: `return 0` ou `return None`).
   - *Mutante 3:* Remover a chamada de persistência ou disparo de evento.

3. **Executar os Testes contra o Mutante:**
   Rode os testes novamente:
   - **Cenário Esperado (Mutante Eliminado ✅):** A suíte de testes FALHA acusando exatamente a lógica alterada.
   - **Cenário de Falha do Teste (Mutante Sobreviveu ❌):** Se todos os testes continuarem PASSANDO mesmo com a lógica corrompida, os testes são frágeis e insuficientes!

4. **Reforçar as Asserções:**
   Caso o mutante sobreviva:
   - Adicione asserções específicas para casos de borda (*boundary cases*).
   - Verifique efeitos colaterais e estados mutados.
   - Reverta a mutação temporária e confirme que a suíte volta a ficar 100% verde com asserções fortes.
