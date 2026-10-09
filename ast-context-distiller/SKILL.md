---
name: ast-context-distiller
description: >-
  Use this skill whenever you need to inspect large code files, dependencies, or modules to understand their public API, signatures, classes, or types without consuming excess tokens. It extracts the AST interface skeleton and strips internal implementation bodies.
---

# AST Context Distiller

O **AST Context Distiller** é uma skill projetada para economizar de 70% a 90% de tokens ao navegar por grandes bases de código. Em vez de ler centenas de linhas de lógica de implementação que o agente não precisa editar, ele gera um esqueleto com tipos, assinaturas, contratos e docstrings.

## Quando Usar

- Ao inspecionar arquivos com mais de 100 linhas apenas para entender "como chamar" uma função ou classe.
- Ao mapear contratos de módulos vizinhos antes de escrever novos recursos ou testes.
- Quando o contexto da conversa estiver próximo do limite de tokens e você precisar preservar memória de trabalho.

## Procedimento de Execução

1. **Identificar os Arquivos de Dependência:**
   Localize os arquivos que você precisa entender (ex: `services/payment.py`, `models/user.ts`).

2. **Executar o Destilador AST:**
   Execute o script auxiliar via terminal:
   ```bash
   python "C:/Users/vicenzo.mori/.gemini/config/skills/ast-context-distiller/scripts/distill_ast.py" <caminho_do_arquivo>
   ```

3. **Interpretar a Interface:**
   - Utilize as assinaturas (`def`, `async def`, `class`, `interface`, tipos de retorno) para compor suas chamadas.
   - Não leia o corpo do arquivo a menos que precise alterar sua implementação interna diretamente.

4. **Regras de Poda:**
   - Corpos de funções são substituídos por `pass` ou omitidos.
   - Docstrings essenciais e anotações de tipo são preservadas para orientar o uso correto.
