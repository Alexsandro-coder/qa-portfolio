# Guia de Estudos: Kanban

É um método para gerenciar e melhorar o fluxo de trabalho de forma contínua. Na prática, o Kanban ajuda o time a visualizar todas as tarefas em um quadro, limitar a quantidade de trabalho em andamento e identificar gargalos para entregar com mais previsibilidade.

---

## 1. Colunas do quadro

| A fazer | Em andamento | Em teste | Concluído |
| :--- | :--- | :--- | :--- |
| Tarefas priorizadas aguardando início | Tarefas sendo desenvolvidas no momento | Tarefas em validação pelo QA | Tarefas testadas e finalizadas |

---

## 2. Limite de WIP (Work In Progress)

É uma regra da Definição de Fluxo de Trabalho (DoW) que define o número máximo de tarefas permitidas ao mesmo tempo em uma coluna, controlado por **slots** (espaços disponíveis). Sem esse limite, o time começa várias tarefas ao mesmo tempo e termina poucas, gerando acúmulo e perda de foco. Com o limite ativo, ninguém puxa um novo item enquanto todos os slots estiverem ocupados, incentivando a equipe a finalizar o que já começou.

- **Exemplo:** Limitar a coluna **Em andamento** a no máximo 2 slots; enquanto os 2 estiverem ocupados, nenhuma nova tarefa sai de **A fazer**.

---

## 3. Fluxo contínuo

Diferente do Scrum, que trabalha em ciclos fechados e com prazo fixo (Sprints), o Kanban opera em **fluxo contínuo**. Nesse modelo, as demandas não são acumuladas em lotes semanais: assim que uma tarefa avança e libera um **slot**, o time puxa o próximo item mais prioritário da coluna **A fazer**, mantendo as entregas constantes e sem interrupções de ciclo.

---

## 4. Comparação: Kanban x Scrum

| Critério | Kanban | Scrum |
| :--- | :--- | :--- |
| **Ciclo** | Fluxo contínuo (sem prazo fixo de entrega) | Sprints fixas (ciclos de 1 a 4 semanas) |
| **Papéis** | Não define papéis obrigatórios | Define papéis específicos (PO, Scrum Master e Developers) |
| **Reuniões** | Não tem eventos obrigatórios | Possui eventos fixos (Planning, Daily, Review e Retrospective) |
| **Mudança** | Prioridades e tarefas podem ser alteradas a qualquer momento, desde que haja slot livre no WIP | Mudanças durante a Sprint são evitadas; o escopo é ajustado entre Sprints |

---

## 5. Exemplo prático: Sistema de Agendamento Audiovisual

Veja como o cartão **"Bloquear reserva duplicada de equipamento no mesmo turno"** percorre o quadro até a entrega final, considerando limites de WIP diferentes por etapa (2 slots para desenvolvimento e 1 slot para testes, evitando acúmulo na validação):

1. **A fazer:** O cartão entra no topo da fila como prioridade para evitar que dois professores reservem o mesmo projetor ou caixa de som na mesma data e aula/turno.
2. **Em andamento (Limite de WIP: 2):** Com 1 slot livre na etapa de desenvolvimento, a tarefa é puxada para programar a verificação de disponibilidade no **Google Apps Script** antes de gravar a linha no **Google Sheets** e exibir o alerta na interface (**JavaScript/Tailwind CSS**).
3. **Em teste (Limite de WIP: 1):** Com o slot de validação livre, o cartão avança para o QA testar os critérios de aceitação. Além de checar horários livres e reservas no mesmo turno, o QA simula o **envio simultâneo** — quando dois professores clicam em "Reservar" no mesmo segundo para pegar o último projetor disponível — garantindo que o sistema bloqueie a segunda requisição e não grave duplicidade na planilha.
4. **Concluído:** Após passar nos testes sem falhas, o cartão chega à última coluna e libera o slot no fluxo para a próxima melhoria do sistema entrar.