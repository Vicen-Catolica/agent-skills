---
name: supply-chain-typosquatting-auditor
description: >-
  Use this skill before running any package manager installation command (such as pip install, npm install, cargo add, dotnet add package) or modifying requirements.txt/package.json. It verifies that packages are legitimate, not hallucinated by the LLM, and not typosquatting attacks.
---

# Supply Chain & Typosquatting Auditor

Esta skill protege o ambiente contra dois dos maiores riscos de segurança associados ao uso de agentes de IA: **alucinação de pacotes** e ataques de **typosquatting** (quando invasores criam bibliotecas maliciosas com nomes intencionalmente parecidos com bibliotecas famosas).

## Quando Usar

- Sempre antes de propor ou executar comandos `pip install <pacote>`, `npm install <pacote>`, etc.
- Ao adicionar novas bibliotecas a arquivos de manifesto (`package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`).
- Quando você estiver em dúvida se um nome de biblioteca realmente existe ou se foi gerado por inferência probabilística.

## Procedimento de Execução

1. **Auditar o Nome do Pacote:**
   Execute o script de verificação de integridade no terminal:
   ```bash
   python "C:/Users/vicenzo.mori/.gemini/config/skills/supply-chain-typosquatting-auditor/scripts/audit_package.py" "<nome_do_pacote>" "<ecossistema: python|npm>"
   ```

2. **Interpretar os Resultados da Auditoria:**
   - **`[ALERT: POTENTIAL TYPOSQUATTING DETECTED!]`:**
     - **Interrompa a instalação imediatamente!**
     - Verifique se você não digitou ou gerou uma variante errada (ex: `requsts` em vez de `requests`, `colorma` em vez de `colorama`).
   - **`[DANGER: PACKAGE NOT FOUND ON PYPI/NPM!]`:**
     - O pacote não existe no repositório público oficial.
     - **Nunca tente instalar.** Pesquise o nome correto da biblioteca padrão da linguagem ou da biblioteca desejada antes de prosseguir.
   - **`[OK: OFFICIAL PACKAGE VERIFIED]`:**
     - O pacote é legítimo, tem autor conhecido e versão válida. Prossiga com a instalação segura.

3. **Boas Práticas de Fixação de Versão:**
   - Sempre fixe a versão (`package==1.2.3` ou `package@^1.2.3`) para evitar que versões futuras corrompidas sejam baixadas automaticamente.
