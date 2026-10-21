# Técnicas de caixa-preta

## 1. Partição de equivalência

### Sistema: cadastro de instrutor, campo "idade" (aceita de 18 a 65)

| Partição | faixa | tipo | valor_de_teste | resultado esperado |
|---|---|---|---|---|
| p1 | menor que 18 | invalido | 16 | mensagem: "idade mínima permitida e de 18 anos" |  
| p2 | de 18 a 65 | valido | 32 |  mensagem: "Cadastro realizado" |
| p3 | maior que 65 | invalido | 70 |  mensagem: "Idade máxima permitida e de 65 anos" |

**Observação:** 32 anos foi escolhido devido esta mais próximo do centro da idade permitida, Não foram utilizados as idades 18 e 65 por se tratarem de valores limite (bordas), os quais já fazem parte do escopo específico de Análise de Valor Limite (AVL)

---

### Sistema: cadastro de senha, campo "senha" (aceita de 8 a 20 caracteres, com pelo menos 1 numero)

| Partição | faixa | tipo | valor_de_teste | resultado esperado | 
|---|---|---|---|---|
| p1 | menor que 8 |invalido | 123abc | mensagem: "senha pequena, mínimo de 8 caracteres" | 
| p2 | de 8 a 20 com numero| valido | r2026claro5539 | mensagem: " senha cadastrada com sucesso" |
| p3 | maior que 20 | invalido | batatinhafrita123batatinhafrita123 | mensagem: "senha excede o limite, máximo de 20 caracteres" |
| p4 | de 8 a 20 sem numero | invalido | abcdefghijklmno | mensagem: "senha deve conter ao menos 1 numero" 

**Observação:** A senha de 14 caracteres (r2026claro5539) foi escolhida como padrão empresarial, seguindo a estrutura: [setor: r] + [ano: 2026] + [produto: claro] + [matrícula: 5539], p2 e p4 têm o mesmo tamanho e diferem apenas pela presença de número. Não foram utilizados os tamanhos de 8 ou 20 caracteres por se tratarem de valores limite (bordas), os quais já fazem parte do escopo específico de Análise de Valor Limite (AVL)

---

### Sistema: desconto de compras, (até R$ 100,00 = 0%; de R$ 100,01 a R$ 300,00 = 5%; acima de R$ 300,00 = 10%)

| Partição | faixa | tipo | valor_de_teste | resultado esperado |
|---|---|---|---|---|
| p1 | ate 100,00 | 0% de desconto | 99,00 | “valor cobrado integralmente, sem desconto” | 
| p2 | entre 100,01 e 300,00 | 5% de desconto | 150,00 | mensagem: "você ganhou 5% de desconto" | 
| p3 | acima de 300,00 | 10% de desconto | 310,00 | mensagem: "você ganhou 10% de desconto" |

**Observação:** O valor de 150,00 escolhido por esta no meio da faixa de valores de 5% , Não foram utilizados os valores 100,01 e 300,01 por se tratarem de valores limite (bordas), os quais já fazem parte do escopo específico de Análise de Valor Limite (AVL)

---

## 2. Análise de valor limite


### Sistema: cadastro de instrutor, campo "idade" (aceita de 18 a 65)

| Valor | Posição | Resultado esperado | Justificativa |
|---|---|---|---|
| 17 | abaixo de faixa (a-1) | mensagem: "idade mínima permitida e de 18 anos" | Valor inválido (abaixo do limite inferior). Garante que o sistema bloqueia menores de 18 anos e valida se a lógica do código não possui falhas em operadores condicionais (ex: uso incorreto de `>` no lugar de `>=`). |
| 18 | borda inferior (a) | mensagem: "Cadastro realizado" | Valor válido (limite inferior). Valida se a regra da borda está incluída e se o sistema aceita o primeiro valor permitido da faixa. |
| 65 | borda superior (b) | mensagem: "Cadastro realizado" | Valor válido (limite superior). Valida se a regra da borda está incluída e se o sistema aceita o último valor permitido da faixa. |
| 66 | acima da faixa (b+1) | mensagem: "Idade máxima permitida e de 65 anos" | Valor inválido (acima do limite superior). Garante que o sistema bloqueia maiores de 65 anos e valida se a lógica do código não possui falhas em operadores condicionais (ex: uso incorreto de `<` no lugar de `<=`). |

---

### Sistema: cadastro de senha, campo "senha" (aceita de 8 a 20 caracteres, com pelo menos 1 número)

| Valor | Posição | Resultado esperado | Justificativa |
|---|---|---|---|
| 7 | abaixo de faixa (a-1) | mensagem: "senha pequena, mínimo de 8 caracteres" | Valor inválido (abaixo do limite inferior). Garante que o sistema bloqueia senhas com menos de 8 caracteres e valida se a lógica do código não possui falhas em operadores condicionais (ex: uso incorreto de `>` no lugar de `>=`). |
| 8 | borda inferior (a) | mensagem: "senha cadastrada com sucesso" | Valor válido (limite inferior). Valida se a regra da borda está incluída e se o sistema aceita o primeiro valor permitido da faixa. |
| 20 | borda superior (b) | mensagem: "senha cadastrada com sucesso" | Valor válido (limite superior). Valida se a regra da borda está incluída e se o sistema aceita o último valor permitido da faixa. |
| 21 | acima da faixa (b+1) | mensagem: "senha excede o limite, máximo de 20 caracteres" | Valor inválido (acima do limite superior). Garante que o sistema bloqueia senhas com mais de 20 caracteres e valida se a lógica do código não possui falhas em operadores condicionais (ex: uso incorreto de `<` no lugar de `<=`). |

