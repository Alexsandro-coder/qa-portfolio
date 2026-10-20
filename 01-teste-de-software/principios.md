# Princípios

## 1. O teste mostra a presença de defeitos, não a sua ausência
*   **O que é:** Testar um sistema serve para provar que existem bugs nele, mas passar em todos os testes não garante que o software está 100% perfeito ou livre de erros.
*   **Exemplo:** Executar 50 testes na tela de agendamento de equipamentos e ver todos passarem com sucesso. Isso prova que esses 50 cenários funcionam, mas não garante que o sistema não vá quebrar ao tentar reservar 1.000 equipamentos de uma só vez.
*   **Não confundir com:** Dizer que o software está pronto e sem nenhum bug só porque o time de QA terminou a bateria de testes planejada.

## 2. Testes exaustivos são impossíveis
*   **O que é:** É inviável testar absolutamente todas as combinações de dados, botões e caminhos de um software, porque o tempo e os recursos do projeto acabariam antes.
*   **Exemplo:** Um formulário com 10 campos de texto e várias caixas de seleção gera milhões de combinações possíveis; em vez de testar tudo, a equipe seleciona os cenários mais importantes e de maior risco.
*   **Não confundir com:** Fazer testes de qualquer jeito ou deixar de cobrir o sistema. O objetivo é priorizar com base no risco e não tentar testar até o infinito.

## 3. Teste precoce economiza tempo e dinheiro
*   **O que é:** É começar as atividades de teste o quanto antes no projeto, analisando regras e documentos antes mesmo de o código ser escrito.
*   **Exemplo:** Encontrar um erro na regra de agendamento durante a leitura da documentação e corrigir em minutos editando o texto, em vez de esperar o desenvolvedor programar tudo errado para depois ter que refazer.
*   **Não confundir com:** Teste de regressão, que acontece lá na frente quando o código já está pronto para garantir que uma alteração nova não quebrou nada antigo.

## 4. Agrupamento de defeitos
*   **O que é:** É o fenômeno onde a grande maioria dos bugs do sistema se concentra em poucas partes específicas do código, geralmente nos módulos mais complexos.
*   **Exemplo:** Em um sistema escolar, 80% dos problemas relatados ficarem concentrados apenas no módulo de cálculo de médias e recuperação, enquanto a tela de cadastro de alunos quase nunca falha.
*   **Não confundir com:** Achar que os erros ficam espalhados de forma igual por todo o sistema. Onde tem complexidade ou muitas mexidas, costuma ter mais bug.

## 5. Cuidado com o paradoxo do pesticida
*   **O que é:** É o fato de que rodar repetidamente os mesmos cenários de teste sem atualizar nada faz com que eles parem de encontrar novos bugs com o passar do tempo.
*   **Exemplo:** Rodar a mesma bateria automatizada na tela de login por 6 meses sem dar erro, mas o sistema quebrar no primeiro dia em que um usuário tenta logar com e-mail contendo caracteres especiais.
*   **Não confundir com:** Teste de confirmação. O teste de confirmação repete o teste antigo só para ver se o bug foi corrigido; já o paradoxo alerta que você precisa criar testes *novos* para achar novos problemas.

## 6. O teste depende do contexto
*   **O que é:** Significa que a forma de planejar e executar os testes muda completamente de acordo com o tipo, o risco e a finalidade de cada software.
*   **Exemplo:** Testar um app simples de lista de tarefas exige um processo leve e focado em usabilidade, enquanto testar um software médico ou bancário exige testes extremamente rigorosos de segurança e precisão.
*   **Não confundir com:** Achar que existe uma "receita de bolo" ou uma lista fixa de testes que serve para qualquer projeto de software do mercado.

## 7. A falácia da ausência de erros
*   **O que é:** É o engano de achar que entregar um sistema sem bugs técnicos é suficiente, sendo que ele pode continuar sendo inútil se não resolver a necessidade real do usuário.
*   **Exemplo:** Entregar uma tela de reservas sem nenhum erro de código e com 100% dos testes aprovados, mas o fluxo exigir 15 etapas manuais e o usuário desistir de usar a ferramenta por ser burocrática demais.
*   **Não confundir com:** Verificação técnica. Corrigir bugs garante que o sistema segue as regras do papel, mas só a validação garante que o produto é realmente útil para a rotina do cliente.

