# verificação funcional

* É testar o que o sistema faz, comparando o comportamento com o que foi pedido. Cada verificação tem três partes: a ação (o que você faz), o resultado esperado (o que deveria acontecer) e o resultado obtido (o que de fato aconteceu).


### Roteiro de 30 verificações (SauceDemo)


| Bloco | Quantidade | Foco |
|---|---|---|
| Login | 6 | Credenciais válidas, inválidas, campos vazios, locked_out_user |
| Navegação e listagem | 6 | Ordenação (nome e preço), exibição de produtos, detalhe do item |
| Carrinho | 6 | Adicionar, remover, quantidade, total, persistência ao navegar |
| Checkout | 6 | Dados obrigatórios, cálculo de total, confirmação do pedido |
| Bugs de propósito | 6 | Comportamentos dos usuários problem_user e error_user |



| ID | Funcionalidade | Pré-condição | Ação | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|---|---|
| VF-01 | Login | Usuário standard_user cadastrado | Digitar standard_user e secret_sauce e clicar em Login | Redirecionar para a página de produtos |  Foi redirecionado para a pagina de Products | Passou |
| VF-02 | Login | Usuário locked_out_user cadastrado | Digitar locked_out_user e secret_sauce e clicar em Login | Exibir mensagem de usuário bloqueado e não redirecionar | A mensagem de usuário bloqueado foi exibida e não houve redirecionamento | Passou |
| VF-03 | Login | Usuário standard_user cadastrado | Digitar standard_user e teste_sauce e clicar em Login | Exibir mensagem de credenciais invalidas | Epic sadface: Username and password do not match any user in this service | Passou |
| VF-04 | Login | Página de login aberta | Deixar o campo usuário vazio, digitar secret_sauce e clicar em Login | Exibir mensagem de Username obrigatorio | Epic sadface: Username is required | Passou |
| VF-05 | Login | Usuário standard_user cadastrado | Digitar standard_user, deixar o campo senha vazio e clicar em Login | Exibir mensagem de Password obrigatorio | Epic sadface: Password is required | Passou |
| VF-06 | Login | Usuário problem_user cadastrado | Digitar problem_user e secret_sauce e clicar em Login | Redirecionar para a página de produtos | Redirecionado para Products, mas todas as imagens dos 6 produtos exibem o mesmo cachorro pug (ex.: Sauce Labs Backpack, Bike Light, Onesie). Evidência: ![vf06_problem_user](01-teste-de-software/evidencias/vf06-problem-user.png)| Falhou |
| VF-07 | listagem | Tela inicial Products | Ordenar o Products com Price (low to high) | Produtos ordenados por preço do menor para o maior | Produtos foram ordenados por valor do menor para o maior | Passou |
| VF-08 | listagem | Tela inicial Products | Ordenar o Products com Name (A to Z) | Produtos ordenados pelo nome de A - Z | Produtos foram ordenados por nome de A - Z | Passou |
| VF-09 |
| VF-10 |
| VF-11 |
| VF-12 |
| VF-13 |
| VF-14 |
| VF-15 |
| VF-16 |
| VF-17 |
| VF-18 |
| VF-19 |
| VF-20 |
| VF-21 |
| VF-22 |
| VF-23 |
| VF-24 |
| VF-25 |
| VF-26 |
| VF-27 |
| VF-28 |
| VF-29 |
| VF-30 |
