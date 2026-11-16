# Guia de Estudos: Scrum

Framework de trabalho em ciclos curtos (Sprints), baseado em transparência, inspeção e adaptação para atingir uma meta.

---

## Papéis

**Product Owner** - É a pessoa responsável por comunicar metas, ordenar o Product Backlog e decidir o que entra primeiro em ordem de importância. Ele atua como a ponte com os stakeholders, e a forma como trabalha no dia a dia pode mudar conforme a cultura da empresa.
* **EX:** Validando regras de negócio de agendamentos para moldar o sistema ao redor.

**Scrum Master** - É a pessoa responsável por cultivar o Scrum na empresa e ser líder servidor em várias frentes, como o Scrum Team, Product Owner e a organização como um todo.
* **EX:** Buscando informações sobre o processo e gargalos do desenvolvimento.

**Developers** - São os profissionais que decidem como fazer o trabalho e entregam o Incremento pronto ao final de cada etapa, aderindo sempre à Definição de Pronto.
* **EX:** Estruturando o banco de dados, criando as telas e programando a lógica do sistema de agendamentos.

---

## Eventos

**Sprint Planning** - É uma reunião colaborativa do Scrum Team realizada antes de iniciar a Sprint, onde abordam tópicos importantes para a etapa do projeto e definem o que será realizado.
* **EX:** Reunião para decidir quais itens do Product Backlog entram na Sprint, com a meta definida e as tarefas da semana divididas.

**Daily Scrum** - É uma reunião de 15 minutos realizada todos os dias úteis da Sprint a fim de inspecionar o progresso rumo à meta da Sprint, podendo ajustar o plano conforme o necessário.
* **EX:** Reunião rápida de manhã para verificar se o plano do dia continua no caminho certo rumo à meta da Sprint e ajustar as tarefas se surgir algum imprevisto.

**Sprint Review** - É uma reunião colaborativa feita perto do fim da Sprint para inspecionar o Incremento entregue junto com os stakeholders. Com base nas informações e feedbacks, é determinado o que fazer em seguida para adaptar o produto.
* **EX:** Apresentação do que foi construído na Sprint para validar com os interessados e decidir os próximos passos do produto.

**Sprint Retrospective** - É a última reunião realizada, contando apenas com a participação do Scrum Team (sem stakeholders), com foco em melhorar o próprio processo. O time discute o que deu certo durante a Sprint, os problemas enfrentados e como foram (ou não) resolvidos, determinando mudanças para aumentar a qualidade e a eficácia da próxima Sprint.
* **EX:** O time percebe que houve atraso nos testes do sistema de agendamento e decide criar uma rotina de revisão diária de código para aumentar a qualidade na próxima Sprint.

---

## Artefatos

**Product Backlog** - É uma lista dinâmica que existe o tempo todo e é mantida pelo Product Owner com os itens necessários para melhorar o produto. Ele reúne problemas maiores quebrados em pedaços menores e mais precisos, dos quais uma parte é escolhida durante a Sprint Planning.
* **EX:** Lista ordenada do sistema de agendamentos contendo no topo "cadastrar cliente" e "escolher horário", e mais abaixo "enviar lembrete por e-mail".

**Sprint Backlog** - É o conjunto dos itens escolhidos do Product Backlog para a Sprint, somado ao plano do time para entregá-los. Esse plano é criado pelos próprios Developers para atingirem a meta da Sprint e é detalhado o suficiente para ser acompanhado na Daily Scrum.
* **EX:** Os Developers escolhem o item "cadastrar cliente" para a Sprint e criam a lista de tarefas técnicas da semana: criar tabela no banco, desenvolver tela de cadastro e testar validações.

**Incremento** - É uma nova etapa ou funcionalidade do produto que foi totalmente finalizada, testada e está pronta para ser usada pelo cliente. Ele se soma ao Incremento anterior e cumpre a Definição de Pronto.
* **EX:** No sistema de agendamentos, é a funcionalidade de "marcar horário" concluída, testada e integrada ao cadastro de clientes que já existia na etapa anterior, pronta para o usuário utilizar.
