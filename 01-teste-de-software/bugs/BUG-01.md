# BUG-01: Imagens incorretas na listagem de produtos para problem_user

- **Status:** Aberto
- **Ambiente:** saucedemo.com, Chrome (Versão 156.0.8078.76 (Versão oficial) 64 bits), Windows 11
- **Pré-condições:** usuário `problem_user` logado (senha `secret_sauce`)
- **Severidade:** média (não impede a compra, mas compromete a identificação visual do produto)
- **Prioridade:** média
- **Relacionado:** VF-06

## Passos para reproduzir
1. Abrir saucedemo.com.
2. Fazer login com `problem_user` / `secret_sauce`.
3. Observar as imagens da listagem de produtos.

## Resultado esperado
Cada produto exibe sua própria imagem.

## Resultado obtido
Os 6 produtos exibem o mesmo cachorro pug (ex.: Sauce Labs Backpack, Sauce Labs Bike Light, Sauce Labs Onesie).

## Evidência
![Listagem do problem_user com imagens repetidas](01-teste-de-software/evidencias/vf06-problem-user.png)