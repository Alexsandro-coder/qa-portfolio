# Glossário

## Teste dinâmico
*   **O que é:** É quando a gente roda o software de verdade para ver como ele se comporta e achar as falhas em tempo de execução.
*   **Exemplo:** Preencher a tela de login com usuário e senha corretos, clicar no botão e ver se o sistema abre a página inicial com sucesso.
*   **Não confundir com:** Teste estático, que analisa os artefatos de desenvolvimento sem rodar o código.

## Teste estático
*   **O que é:** É analisar qualquer documento ou o próprio código do sistema sem precisar executar o programa, caçando os defeitos direto na estrutura.
*   **Exemplo:** Fazer um code review com um colega de equipe para revisar as linhas de código que foram escritas para o sistema.
*   **Não confundir com:** Teste dinâmico, que obrigatoriamente precisa colocar o software para rodar.

## Nível de teste
*   **O que é:** É o grupo de atividades de teste que ficam juntas e estão ligadas a uma etapa específica do desenvolvimento do projeto.
*   **Exemplo:** Testar uma função isolada do código (componente), depois testar as telas juntas (sistema) e por fim o cliente validar o software (aceitação).
*   **Não confundir com:** Tipos de teste, que focam no objetivo da qualidade (como funcional ou desempenho) e não na fase do desenvolvimento.

## Ciclo de vida de desenvolvimento
*   **O que é:** É o modelo que define como as etapas de criação do software são organizadas pela equipe do início ao fim do projeto.
*   **Exemplo:** Trabalhar com o modelo cascata (onde uma fase só começa quando a outra termina) ou com o modelo ágil (dividido em sprints de entrega rápida).
*   **Não confundir com:** Ciclo de vida do teste, que cuida apenas das fases e tarefas específicas da equipe de QA.

## Objetivos de teste
*   **O que é:** São as metas e os propósitos que a gente quer alcançar quando decide realizar os testes no sistema.
*   **Exemplo:** Encontrar defeitos na tela de agendamento de equipamentos antes que o cliente pegue a versão final.
*   **Não confundir com:** Nível de teste, que aponta em qual camada ou fase o teste vai acontecer, enquanto o objetivo explica a razão de testar.

## Depuração
*   **O que é:** É o trabalho técnico do desenvolvedor para revirar o código, achar onde está a raiz do problema e consertar o bug que foi relatado.
*   **Exemplo:** O programador colocar breakpoints na linha do cálculo de horas, ver que a variável veio errada e corrigir o sinal matemático.
*   **Não confundir com:** Teste de software, que serve para rodar o sistema e levantar as falhas, sem mexer ou corrigir o código-fonte.

## Erro
*   **O que é:** É o engano ou o vacilo que a pessoa comete na sua cabeça enquanto está planejando ou escrevendo alguma parte do projeto.
*   **Exemplo:** O desenvolvedor se confundir na regra de negócio e achar que "maior de idade" significa ter mais de 18 anos completos (esquecendo de incluir quem tem exatamente 18).
*   **Não confundir com:** Defeito, que é a marca física ou a linha errada que ficou salva no arquivo de código por causa desse engano.

## Defeito
*   **O que é:** É a falha escrita no código ou no documento, sendo a consequência direta do erro que o ser humano cometeu.
*   **Exemplo:** O desenvolvedor digitar `if (idade > 18)` nas linhas do sistema, quando a regra correta exigia usar `>= 18`.
*   **Não confundir com:** Falha, que é o problema se manifestando na tela quando o programa roda e esbarra nesse ponto específico.

## Falha
*   **O que é:** É o comportamento errado que aparece na tela do usuário quando o sistema em execução passa por cima de um defeito oculto.
*   **Exemplo:** Um jovem de exatamente 18 anos tentar fazer o cadastro no sistema e ser rejeitado com uma mensagem dizendo que ele não tem permissão para entrar.
*   **Não confundir com:** Defeito, que fica guardado quietinho no código e só gera a falha se aquela linha específica for usada na prática.

## Teste de confirmação
*   **O que é:** É o teste que a gente faz focado em rodar de novo o mesmo cenário que tinha quebrado, só para garantir que o conserto do desenvolvedor funcionou.
*   **Exemplo:** Testar o cadastro com um usuário de 18 anos (que antes dava erro) para ver se agora ele consegue criar a conta normalmente.
*   **Não confundir com:** Teste de regressão, que vai checar se as outras partes do sistema continuam funcionando bem depois dessa mexida.

