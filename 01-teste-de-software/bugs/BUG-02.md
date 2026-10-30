# BUG-02: Imagem de produto divergente da sua descrição

- **Status:** Aberto
- **Ambiente:** saucedemo.com, Chrome (Versão 156.0.8078.76 (Versão oficial) 64 bits), Windows 11
- **Pré-condições:** usuário `standard_user` logado (senha `secret_sauce`)
- **Severidade:** Alta (alta: o defeito afeta todos os usuários normais e induz a escolha errada de produto, já que a imagem não corresponde à descrição)
- **Prioridade:** Alta
- **Relacionado:** VF-13

## Passos para reproduzir
1. Abrir saucedemo.com.
2. Fazer login com `standard_user` / `secret_sauce`.
3. Localizar o card do produto Sauce Labs Bolt T-Shirt.

## Resultado esperado
A imagem do card deve exibir a camiseta cinza com a estampa de raio vermelho (Bolt), conforme a descrição exibida no card.

## Resultado obtido
A imagem exibida é de uma camiseta preta, e não cinza com bolt vermelho

## Evidência
![Listagem do standard_user com imagem diferente da descrição](evidencias/vf13-standard_user.png)