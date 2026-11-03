# Verificações funcionais

Verificação funcional é testar o que o sistema faz, comparando o comportamento com o que foi pedido. Cada verificação tem três partes: a **ação** (o que foi feito), o **resultado esperado** (o que deveria acontecer) e o **resultado obtido** (o que de fato aconteceu).

**Sistema:** SauceDemo (saucedemo.com), Chrome 156, Windows 11.
**Total:** 32 verificações. Bugs encontrados: 5 (ver pasta `bugs/`).

| Bloco | Quantidade | Foco |
|---|---|---|
| Login | 6 | Credenciais válidas e inválidas, campos vazios, usuário bloqueado |
| Listagem | 8 | Ordenação (nome e preço), imagens, preços, detalhe do item |
| Carrinho | 8 | Adicionar, remover, contador, persistência ao navegar |
| Checkout | 6 | Campos obrigatórios, cálculo de total, confirmação do pedido |
| Bugs de propósito | 4 | Comportamentos do problem_user |

---

## Login (6)

| ID | Funcionalidade | Pré-condição | Ação | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|---|---|
| VF-01 | Login | Usuário standard_user cadastrado | Digitar standard_user e secret_sauce e clicar em Login | Redirecionar para a página de produtos | Redirecionado para a página Products | Passou |
| VF-02 | Login | Usuário locked_out_user cadastrado | Digitar locked_out_user e secret_sauce e clicar em Login | Exibir mensagem de usuário bloqueado e não redirecionar | Mensagem de usuário bloqueado exibida e sem redirecionamento | Passou |
| VF-03 | Login | Usuário standard_user cadastrado | Digitar standard_user e teste_sauce e clicar em Login | Exibir mensagem de credenciais inválidas | "Epic sadface: Username and password do not match any user in this service" | Passou |
| VF-04 | Login | Página de login aberta | Deixar o campo usuário vazio, digitar secret_sauce e clicar em Login | Exibir mensagem de usuário obrigatório | "Epic sadface: Username is required" | Passou |
| VF-05 | Login | Usuário standard_user cadastrado | Digitar standard_user, deixar o campo senha vazio e clicar em Login | Exibir mensagem de senha obrigatória | "Epic sadface: Password is required" | Passou |
| VF-06 | Login | Usuário problem_user cadastrado | Digitar problem_user e secret_sauce e clicar em Login | Redirecionar para a página de produtos | Redirecionado para Products, mas as imagens dos 6 produtos são o mesmo cachorro pug. Ver BUG-01 | Falhou |

---

## Listagem (8)

| ID | Funcionalidade | Pré-condição | Ação | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|---|---|
| VF-07 | Listagem | Página Products aberta | Ordenar por Price (low to high) | Produtos do menor para o maior preço | Primeiro: Sauce Labs Onesie ($7.99). Último: Sauce Labs Fleece Jacket ($49.99) | Passou |
| VF-08 | Listagem | Página Products aberta | Ordenar por Price (high to low) | Produtos do maior para o menor preço | Primeiro: Sauce Labs Fleece Jacket ($49.99). Último: Sauce Labs Onesie ($7.99) | Passou |
| VF-09 | Listagem | Página Products aberta | Ordenar por Name (A to Z) | Produtos de A a Z | Sauce Labs Backpack, Bike Light, Bolt T-Shirt, Fleece Jacket, Onesie, Test.allTheThings() T-Shirt (Red) | Passou |
| VF-10 | Listagem | Página Products aberta | Ordenar por Name (Z to A) | Produtos de Z a A | Test.allTheThings() T-Shirt (Red), Onesie, Fleece Jacket, Bolt T-Shirt, Bike Light, Backpack | Passou |
| VF-11 | Listagem | Página Products aberta | Clicar em um produto (ex.: Sauce Labs Backpack) | Abrir a página do produto | Página do produto aberta com nome, descrição e valor corretos | Passou |
| VF-12 | Listagem | standard_user logado | Observar imagem e preço dos 6 produtos | Cada produto com imagem própria e preço correspondente | Todos os produtos com imagem e preço individuais e correspondentes | Passou |
| VF-13 | Listagem | standard_user logado | Observar imagem, nome e descrição do Sauce Labs Bolt T-Shirt | Imagem, nome e descrição condizentes com o produto | Descrição de camiseta cinza com bolt vermelho, mas a imagem exibida é de camisa preta. Ver BUG-02 | Falhou |
| VF-14 | Listagem | standard_user logado | Observar o nome do Test.allTheThings() T-Shirt (Red) | Nome no padrão do catálogo "Sauce Labs ..." | Nome "Test.allTheThings() T-Shirt (Red)" foge do padrão. Ver BUG-03 | Falhou |

---

## Carrinho (8)

