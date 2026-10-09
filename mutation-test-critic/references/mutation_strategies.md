# Mutation Testing Strategies for Coding Agents

O teste de mutação expõe falhas na qualidade dos testes unitários ao introduzir intencionalmente defeitos artificiais ("mutantes") no código de produção. Se a suíte de testes do agente continuar passando após a mutação, o teste é considerado **fraco** (o mutante sobreviveu). Se o teste falhar, o teste é considerado **forte** (o mutante foi eliminado).

## Operadores de Mutação Principais

### 1. Inversão Relacional (Conditional Boundary Mutants)
Substituir operadores de comparação nos limites:
- `>` por `>=` ou `<`
- `<` por `<=` ou `>`
- `==` por `!=`
- `>=` por `>`
*Exemplo de Falha de Teste:* O teste testa apenas o caso típico, mas ignora o valor de fronteira (`if x > 10` onde `x = 10`).

### 2. Mutação Lógica (Boolean Logic Mutants)
- Substituir `and` / `&&` por `or` / `||`.
- Inverter flags booleanas (`return not is_valid`).
- Trocar `True` por `False`.

### 3. Remoção de Efeitos Colaterais (Void Method Call Deletion)
- Comentar chamadas de métodos void/sem retorno (ex: salvar em log, disparar evento de telemetria, chamar commit de transação).
*Exemplo de Falha de Teste:* O teste usa mock e não verifica se o método colateral foi invocado (`verify` ou `assert_called_once`).

### 4. Mutação Aritmética (Math Mutants)
- Trocar `+` por `-`.
- Trocar `*` por `/`.
- Substituir incrementos (`+= 1` por `+= 0` ou `-= 1`).

### 5. Substituição de Retorno (Return Value Mutation)
- Substituir valores de retorno por `None`, `null`, `""`, `0` ou lista vazia `[]`.
