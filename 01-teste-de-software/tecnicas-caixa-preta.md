# Técnicas de caixa-preta

## 1. Partição de equivalência

### Sistema: cadastro de instrutor, campo "idade" (aceita de 18 a 65)

| Partição | Faixa | Tipo | Valor de teste | Resultado esperado |
|---|---|---|---|---|
| P1 | menor que 18 | inválido | 16 | Mensagem: "idade mínima permitida é de 18 anos" |
| P2 | de 18 a 65 | válido | 32 | Mensagem: "Cadastro realizado" |
| P3 | maior que 65 | inválido | 70 | Mensagem: "idade máxima permitida é de 65 anos" |

**Observação:** 32 anos foi escolhido por estar próximo do centro da faixa. Não foram usados 18 e 65 porque são valores de borda, que pertencem à análise de valor limite.

### Sistema: cadastro de senha, campo "senha" (aceita de 8 a 20 caracteres, com pelo menos 1 número)

| Partição | Faixa | Tipo | Valor de teste | Resultado esperado |
|---|---|---|---|---|
| P1 | menor que 8 | inválido | 123abc | Mensagem: "senha pequena, mínimo de 8 caracteres" |
| P2 | de 8 a 20, com número | válido | r2026claro5539 | Mensagem: "senha cadastrada com sucesso" |
| P3 | maior que 20 | inválido | batatinhafrita123batatinhafrita123 | Mensagem: "senha excede o limite, máximo de 20 caracteres" |
| P4 | de 8 a 20, sem número | inválido | abcdefghijklmno | Mensagem: "senha deve conter ao menos 1 número" |

**Observação:** a senha de 14 caracteres (r2026claro5539) foi escolhida como padrão empresarial, seguindo a estrutura [setor: r] + [ano: 2026] + [produto: claro] + [matrícula: 5539]. P2 e P4 têm o mesmo tamanho e diferem apenas pela presença de número. Não foram usados 8 e 20 caracteres porque são valores de borda, que pertencem à análise de valor limite.

### Sistema: desconto de compras (até R$ 100,00 = 0%; de R$ 100,01 a R$ 300,00 = 5%; acima de R$ 300,00 = 10%)

| Partição | Faixa | Tipo | Valor de teste | Resultado esperado |
|---|---|---|---|---|
| P1 | até 100,00 | 0% de desconto | 99,00 | Mensagem: "valor cobrado integralmente, sem desconto" |
| P2 | entre 100,01 e 300,00 | 5% de desconto | 150,00 | Mensagem: "você ganhou 5% de desconto" |
| P3 | acima de 300,00 | 10% de desconto | 310,00 | Mensagem: "você ganhou 10% de desconto" |

**Observação:** 150,00 foi escolhido por estar no meio da faixa de 5%. Não foram usados 100,01 e 300,01 porque são valores de borda, que pertencem à análise de valor limite.

## 2. Análise de valor limite

### Sistema: cadastro de instrutor, campo "idade" (aceita de 18 a 65)

| Valor | Posição | Resultado esperado | Justificativa |
|---|---|---|---|
| 17 | abaixo da faixa (a-1) | Mensagem: "idade mínima permitida é de 18 anos" | Valor logo abaixo da borda inferior. Se o código usar `>` no lugar de `>=`, a regra de 18 anos ficaria errada e o 18 seria recusado. Este caso confirma que o 17 é bloqueado. |
| 18 | borda inferior (a) | Mensagem: "Cadastro realizado" | Primeiro valor válido. Confirma que a borda inferior está incluída na faixa. |
| 65 | borda superior (b) | Mensagem: "Cadastro realizado" | Último valor válido. Confirma que a borda superior está incluída na faixa. |
| 66 | acima da faixa (b+1) | Mensagem: "idade máxima permitida é de 65 anos" | Valor logo acima da borda superior. Se o código usar `<` no lugar de `<=`, o 65 seria recusado. Este caso confirma que o 66 é bloqueado. |

### Sistema: cadastro de senha, campo "senha" (aceita de 8 a 20 caracteres, com pelo menos 1 número)