| ID | Funcionalidade | Pré-condição | Ação | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|---|---|
| VF-15 | Carrinho | standard_user logado, carrinho vazio | Clicar em "Add to cart" no Sauce Labs Backpack | Ícone mostra 1 e o botão muda para "Remove" | Ícone mostrando 1 e botão alterado para "Remove" | Passou |
| VF-16 | Carrinho | standard_user logado, carrinho vazio | Adicionar Backpack, Bike Light e Onesie | Ícone mostra 3 | Ícone mostrando 3 | Passou |
| VF-17 | Carrinho | 1 item no carrinho | Clicar em "Remove" no item adicionado | Ícone some ou mostra 0, e o botão volta para "Add to cart" | Ícone sem número e botão "Add to cart" restaurado | Passou |
| VF-18 | Carrinho | standard_user logado, 3 itens no carrinho | Abrir o carrinho e conferir a lista | Os 3 itens com nome e preço corretos | Sauce Labs Onesie ($7.99), Sauce Labs Backpack ($29.99) e Sauce Labs Bike Light ($9.99), conferindo com a listagem | Passou |
| VF-19 | Carrinho | Itens no carrinho | Abrir o carrinho, clicar em "Continue Shopping" e voltar | Itens continuam no carrinho | Itens continuam no carrinho após voltar à listagem | Passou |
| VF-20 | Carrinho | Carrinho com itens | Recarregar a página (F5) | Itens permanecem no carrinho | O item permaneceu no carrinho após o F5 | Passou |
| VF-21 | Carrinho | Carrinho com 1 item | Remover o item dentro da tela do carrinho | Item removido e contador atualizado | Item removido da lista e contador atualizado para o novo total | Passou |
| VF-22 | Carrinho | problem_user logado | Adicionar Bolt T-Shirt, Fleece Jacket e Test.allTheThings() T-Shirt (Red) | Itens adicionados e contador correto | Três itens não entraram no carrinho (Bolt T-Shirt, Fleece Jacket e Test.allTheThings() T-Shirt). Os demais entraram e o contador acompanhou. Ver BUG-04 | Falhou |

---

## Checkout (6)

| ID | Funcionalidade | Pré-condição | Ação | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|---|---|
| VF-23 | Checkout | standard_user logado, 3 itens no carrinho | Clicar em "Checkout" | Tela "Your Information" com First Name, Last Name e Postal Code | Tela "Checkout: Your Information" com os campos First Name, Last Name e Zip/Postal Code | Passou |
| VF-24 | Checkout | Tela "Your Information" aberta, campos vazios | Clicar em "Continue" sem preencher nada | Mensagem "Error: First Name is required" | Mensagem "Error: First Name is required" exibida | Passou |
| VF-25 | Checkout | Tela "Your Information" aberta | Preencher First Name e Postal Code, deixar Last Name vazio e clicar em "Continue" | Mensagem "Error: Last Name is required" | Mensagem "Error: Last Name is required" exibida | Passou |
| VF-26 | Checkout | Campos preenchidos corretamente | Clicar em "Continue" | Tela "Checkout: Overview" com os 3 itens e o total | Tela "Checkout: Overview" com Sauce Labs Onesie ($7.99), Sauce Labs Backpack ($29.99) e Sauce Labs Bike Light ($9.99) | Passou |
| VF-27 | Checkout | Tela "Checkout: Overview" aberta | Conferir Item total, Tax e Total | Item total = soma dos preços; Total = Item total + Tax | Item total $47.97 (igual à soma dos preços), Tax $3.84, Total $51.81 | Passou |
| VF-28 | Checkout | Tela "Checkout: Overview" aberta | Clicar em "Finish" | Tela "Thank you for your order!" e contador zerado | Tela "Thank you for your order!" exibida e contador em 0 | Passou |

---

## Bugs de propósito (4)

| ID | Funcionalidade | Pré-condição | Ação | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|---|---|
| VF-29 | Bugs de propósito | problem_user logado | Abrir a página de produtos e observar as imagens | Cada produto com imagem própria | Mesmo cachorro pug nos 6 produtos. Ver BUG-01 | Falhou |
| VF-30 | Bugs de propósito | problem_user logado | Abrir o detalhe do Sauce Labs Backpack | Imagem e descrição correspondem ao produto | Imagem e descrição do Sauce Labs Backpack correspondem ao produto | Passou |
| VF-31 | Bugs de propósito | problem_user logado | Adicionar ao carrinho Bolt T-Shirt, Fleece Jacket e Test.allTheThings() T-Shirt (Red) | Os três itens entram no carrinho e o contador aumenta | Os três itens não entraram no carrinho. Ver BUG-04 | Falhou |
| VF-32 | Bugs de propósito | problem_user logado, com Sauce Labs Backpack no carrinho | Clicar em "Remove" na listagem principal | Item removido e botão volta para "Add to cart" | Botão "Remove" travado na listagem principal: o item não é removido e o contador não muda. Ver BUG-05 | Falhou |