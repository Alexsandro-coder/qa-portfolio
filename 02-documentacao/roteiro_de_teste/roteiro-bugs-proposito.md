# Roteiro de testes: Bugs de Propósito (problem_user)

## 1. Objetivo

Isolar e verificar as falhas conhecidas de renderização, adição/remoção de itens e comportamento inconsistente do catálogo provocadas pelo usuário `problem_user`.

## 2. Pré-condições gerais
- Navegador Chrome (versão 156) em Windows 11.
- Acesso a `saucedemo.com`.
- Autenticação prévia efetuada com o usuário `problem_user` (senha `secret_sauce`).

## 3. Massa de dados

| Usuário | Senha | Uso |
|---|---|---|
| problem_user | secret_sauce | Evidenciar comportamentos anômalos e defeitos conhecidos da aplicação |

## 4. Ordem de execução

| Ordem | Caso | Descrição curta | Depende de |
|---|---|---|---|
| 1 | VF-29 | Exibição de imagens no catálogo (Pug repetido) | Nenhum |
| 2 | VF-30 | Exibição de detalhes da Sauce Labs Backpack | Nenhum |
| 3 | VF-31 | Adição de produtos específicos ao carrinho | Nenhum |
| 4 | VF-32 | Remoção de item na listagem principal | Nenhum |

## 5. Critério de saída
O bloco de bugs de propósito é considerado executado quando todos os 4 casos (VF-29 a VF-32) tiverem status preenchido (Passou ou Falhou) e os defeitos vinculados (BUG-01, BUG-04 e BUG-05) estiverem devidamente reportados no repositório.

## 6. Observações
- Este bloco agrupa exclusivamente as verificações com `problem_user` para não interferir na execução do caminho feliz e dos testes funcionais padrão realizados com `standard_user`.
- Os casos VF-29 a VF-32 estão detalhados em `verificacoes-funcionais.md`. Este roteiro estabelece a ordem e a rastreabilidade dos defeitos simulados.