| Valor | Posição | Resultado esperado | Justificativa |
|---|---|---|---|
| 7 | abaixo da faixa (a-1) | Mensagem: "senha pequena, mínimo de 8 caracteres" | Valor logo abaixo da borda inferior. Se o código usar `>` no lugar de `>=`, a senha de 8 caracteres seria recusada. |
| 8 | borda inferior (a) | Mensagem: "senha cadastrada com sucesso" | Primeiro valor válido. Confirma que o tamanho mínimo está incluído. |
| 20 | borda superior (b) | Mensagem: "senha cadastrada com sucesso" | Último valor válido. Confirma que o tamanho máximo está incluído. |
| 21 | acima da faixa (b+1) | Mensagem: "senha excede o limite, máximo de 20 caracteres" | Valor logo acima da borda superior. Se o código usar `<` no lugar de `<=`, a senha de 20 caracteres seria recusada. |

### Sistema: desconto de compras (até R$ 100,00 = 0%; de R$ 100,01 a R$ 300,00 = 5%; acima de R$ 300,00 = 10%)

| Valor | Posição | Resultado esperado | Justificativa |
|---|---|---|---|
| 100,00 | borda superior da faixa 1 (0%) | Mensagem: "valor cobrado integralmente, sem desconto" | 100,00 pertence à faixa de 0%. Se o código usar `>` no lugar de `>=`, ele daria 5% aqui. |
| 100,01 | borda inferior da faixa 2 (5%) | Mensagem: "você ganhou 5% de desconto" | Primeiro valor da faixa de 5%. Confirma que o desconto começa no centavo correto. |
| 300,00 | borda superior da faixa 2 (5%) | Mensagem: "você ganhou 5% de desconto" | 300,00 pertence à faixa de 5%. Se o código usar `>` no lugar de `>=`, ele daria 10% aqui. |
| 300,01 | borda inferior da faixa 3 (10%) | Mensagem: "você ganhou 10% de desconto" | Primeiro valor da faixa de 10%. Confirma que a transição de faixa ocorre no centavo correto. |

## 3. Tabela de decisão

### DT1: frete

**Tabela completa (8 regras)**

| Condição | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|---|---|---|---|---|---|---|---|---|
| Compra ≥ R$ 200,00 | Sim | Sim | Sim | Sim | Não | Não | Não | Não |
| Cliente cadastrado | Sim | Sim | Não | Não | Sim | Não | Sim | Não |
| Interior | Sim | Não | Não | Sim | Sim | Sim | Não | Não |
| **Frete** | R$ 15 | R$ 0 | R$ 10 | R$ 25 | R$ 35 | R$ 35 | R$ 20 | R$ 20 |

**Tabela simplificada (6 regras)**

| Condição | R1 | R2 | R3 | R4 | R5 (antigas R5 e R6) | R6 (antigas R7 e R8) |
|---|---|---|---|---|---|---|
| Compra ≥ R$ 200,00 | Sim | Sim | Sim | Sim | Não | Não |
| Cliente cadastrado | Sim | Sim | Não | Não | - | - |
| Interior | Sim | Não | Não | Sim | Sim | Não |
| **Frete** | R$ 15 | R$ 0 | R$ 10 | R$ 25 | R$ 35 | R$ 20 |

**Justificativa da simplificação:** abaixo de R$ 200,00, o cadastro não altera o frete. Por isso R5 e R6 (cadastrado ou não, com interior) dão R$ 35 e foram unidas. R7 e R8 (cadastrado ou não, sem interior) dão R$ 20 e também foram unidas.

### DT2: reserva de equipamento

**Tabela completa (8 regras)**

| Condição | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|---|---|---|---|---|---|---|---|---|
| É professor? | Sim | Sim | Sim | Sim | Não | Não | Não | Não |
| Equipamento disponível? | Sim | Sim | Não | Não | Sim | Sim | Não | Não |
| Antecedência ≥ 24h? | Sim | Não | Sim | Não | Sim | Não | Sim | Não |
| **Status do pedido** | Aprovada | Coordenação | Recusada | Recusada | Coordenação | Coordenação | Recusada | Recusada |

**Tabela simplificada (4 regras)**

| Condição | R1 | R2 | R3 (antigas R5 e R6) | R4 (antigas R3, R4, R7 e R8) |
|---|---|---|---|---|
| É professor? | Sim | Sim | Não | - |
| Equipamento disponível? | Sim | Sim | Sim | Não |
| Antecedência ≥ 24h? | Sim | Não | - | - |
| **Status do pedido** | Aprovada | Coordenação | Coordenação | Recusada |

**Justificativa da simplificação:** para aluno com equipamento disponível, a antecedência não muda o resultado (sempre Coordenação), então R5 e R6 foram unidas. Para equipamento indisponível, o resultado é sempre Recusada, independentemente de quem pediu ou da antecedência, então R3, R4, R7 e R8 foram unidas.