## Teste de regressão
*   **O que é:** É rodar testes nas partes do sistema que não sofreram alterações para garantir que o código novo não estragou o que já estava funcionando.
*   **Exemplo:** Depois de ajustar a regra de idade no cadastro, testar o fluxo de login e a tela de listagem de equipamentos para ver se nada quebrou por tabela.
*   **Não confundir com:** Teste de confirmação, que só olha para o ponto exato que foi corrigido para fechar o chamado do bug.

## QA
*   **O que é:** É a garantia da qualidade focada na melhoria dos processos de trabalho, agindo antes do código ficar pronto para prevenir os problemas.
*   **Exemplo:** Criar uma regra onde nenhuma tarefa pode ser programada se os critérios de aceitação não estiverem muito claros para o time.
*   **Não confundir com:** QC, que trabalha olhando diretamente para o software pronto para caçar e apontar os problemas.

## QC
*   **O que é:** É o controle de qualidade focado em examinar o produto final de forma prática para avaliar se ele cumpre o que foi pedido.
*   **Exemplo:** O analista pegar a versão final liberada e executar o roteiro de testes para validar as funcionalidades.
*   **Não confundir com:** A correção de bugs feita pelos desenvolvedores. O QC descobre e relata os problemas, mas quem altera o código é o programador.

## Análise de teste
*   **O que é:** É a fase onde a gente estuda os documentos do projeto para entender as regras e definir exatamente o que precisa ser testado.
*   **Exemplo:** Analisar o documento da tela de login e determinar que é necessário testar as condições de: login correto, senha errada, campo vazio e bloqueio após 3 tentativas inválidas.
*   **Não confundir com:** Modelagem de teste, que pega essas ideias de teste e cria o passo a passo detalhado com os dados práticos.

## Modelagem de teste
*   **O que é:** É a atividade que pega as ideias gerais levantadas na análise e monta a estrutura prática de como o teste vai acontecer.
*   **Exemplo:** Pegar a condição "senha errada" e criar o Caso de Teste 01 com os dados: Usuário = `teste@audiovisual.com`, Senha = `123` e Resultado esperado = Exibir o alerta "Senha incorreta".
*   **Não confundir com:** Análise de teste, que fica apenas no mapeamento macro das regras e dos riscos sem desenhar os passos do teste.

## Processo de teste
*   **O que é:** É a estrutura que divide o trabalho de testes em 7 atividades sequenciais para garantir a organização do dia a dia:
    *   **Planejamento:** Decidir testar o cadastro de pedidos e as regras de conflito de horário no sistema de equipamentos audiovisuais.
    *   **Monitoramento e Controle:** Avaliar se o time vai conseguir rodar todos os testes no prazo e ajustar as tarefas se houver atraso.
    *   **Análise:** Estudar a regra de devolução de projetores e definir que precisamos testar entregas com atraso.
    *   **Modelagem:** Escrever o caso de teste informando as datas, o ID do projetor e a mensagem de multa esperada.
    *   **Implementação:** Deixar as contas de testes criadas e os equipamentos cadastrados no banco de dados para poder usar.
    *   **Execução:** Entrar no sistema, simular a reserva do projetor e anotar se o programa respondeu certo ou deu erro.
    *   **Conclusão:** Somar quantos bugs foram achados, fechar os relatórios e salvar o resumo da versão para a equipe.
*   **Exemplo:** Seguir esses 7 passos durante a validação do novo módulo de reservas do sistema de equipamentos audiovisuais.
*   **Não confundir com:** Estratégia de teste, que são as diretrizes gerais de alto nível adotadas pela empresa para todos os projetos de forma fixa.

## Stakeholders
*   **O que é:** É qualquer pessoa ou grupo que tem algum interesse no projeto, podendo influenciar ou sofrer impactos com o resultado do software.
*   **Exemplo:** O investidor que financia o projeto, o gerente de operações, a recepção que gerencia os pedidos e os técnicos de som.
*   **Não confundir com:** A ideia de que usuário final não faz parte desse grupo. O usuário final é um tipo de stakeholder, mas nem todo stakeholder usa o sistema na prática (como quem financia o projeto).

