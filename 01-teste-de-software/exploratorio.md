## Sessão 1: Checkout com campos de espaços

- **Missão:** tentar quebrar o checkout com campos contendo só espaços.
- **Tempo:** 5 min (achado encontrado logo no início; sessão encerrada ao confirmar o defeito)
- **Testado:** First Name com "   ", Last Name com "   ", Postal Code com "     ".
- **Achados:** O Checkout aceitou todos os campos com o espaço em branco e ao clicar em continue , a tela avançou para Checkout: Overview.
- **Dúvidas:** a regra de negócio aceita espaços? Confirmar com a especificação.

## Sessão 2: Checkout com caracteres especiais

- **Missão:** tentar quebrar o checkout com campos contendo só caracteres especiais.
- **Tempo:** 5 min (achado encontrado logo no início; sessão encerrada ao confirmar o defeito)
- **Testado:** First Name com "!@#", Last Name com "!@#", Postal Code com "!@#".
- **Achados:** O Checkout aceitou todos os campos com caracteres especiais e e ao clicar em continue , a tela avançou para Checkout: Overview.
- **Dúvidas:** a regra de negócio aceita caracteres especiais? Confirmar com a especificação.

## Sessão 3: Checkout com carrinho vazio
- **Missão:** tentar quebrar o  checkout com o carrinho vazio.
- **Tempo** 5 min (achado encontrado logo no início; sessão encerrada ao confirmar o defeito)
- **Testado** Carrinho com (0) itens, First Name com "jose", Last Name com "Maria", Postal Code com "00000".
- **Achados** O Checkout aceitou o carrinho vazio e e ao clicar em continue , a tela avançou para Checkout: Overview e na mesma tela ao clicar em Finish avançou para Checkout: Complete!.
- **Dúvidas** a regra de negócio aceita carrinho vazio? Confirmar com a especificação.