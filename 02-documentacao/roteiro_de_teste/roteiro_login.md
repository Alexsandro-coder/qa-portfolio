# Roteiro de testes: Login

## 1. Objetivo
Verificar o comportamento da tela de login do SauceDemo para credenciais válidas, inválidas e campos obrigatórios.

## 2. Pré-condições gerais
- Navegador Chrome (versão 156) em Windows 11.
- Acesso a saucedemo.com.
- Senha de todos os usuários de teste: `secret_sauce`.

## 3. Massa de dados

| Usuário | Senha | Uso |
|---|---|---|
| standard_user | secret_sauce | Caminho feliz |
| locked_out_user | secret_sauce | Usuário bloqueado |
| problem_user | secret_sauce | Comportamento com defeitos conhecidos |
| (vazio) | secret_sauce | Campo obrigatório |
| standard_user | teste_sauce | Senha inválida |

## 4. Ordem de execução

| Ordem | Caso | Descrição curta | Depende de |
|---|---|---|---|
| 1 | VF-01 | Login válido com standard_user | Nenhum |
| 2 | VF-03 | Senha inválida | Nenhum |
| 3 | VF-04 | Campo de usuário vazio | Nenhum |
| 4 | VF-05 | Campo de senha vazio | Nenhum |
| 5 | VF-02 | Usuário bloqueado | Nenhum |
| 6 | VF-06 | Login do problem_user | Nenhum |

## 5. Critério de saída
O bloco de login é considerado executado quando todos os 6 casos tiverem status preenchido (Passou ou Falhou) e os bugs relacionados estiverem registrados.

## 6. Observações
- A ordem foi escolhida para começar pelo caminho feliz e deixar o problem_user por último, porque ele tem defeitos conhecidos que não devem atrapalhar o restante.
- Os casos VF-01 a VF-06 estão em `verificacoes-funcionais.md`. Este roteiro define a ordem e os dados, não repete os passos.