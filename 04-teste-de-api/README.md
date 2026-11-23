# 04: Teste de API

Automação de testes da API ServeRest (https://serverest.dev) no Postman, com dados dinâmicos, encadeamento entre requisições e limpeza ao final.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| [conceitos-api.md](conceitos-api.md) | Conceitos de API, métodos HTTP, status codes, body e headers |
| [ServeRest.postman_collection.json](ServeRest.postman_collection.json) | Coleção exportada do Postman, pronta para importar |

## Resultado da última execução

Execução pelo Runner do Postman: **28 testes passaram, 0 falharam**, em 12 requisições.

![Resultado do Runner](evidencias/runner-resultado.png)

## Requisições

| Requisição | Cenário | Método e rota | Status esperado | Status obtido | Resultado |
|---|---|---|---|---|---|
| login_valido | Caminho feliz | POST /login | 200 | 200 | Passou |
| login_invalido_senha_errada | Autenticação | POST /login | 401 | 401 | Passou |
| cadastro_valido | Caminho feliz | POST /usuarios | 201 | 201 | Passou |
| cadastro_invalido_campo_obrigatorio_em_branco | Dado inválido | POST /usuarios | 400 | 400 | Passou |
| lista_de_usuarios | Caminho feliz | GET /usuarios | 200 | 200 | Passou |
| usuario_id_inexistente | Recurso inexistente | GET /usuarios/{id} | 400 | 400 | Passou |
| cadastro_de_produto_sem_token | Autenticação | POST /produtos | 401 | 401 | Passou |
| cadastro_de_produto_com_token_valido | Caminho feliz | POST /produtos | 201 | 201 | Passou |
| produto_id_inexistente | Recurso inexistente | GET /produtos/{id} | 400 | 400 | Passou |
| lista_produtos | Caminho feliz | GET /produtos | 200 | 200 | Passou |
| excluir_produto_valido | Limpeza | DELETE /produtos/{id} | 200 | 200 | Passou |
| excluir_usuario_valido | Limpeza | DELETE /usuarios/{id} | 200 | 200 | Passou |

## Como a automação funciona

- **Dados únicos:** o e-mail do cadastro é gerado a cada execução, para o teste não depender de dados que já existem.
- **Encadeamento:** o token do login e os IDs criados são salvos em variáveis e reutilizados nas requisições seguintes.
- **Limpeza:** as requisições de DELETE rodam por último e removem o usuário e o produto criados.

## Limitações conhecidas

- Se uma requisição falhar no meio, a limpeza pode não rodar e deixar dados criados. A melhoria seria executar a limpeza mesmo em caso de falha.
- O resultado das requisições de ID inexistente depende do formato do ID usado na documentação da ServeRest.