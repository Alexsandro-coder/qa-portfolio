# Roteiro de testes: Listagem

## 1. Objetivo
Verificar a exibição da lista de produtos, o funcionamento das ordenações (por nome e por preço), a navegação para os detalhes de um item e a integridade das imagens e nomenclaturas do catálogo no SauceDemo.

## 2. Pré-condições gerais
- Navegador Chrome (versão 156) em Windows 11.
- Acesso a saucedemo.com.
- Senha de todos os usuários de teste: `secret_sauce`.

## 3. Massa de dados
| Usuário | Senha | Uso |
|---|---|---|
| standard_user | secret_sauce | Validação de ordenação, navegação e inspeção de catálogo |

## 4. Ordem de execução
| Ordem | Caso | Descrição curta | Depende de |
|---|---|---|---|
| 1 | VF-07 | Ordenação por Price (low to high) | Nenhum |
| 2 | VF-08 | Ordenação por Price (high to low) | VF-07 |
| 3 | VF-09 | Ordenação por Name (A to Z) | Nenhum |
| 4 | VF-10 | Ordenação por Name (Z to A) | VF-09 |
| 5 | VF-11 | Navegação para página do produto | Nenhum |
| 6 | VF-12 | Verificação geral de imagens e preços | Nenhum |
| 7 | VF-13 | Imagem da Sauce Labs Bolt T-Shirt | VF-12 |
| 8 | VF-14 | Padrão de nome da Test.allTheThings() | VF-12 |

## 5. Critério de saída
O bloco de listagem é considerado executado quando todos os 8 casos (VF-07 a VF-14) tiverem status preenchido (Passou ou Falhou) e os bugs vinculados (BUG-02 e BUG-03) estiverem registrados.

## 6. Observações
- A ordem começa pelos testes de ordenação e navegação principal (VF-07 a VF-12) e deixa os casos VF-13 e VF-14 por último por serem defeitos já conhecidos, evitando que falhas visuais bloqueiem o fluxo da suíte.
- Os casos VF-07 a VF-14 estão em `verificacoes-funcionais.md`. Este roteiro apenas organiza a ordem e os dados, sem repetir o detalhamento dos passos.