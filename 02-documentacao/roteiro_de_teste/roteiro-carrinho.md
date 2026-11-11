# Roteiro de testes: Carrinho de Compras

## 1. Objetivo

Verificar o comportamento de adição, remoção e persistência de itens no carrinho de compras, contagem do badge na barra superior e validação de restrições por usuário.

## 2. Pré-condições gerais
- Navegador Chrome (versão 156) em Windows 11.
- Acesso a `saucedemo.com`.
- Login realizado com sucesso com `standard_user` ou `problem_user` conforme o caso (VF-01 executado).

## 3. Massa de dados

| Usuário | Senha | Uso |
|---|---|---|
| standard_user | secret_sauce | Adição/remoção de itens, navegação entre telas e testes de persistência |
| problem_user | secret_sauce | Identificação de falha ao adicionar produtos específicos ao carrinho |

## 4. Ordem de execução

| Ordem | Caso | Descrição curta | Depende de |
|---|---|---|---|
| 1 | VF-15 | Adicionar 1 item a partir da vitrine | Nenhum |
| 2 | VF-17 | Remover 1 item a partir da vitrine | VF-15 |
| 3 | VF-16 | Adicionar múltiplos itens a partir da vitrine | Nenhum |
| 4 | VF-18 | Conferir lista e valores na tela do carrinho | VF-16 |
| 5 | VF-19 | Navegação "Continue Shopping" e retorno ao carrinho | VF-18 |
| 6 | VF-20 | Persistência do carrinho após recarregar a página (F5) | VF-18 |
| 7 | VF-21 | Remover item diretamente na tela do carrinho | VF-18 |
| 8 | VF-22 | Adicionar produtos específicos com `problem_user` | Nenhum |

## 5. Critério de saída
O bloco de carrinho é considerado executado quando todos os 8 casos (VF-15 a VF-22) tiverem status preenchido (Passou ou Falhou) e o bug vinculado (BUG-04) estiver devidamente registrado.

## 6. Observações
- A ordem executa primeiro o ciclo de adição/remoção unitária e múltiplos itens com `standard_user` (VF-15 a VF-21) para validar as regras do carrinho antes de testar a falha com `problem_user`.
- O caso VF-22 é mantido por último por ser um defeito conhecido, evitando que falhas de inclusão de itens bloqueiem os testes funcionais gerais.
- Os casos VF-15 a VF-22 estão em `verificacoes-funcionais.md`. Este roteiro define a ordem, a massa de dados e as dependências operacionais.