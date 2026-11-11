# Relatório de testes: SauceDemo

## 1. Resumo

- **Total de verificações executadas:** 32
- **Passou:** 25
- **Falhou:** 7 (VF-06, VF-22, VF-29, VF-31 e VF-32 no `problem_user`; VF-13 e VF-14 no `standard_user`)

---

## 2. Resultados por bloco

| Bloco | Total | Passou | Falhou |
|---|---|---|---|
| **Login** | 6 | 5 | 1 |
| **Listagem** | 8 | 6 | 2 |
| **Carrinho** | 8 | 7 | 1 |
| **Checkout** | 6 | 6 | 0 |
| **Bugs de propósito** | 4 | 1 | 3 |
| **TOTAL** | **32** | **25** | **7** |

---

## 3. Bugs encontrados

| ID | Título | Severidade | Status |
|---|---|---|---|
| **BUG-01** | Imagens incorretas na listagem de produtos para problem_user | Média | Aberto |
| **BUG-02** | Imagem de produto divergente da sua descrição | Alta | Aberto |
| **BUG-03** | Nome foge do padrão "Sauce Labs ..." | Baixa | Aberto |
| **BUG-04** | Produtos que não puderam ser adicionados no carrinho | Alta | Aberto |
| **BUG-05** | Remoção travada na listagem principal para problem_user | Média | Aberto |
| **BUG-06** | Checkout com campos de espaços | Alta | Aberto |
| **BUG-07** | Checkout com caracteres especiais | Alta | A confirmar (depende de especificação) |
| **BUG-08** | Checkout concluído com carrinho vazio | Alta | Aberto |

---

## 4. Sessões exploratórias

- **Sessão 1 (Checkout com campos de espaços):**
  - *Resultado:* **Falha / Defeito encontrado.** O Checkout aceitou os campos First Name, Last Name e Postal Code contendo apenas espaços em branco e avançou para a tela *Checkout: Overview* sem exibir mensagem de campo obrigatório.
- **Sessão 2 (Checkout com caracteres especiais):**
  - *Resultado:* **Aceito; a confirmar se é defeito (ver dúvida no exploratório).** O Checkout aceitou caracteres especiais nos campos do formulário e avançou para *Checkout: Overview*. É necessário confirmar com a especificação se a regra de negócio permite ou restringe caracteres especiais nesses campos.
- **Sessão 3 (Checkout com carrinho vazio):**
  - *Resultado:* **Falha / Defeito encontrado.** O Checkout aceitou o carrinho com 0 itens, avançou para *Checkout: Overview* e o pedido foi concluído com carrinho vazio (*Checkout: Complete!*).

---

## 5. Conclusão

O fluxo principal de login, carrinho e checkout do `standard_user` funcionou; os defeitos encontrados atingem a listagem (imagens e nomes), a adição de itens para o `problem_user` e a validação do checkout.