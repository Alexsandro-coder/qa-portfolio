# Técnicas de caixa-preta

## 1. Partição de equivalência

### Sistema: cadastro de instrutor, campo "idade" (aceita de 18 a 65)

| Partição | faixa | tipo | valor_de_teste | resultado esperado |
|---|---|---|---|---|
| p1 | menor que 18 | invalido | 16 | mensagem: "idade mínima permitida e de 18 anos" |  
| p2 | de 18 a 65 | valido | 32 |  mensagem: "Cadastro realizado" |
| p3 | maior que 65 | invalido | 70 |  mensagem: "Idade máxima permitida e de 65 anos" |

**Observação:** 32 anos foi escolhido devido esta mais próximo do centro da idade permitida, Não foram utilizados as idades 18 e 65 por se tratarem de valores limite (bordas), os quais já fazem parte do escopo específico de Análise de Valor Limite (AVL)



### Sistema: cadastro de senha, campo "senha" (aceita de 8 a 20 caracteres, com pelo menos 1 numero)

| Partição | faixa | tipo | valor_de_teste | resultado esperado | 
|---|---|---|---|---|
| p1 | menor que 8 |invalido | 123abc | mensagem: "senha pequena, mínimo de 8 caracteres" | 
| p2 | de 8 a 20 com numero| valido | r2026claro5539 | mensagem: " senha cadastrada com sucesso" |
| p3 | maior que 20 | invalido | batatinhafrita123batatinhafrita123 | mensagem: "senha excede o limite, máximo de 20 caracteres" |
| p4 | de 8 a 20 sem numero | invalido | abcdefghijklmno | mensagem: "senha deve conter ao menos 1 numero" 

**Observação:** A senha de 14 caracteres (r2026claro5539) foi escolhida como padrão empresarial, seguindo a estrutura: [setor: r] + [ano: 2026] + [produto: claro] + [matrícula: 5539], p2 e p4 têm o mesmo tamanho e diferem apenas pela presença de número. Não foram utilizados os tamanhos de 8 ou 20 caracteres por se tratarem de valores limite (bordas), os quais já fazem parte do escopo específico de Análise de Valor Limite (AVL)


### Sistema: desconto de compras, (até R$ 100,00 = 0%; de R$ 100,01 a R$ 300,00 = 5%; acima de R$ 300,00 = 10%)
| Partição | faixa | tipo | valor_de_teste | resultado esperado |
|---|---|---|---|---|
| p1 | ate 100,00 | 0% de desconto | 99,00 | “valor cobrado integralmente, sem desconto” | 
| p2 | entre 100,01 e 300,00 | 5% de desconto | 150,00 | mensagem: "você ganhou 5% de desconto" | 
| p3 | acima de 300,00 | 10% de desconto | 310,00 | mensagem: "você ganhou 10% de desconto" |

**Observação:** O valor de 150,00 escolhido por esta no meio da faixa de valores de 5% , Não foram utilizados os valores 100,01 e 300,01 por se tratarem de valores limite (bordas), os quais já fazem parte do escopo específico de Análise de Valor Limite (AVL)
