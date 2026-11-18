# API (Application Programming Interface)

- **O que é?** - API é uma interface que permite que dois sistemas conversem entre si, escondendo a complexidade interna.
- **O que faz?** - Recebe uma requisição, processa e devolve uma resposta, sem o cliente precisar conhecer o banco ou o código do servidor.

---

## Requisição e Resposta

- **O que o cliente envia para o servidor?** - O cliente realiza uma requisição (*request*), seja para buscar, enviar ou alterar dados.
- **O que o servidor devolve?** - O servidor processa a requisição, consulta os dados e devolve um *status code* e, em geral, um JSON.
- **Exemplo no sistema de agendamento:** Quando um professor preenche o formulário para reservar um projetor e clica em confirmar, o navegador envia uma requisição com os dados da reserva (equipamento, data e horário) para o servidor. O servidor verifica a disponibilidade, salva o agendamento na planilha e devolve o *status code* `201` junto com um JSON confirmando a reserva.

---

## Métodos HTTP

- **GET** - Busca informações (ex: listar os equipamentos disponíveis para agendamento).
- **POST** - Adiciona informações novas (ex: criar uma nova reserva de projetor).
- **HEAD** - Busca metadados (ex: verificar o tamanho de um arquivo e a data de atualização).
- **PUT** - Atualiza um item existente por inteiro ou cria um novo se ele não existir (ex: atualizar uma reserva já feita com todos os dados).
- **DELETE** - Apaga um item específico (ex: cancelar e remover uma reserva existente).
- **PATCH** - Atualiza só alguns campos do item (ex: alterar apenas o horário de devolução de uma reserva).

---

## Status Codes

- **200** - A solicitação foi bem-sucedida.
- **201** - A requisição foi bem-sucedida e um novo recurso foi criado.
- **400** - O servidor não pode processar a informação por erro do cliente (ex: erro de sintaxe).
- **401** - Falta de autenticação ou credencial inválida (ex: login sem token).
- **403** - O cliente está autenticado, mas não tem permissão para acessar aquele recurso.
- **404** - O recurso solicitado não existe.
- **500** - Falha interna do servidor.

---

## Body e Headers

- **O que é Body?** - É o conteúdo principal da mensagem onde vão os dados reais (geralmente em JSON). Funciona como a carta que vai dentro do envelope.
- **O que é Headers?** - São os metadados da requisição (como a chave de acesso, tipo de arquivo ou idioma). Fica no início da requisição, antes do *body*, e funciona como o envelope de uma carta.

### Exemplo de JSON (Body):
```json
{
  "id": 17,
  "equipamento": "Projetor 01",
  "data": "2026-11-20",
  "horario": "14:00",
  "status": "aprovada"
}
```

### Exemplo de Headers:
```http
Authorization: Bearer chave_123
Content-Type: application/json
Accept-Language: pt-BR
```