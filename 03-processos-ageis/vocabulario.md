# Vocabulário: Processos Ágeis

## Sprint

* **O que é:** É um ciclo curto e com prazo fixo em que o time trabalha focado para entregar uma parte funcional e testada do produto.

* **Exemplo:** Uma Sprint de uma semana, duração escolhida pelo próprio time, para desenvolver e validar todo o fluxo de reserva de projetores pelos professores.

## Product Backlog

* **O que é:** É a lista oficial e priorizada de todas as funcionalidades, melhorias e correções que o produto precisa, sempre ordenada pelo Product Owner de acordo com o que traz mais valor primeiro.

* **Exemplo:** A fila de demandas do sistema de agendamento da escola, trazendo no topo "impedir reserva duplicada no mesmo turno" e, mais abaixo, "filtrar equipamentos por sala" e "exportar relatório mensal".

## Sprint Backlog

* **O que é:** É o conjunto de itens selecionados do Product Backlog para a Sprint atual, acompanhado do plano técnico detalhado de como o time vai executá-los.

* **Exemplo:** Para entregar a tela de solicitação na semana, o time quebra o objetivo em tarefas técnicas da nossa stack: estruturar o layout em Tailwind CSS, escrever a função de envio no Google Apps Script e testar a gravação na planilha do Google Sheets.

## Sprint Goal (Meta da Sprint)

* **O que é:** É o objetivo central e único da Sprint, definido durante a Sprint Planning, que dá propósito ao trabalho do time e ajuda a tomar decisões caso surja algum imprevisto técnico.

* **Exemplo:** "Garantir que os professores consigam consultar a disponibilidade e reservar caixas de som pelo celular sem conflitos de horário."

## DoD (Definição de Pronto)

* **O que é:** É o checklist de critérios de qualidade que o time estabelece para garantir que uma entrega esteja realmente finalizada e pronta para uso.

* **Exemplo:** Uma tarefa só é considerada pronta quando o formulário funciona no celular, grava os dados corretamente no Google Sheets, bloqueia conflitos e passa pela validação de QA sem falhas.

## Incremento

* **O que é:** É o resultado prático e funcional entregue ao final de uma Sprint, somando as novas funcionalidades testadas a tudo o que já existia no produto.

* **Exemplo:** A consulta visual de horários e equipamentos já reservados por turno funcionando e integrada ao formulário de solicitação de reserva entregue na Sprint anterior.

## WIP (Work In Progress)

* **O que é:** É o limite máximo de tarefas que podem estar sendo executadas simultaneamente em uma etapa do fluxo, evitando que o time comece muita coisa sem terminar nada.

* **Exemplo:** Restringir a coluna "Em teste" a no máximo 1 tarefa por vez, evitando que o desenvolvedor acumule entregas pendentes antes de a validação atual ser concluída.

## Slot

* **O que é:** É cada vaga disponível dentro do limite de WIP de uma coluna no quadro Kanban, sinalizando quando o time tem capacidade livre para puxar uma nova demanda.

* **Exemplo:** Como a coluna "Em teste" tem 1 slot e já está ocupado, a próxima tarefa aguarda na fila até liberar.

## Sprint Retrospective (Retrospectiva)

* **O que é:** É a reunião exclusiva do time ao encerrar uma Sprint para analisar o que funcionou bem na rotina de trabalho e definir melhorias práticas para a próxima Sprint.

* **Exemplo:** Ao final da Sprint, o time percebe que houve retrabalho porque os nomes das colunas do Google Sheets mudaram no meio da semana e decide congelar a estrutura da planilha antes de iniciar o código na próxima Sprint.

## Daily Scrum

* **O que é:** É uma reunião rápida e diária de no máximo 15 minutos para os desenvolvedores sincronizarem o progresso rumo à meta da Sprint e ajustarem o plano do dia diante de bloqueios.

* **Exemplo:** Na reunião de 15 minutos logo no início da manhã, um desenvolvedor relata um erro de permissão no Google Apps Script e o time ajusta o plano do dia para destravar o acesso antes de seguir com os testes da interface.