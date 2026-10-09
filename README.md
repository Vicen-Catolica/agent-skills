# Agent Skills Collection — Advanced Engineering Guardrails & Token Economy

Uma coleção de **Skills especializadas para Agentes de Codificação de IA** (compatível com Google Antigravity, Claude Code, Cursor, Codex e Reversa). Projetadas para resolver os principais desafios do desenvolvimento agentílico moderno: **economia extrema de tokens, mitigação de riscos de quebra, rigor em testes, segurança de dependências e auditoria de arquitetura**.

---

## 📦 Skills Disponíveis

### 1. 🧬 [`ast-context-distiller`](./ast-context-distiller/SKILL.md)
* **Objetivo:** Redução drástica do consumo de tokens (70%–90%).
* **O que faz:** Poda arquivos de código via Árvore Sintática Abstrata (AST) para gerar esqueletos de interfaces (classes, métodos, assinaturas de tipos, retornos e docstrings), omitindo a lógica interna que o agente não precisa carregar em memória.
* **Script Utilitário:** `ast-context-distiller/scripts/distill_ast.py`

### 2. 🛡️ [`agent-blast-radius-sentinel`](./agent-blast-radius-sentinel/SKILL.md)
* **Objetivo:** Prevenção preventiva de quebras e regressões em cascata.
* **O que faz:** Mapeia a base de código antes de qualquer alteração estrutural para identificar todos os arquivos dependentes, pontos de chamada e testes que dependem de um símbolo compartilhado.
* **Script Utilitário:** `agent-blast-radius-sentinel/scripts/calc_blast_radius.py`

### 3. 🧪 [`mutation-test-critic`](./mutation-test-critic/SKILL.md)
* **Objetivo:** Fim do "teatro de cobertura" em testes automatizados.
* **O que faz:** Injeta deliberadamente pequenas mutações lógicas (inversão de operadores, troca de condicionais, remoção de efeitos colaterais) para auditar se a suíte de testes realmente falha quando o código é corrompido.
* **Guia:** `mutation-test-critic/references/mutation_strategies.md`

### 4. 📦 [`supply-chain-typosquatting-auditor`](./supply-chain-typosquatting-auditor/SKILL.md)
* **Objetivo:** Segurança da cadeia de suprimentos e prevenção de alucinações.
* **O que faz:** Intercepta comandos de instalação (`pip install`, `npm install`), audita o nome do pacote contra riscos de typosquatting e verifica a existência do pacote no registro público oficial (PyPI/npm).
* **Script Utilitário:** `supply-chain-typosquatting-auditor/scripts/audit_package.py`

### 5. 😈 [`adversarial-devils-advocate`](./adversarial-devils-advocate/SKILL.md)
* **Objetivo:** Estresse de arquitetura e mitigação do viés do "caminho feliz".
* **O que faz:** Atua como um crítico cético na fase de planejamento de software, identificando *race conditions*, memory leaks, falhas parciais de rede, loops infinitos e consultas N+1 antes da escrita do código.
* **Guia:** `adversarial-devils-advocate/references/adversarial_checklist.md`

---

## 📋 Protocolo Operacional Geral: [`AGENTS.md`](./AGENTS.md)
O arquivo [`AGENTS.md`](./AGENTS.md) incluso neste repositório define o ciclo de vida completo de desenvolvimento com agentes (**Início, Meio e Fim**), orquestrando o framework [Reversa](https://github.com/sandeco/reversa) (da engenharia reversa de especificações SDD até a implementação via ciclo forward) e aplicando as diretrizes globais de economia de tokens.

---

## 🚀 Como Instalar e Usar

### Instalação Global (Antigravity)
Copie as pastas para o diretório de skills globais:
```bash
~/.gemini/config/skills/
```

### Instalação por Projeto (Workspace)
Copie as pastas desejadas para a raiz do seu repositório:
```bash
.agents/skills/   # ou .claude/skills/
```

---

## 📄 Licença
MIT License.
