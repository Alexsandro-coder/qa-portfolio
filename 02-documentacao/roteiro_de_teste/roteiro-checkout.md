# Roteiro de testes: Checkout

## 1. Objetivo

Verificar a navegação para a etapa de informação do comprador, a validação de campos obrigatórios do formulário, o cálculo do resumo do pedido (subtotal, impostos e total) e a finalização da compra.

## 2. Pré-condições gerais
- Navegador Chrome (versão 156) em Windows 11.
- Acesso a `saucedemo.com`.
- Login realizado com sucesso com o usuário `standard_user` (VF-01 executado).
- Itens previamente adicionados ao carrinho conforme a necessidade de cada caso.

## 3. Massa de dados

| Usuário | Senha | Uso |
|---|---|---|
| standard_user | secret_sauce | Validação de fluxo ponta a ponta, validação de campos obrigatórios e conferência de totais |

## 4. Ordem de execução

| Ordem | Caso | Descrição curta | Depende de |
|---|---|---|---|
| 1 | VF-23 | Acesso à tela Checkout: Your Information | Nenhum |
| 2 | VF-24 | Validação de formulário com todos os campos vazios | VF-23 |
| 3 | VF-25 | Validação de formulário com Last Name vazio | VF-23 |
| 4 | VF-26 | Avanco para a tela Checkout: Overview | VF-23 |
| 5 | VF-27 | Conferência de Item total, Tax e Total | VF-26 |
| 6 | VF-28 | Finalização do pedido e zeramento do carrinho | VF-26 |

## 5. Critério de saída
O bloco de checkout é considerado executado quando todos os 6 casos (VF-23 a VF-28) tiverem status preenchido (Passou ou Falhou) e eventuais divergências de cálculo ou navegação estiverem devidamente registradas.

## 6. Observações
- A ordem segue o fluxo natural de navegação do usuário (dados do comprador -> validação de formulário -> visão geral -> finalização).
- Os casos VF-23 a VF-28 estão em `verificacoes-funcionais.md`. Este roteiro organiza a ordem de execução, a massa de dados e as dependências operacionais entre as telas do checkout.