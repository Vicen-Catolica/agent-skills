# Adversarial Devil's Advocate Checklist

Este checklist orienta o agente a assumir uma postura cética e rigorosa para identificar falhas ocultas em planos arquiteturais e propostas técnicas antes do início da codificação.

## 1. Concorrência e Condições de Corrida (Race Conditions)
- O que acontece se duas requisições idênticas chegarem no mesmo milissegundo?
- Há risco de leituras sujas (*dirty reads*) ou escritas concorrentes sobre o mesmo recurso?
- Transações de banco de dados utilizam locks otimistas/pessimistas adequados?
- Há dependência de estado em memória não sincronizado entre múltiplos nós/threads?

## 2. Falhas Silenciosas e Resiliência
- Se o serviço externo ou banco cair, a aplicação falha de forma visível ou esconde a exceção silenciosamente (`except: pass`)?
- Há políticas de timeout e retentativa com backoff exponencial configuradas para todas as chamadas remotas?
- O que ocorre durante quedas repentinas de conexão no meio de uma transação multi-etapas?

## 3. Gestão de Memória, Recursos e Vazamentos
- Conexões de banco, arquivos e sockets de rede são explicitamente fechados (`with`, `using`, `try...finally`)?
- Estruturas de dados em memória (caches globais, listas de histórico) possuem limite de tamanho (`LRU`) ou crescem infinitamente até provocar Out-of-Memory (OOM)?

## 4. Segurança e Validação de Fronteira
- Há entradas de usuário inseridas diretamente em queries SQL, comandos shell ou templates HTML?
- Os endpoints exigem autenticação e autorização explícita para o dono do recurso (prevenção a IDOR)?
- Limites de tamanho de payload estão definidos para evitar ataques de DoS por exaustão de buffer?

## 5. Escalabilidade e Volumetria
- A solução realiza queries N+1 no banco de dados?
- O que acontece quando a tabela tiver 1.000.000 de registros em vez dos 10 registros de teste?
- Índices de banco de dados foram previstos para colunas utilizadas em cláusulas `WHERE` e `JOIN`?