---

### Sistema: desconto de compras (até R$ 100,00 = 0%; de R$ 100,01 a R$ 300,00 = 5%; acima de R$ 300,00 = 10%)

| Valor | Posição | Resultado esperado | Justificativa |
|---|---|---|---|
| 100,00 | Borda superior da Faixa 1 (0%) | mensagem: "valor cobrado integralmente, sem desconto" | 100,00 pertence à faixa de 0%. Se o código usar `>` no lugar de `>=`, ele daria 5% aqui. |
| 100,01 | Borda inferior da Faixa 2 (5%) | mensagem: "você ganhou 5% de desconto" | Primeiro valor válido para o desconto de 5%. Garante que o sistema inicia o desconto exatamente no centavo correto. |
| 300,00 | Borda superior da Faixa 2 (5%) | mensagem: "você ganhou 5% de desconto" | 300,00 pertence à faixa de 5%. Se o código usar `>` no lugar de `>=`, ele daria 10% aqui. |
| 300,01 | Borda inferior da Faixa 3 (10%) | mensagem: "você ganhou 10% de desconto" | Primeiro valor válido para o desconto máximo de 10%. Valida se a transição de faixas ocorre corretamente no centavo estipulado. |

---

## 3. Tabela de Decisão


### (DT1) - Regras de Frete

Esta é a estrutura completa mapeando todas as 8 combinações possíveis de condições:

| Condição | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|---|---|---|---|---|---|---|---|---|
| Compra >= R\$ 200,00 | Sim | Sim | Sim | Sim | Não | Não | Não | Não |
| Cliente Cadastrado | Sim | Sim | Não | Não | Sim | Não | Sim | Não |
| Interior | Sim | Não | Não | Sim | Sim | Sim | Não | Não |
| **Ação: Valor do Frete** | **R\$ 15** | **R\$ 0** | **R\$ 10** | **R\$ 25** | **R\$ 35** | **R\$ 35** | **R\$ 20** | **R\$ 20** |



### Tabela de Decisão Resumida e Otimizada (DT1)

Ao aplicar a técnica de simplificação de tabelas de decisão, consolidamos os cenários onde o status do "Cliente Cadastrado" torna-se irrelevante (`-`) para o resultado final do frete (quando a compra é menor que R\$ 200,00). Isso reduz o escopo de 8 para 6 regras de teste essenciais:

| Condição | R1 | R2 | R3 | R4 | R5 (Consolidada) | R6 (Consolidada) |
|---|---|---|---|---|---|---|
| Compra >= R\$ 200,00 | Sim | Sim | Sim | Sim | Não | Não |
| Cliente Cadastrado | Sim | Sim | Não | Não | - | - |
| Interior | Sim | Não | Não | Sim | Sim | Não |
| **Ação: Valor do Frete** | **R\$ 15** | **R\$ 0** | **R\$ 10** | **R\$ 25** | **R\$ 35** | **R\$ 20** |

#### Detalhamento das Regras Consolidadas:
* **R5 (União das antigas R5 e R6):** Quando a compra é menor que R\$ 200,00 e a entrega é no interior, o frete sempre será **R\$ 35** (R\$ 20 do frete cheio + R\$ 15 do interior), não importando se o cliente é cadastrado ou não.
* **R6 (União das antigas R7 e R8):** Quando a compra é menor que R\$ 200,00 e a entrega é na capital, o frete sempre será **R\$ 20** (frete cheio sem adicionais), independentemente do cadastro do cliente.

---

### (DT2) - Reserva de Equipamento

Esta estrutura mapeia todas as 8 combinações lógicas possíveis para o sistema de reservas:

| Condição | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|---|---|---|---|---|---|---|---|---|
| É Professor? | Sim | Sim | Sim | Sim | Não (Aluno) | Não (Aluno) | Não (Aluno) | Não (Aluno) |
| Equipamento Disponível? | Sim | Sim | Não | Não | Sim | Sim | Não | Não |
| Antecedência >= 24h? | Sim | Não | Sim | Não | Sim | Não | Sim | Não |
| **Ação: Status do Pedido** | **Aprovada** | **Coordenação** | **Recusada** | **Recusada** | **Coordenação** | **Coordenação** | **Recusada** | **Recusada** |



### Tabela de Decisão Resumida e Otimizada (DT2)

Ao aplicar as regras de simplificação, reduzimos o escopo de 8 para **4 regras essenciais de teste**, eliminando redundâncias quando as condições não alteram o resultado final:

| Condição | R1 | R2 | R3 (Consolidada) | R4 (Consolidada) |
|---|---|---|---|---|
| É Professor? | Sim | Sim | Não (Aluno) | - |
| Equipamento Disponível? | Sim | Sim | Sim | Não |
| Antecedência >= 24h? | Sim | Não | - | - |
| **Ação: Status do Pedido** | **Aprovada** | **Coordenação** | **Coordenação** | **Recusada** |

#### Detalhamento das Regras Consolidadas:
* **R3 (União das antigas R5 e R6):** Quando o solicitante é um Aluno e o equipamento está disponível, o pedido sempre vai para a **Coordenação**, tornando a antecedência de 24h irrelevante (`-`) para a decisão do sistema.
* **R4 (União das antigas R3, R4, R7 e R8):** Se o equipamento estiver indisponível, o pedido sempre será **Recusada**, independentemente de quem solicitou (Professor ou Aluno) ou do prazo de antecedência.
