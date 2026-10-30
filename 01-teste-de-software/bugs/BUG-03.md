# BUG-03: Nome foge do padrão “Sauce Labs ..."

- **Status:** Aberto
- **Ambiente:** saucedemo.com, Chrome (Versão 156.0.8078.76 (Versão oficial) 64 bits), Windows 11
- **Pré-condições:** usuário `standard_user` logado (senha `secret_sauce`)
- **Severidade:** Baixa (não impede a compra, mas compromete a identificação do produto)
- **Prioridade:** Baixa
- **Relacionado:** VF-14

## Passos para reproduzir
1. Abrir saucedemo.com.
2. Fazer login com `standard_user` / `secret_sauce`.
3. Localizar o card do produto Test.allTheThings() T-Shirt (Red)

## Resultado esperado
O nome do produto deve seguir o padrão estabelecido "Sauce Labs ..."

## Resultado obtido
O produto não seguiu o padrão estabelecido e está com o nome de Test.allTheThings() T-Shirt (Red)

## Evidência
![Listagem do standard_user com nome fora do padrão no catálogo](evidencias/vf14-standard_user.png)