## Rastreabilidade
*   **O que é:** É conseguir montar uma ponte documental que liga uma ponta à outra do projeto, mostrando qual requisito gerou qual teste e qual bug.
*   **Exemplo:** Criar uma amarração onde o Requisito `RF-02` (Reserva de Caixa de Som) liga ao Caso de Teste `CT-05`, que por sua vez liga ao Bug `#21`.
*   **Não confundir com:** Cobertura de teste, que calcula a porcentagem geral de itens validados, enquanto a rastreabilidade cria os caminhos individuais entre eles.

## Cobertura
*   **O que é:** É a medida em formato de porcentagem que aponta o quanto da nossa base de testes ou do código foi validado pelas baterias de testes.
*   **Exemplo:** Se a especificação do sistema de audiovisual possui 10 requisitos de reserva e nossos testes passaram por 8 deles, temos 80% de cobertura de requisitos.
*   **Não confundir com:** Rastreabilidade, que serve para desenhar o vínculo entre as pontas, e nem com Monitoramento, que serve para controlar o andamento das tarefas contra o cronograma.

## Independência de teste
*   **O que é:** É a sepação e a distância de quem faz o código e de quem testa, evitando que o criador avalie seu próprio trabalho.
*   **Exemplo:** A empresa colocar um analista de QA focado para testar a tela de reservas que foi programada pelo desenvolvedor do backend.
*   **Não confundir com:** O próprio autor testando suas linhas de código. Quem cria o recurso tem pontos cegos e facilidade para ignorar as próprias falhas de raciocínio.

## Causa-raiz
*   **O que é:** É o motivo inicial mais profundo que provocou o surgimento do erro humano lá no começo do processo.
*   **Exemplo:** O documento de requisitos veio com uma frase confusa sobre o limite de horário, fazendo o programador entender a regra errado. A causa-raiz é a ambiguidade do texto inicial.
*   **Não confundir com:** O defeito. O defeito é o ponto exato da linha de código onde o problema está escrito; a causa-raiz explica o motivo daquele problema ter nascido.

## Caso de teste
*   **O que é:** É a receita estruturada contendo o cenário anterior, as informações usadas, a sequência de cliques e o que deve acontecer no final.
*   **Exemplo:**
    *   **Pré-condição:** Carrinho de reservas contendo 1 câmera DSLR cadastrada.
    *   **Dados de entrada:** Clique no botão "Remover item".
    *   **Passos:** 1. Abrir a listagem de reservas atuais. 2. Clicar na lixeira ao lado da câmera.
    *   **Resultado esperado:** A câmera deve sumir da lista de pedidos e o contador de itens deve atualizar para zero.
*   **Não confundir com:** Cenário de teste, que traz apenas uma ideia resumida e macro do objetivo (ex: "Testar remoção de itens"), sem detalhar dados ou caminhos.

## Oráculo de teste
*   **O que é:** É a base ou o guia confiável que o testador consulta para ter certeza absoluta de qual é o comportamento correto do software.
*   **Exemplo:** Olhar o documento de regras do negócio, conferir um desenho de tela feito no Figma, fazer uma conta matemática na mão ou perguntar direto para o especialista do produto.
*   **Não confundir com:** Resultado esperado. O resultado esperado é a frase descritiva que você digita dentro do caso de teste; o oráculo é o documento de origem de onde você buscou aquela informação.

## Verificação
*   **O que é:** É checar se os artefatos e o software estão seguindo direitinho as regras e especificações técnicas que foram escritas no papel.
*   **Exemplo:** Olhar a tela de devolução criada e conferir se ela respeita o tamanho de caracteres e as validações de segurança pedidas no documento de arquitetura.
*   **Não confundir com:** Validação, que confere se o produto funciona bem e resolve a necessidade real do cliente na prática do dia a dia.

## Validação
*   **O que é:** É o processo de conferir se o software pronto atende o que o cliente precisa e funciona bem na rotina real de quem vai usar.
*   **Exemplo:** Entregar o módulo de agendamento na mão do técnico de áudio para ele simular os pedidos dele e ver se o fluxo é rápido e resolve a rotina de trabalho dele na empresa.
*   **Não confundir com:** Verificação, que apenas bate o sistema contra o documento técnico para ver se as regras de escrita e estrutura foram seguidas no papel.
