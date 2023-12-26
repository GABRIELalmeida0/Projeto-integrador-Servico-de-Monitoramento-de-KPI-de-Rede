<p>
<h4>
Título da proposta
</h4>
Serviço de Monitoramento de KPI de Rede: Um Caminho para a Qualidade de Experiência em Plataformas de streaming.
</p>

<p>
<h4>
Resumo da proposta
</h4>
&emsp;&emsp;Nos últimos anos as plataformas de conteúdo de streaming vêm se popularizando mundialmente. Uma das causas principais dessa popularização veio através da pandemia mundial sofrida anos atrás, que sofre repercussões até os dias de hoje, o que levou as pessoas a serem obrigadas a ficarem em suas casas e, em  muitos casos até mesmo que trabalhar home office, assistir aulas online, e outras responsabilidades a cumprir. Essa expansão trouxe uma preocupação com a qualidade da entrega do streaming, já que, cada vez mais a necessidade da valoração da qualidade aumentava. Dessa forma, as plataformas responsáveis por entregar o streaming passaram por uma explosão no quantitativo de usuários, e começaram a dar um maior nível de atenção ao monitoramento da rede que entrega o streaming. Essa é uma forma de se obter uma visão de como o vídeo transmitido está chegando para o cliente, a necessidade desse tipo de monitoramento é essencial para poder se obter uma perspectiva melhor da condição do streaming que o cliente está recebendo. Por isso, a nossa proposta é entregar um serviço que seja capaz de fazer o monitoramento de métricas de rede com base nas KPI’s, que são essenciais para se indicar aproximadamente a experiência do QoE do usuário, deste modo, poderemos entregar as plataformas de streaming uma análise melhor de como os vídeos são entregues, pela perspectiva do usuário, de acordo com os parâmetros das KPI’s.
</p>

<p>
<h4>
Introdução:
</h4>
&emsp;&emsp;À medida que os aparelhos eletrônicos vêm ganhando cada vez mais espaço no mercado, o tráfego de multimídia segue aumentando exponencialmente [1]. Dessa forma, até mesmo grandes plataformas como YouTube, Twitch, Netflix, e provedores , exigem cada vez mais atenção à qualidade do streaming oferecido aos seus usuários. Com isso surgiram as métricas subjetivas denominadas de QoE (Qualidade de Experiência), que se concentram em como os usuários percebem a qualidade de um produto ou serviço, já que a satisfação do usuário desempenha um papel significativo na reputação da empresa e na fidelização do cliente. No entanto, quando se usam métricas não objetivas para avaliar o QoE, causa - se um impacto direto na avaliação do vídeo recebido pelo usuário através da rede dessas plataformas. Uma vez que esse tipo de métrica depende de fatores externos, tais como o nível de conhecimento técnico, experiências anteriores, variações culturais e linguísticas ou fatores emocionais do telespectador [2]. Assim, propomos um serviço capaz de monitorar a os Indicadores Chave de Desempenho (KPI) de rede e com base nas Métricas Objetivas fornecer uma perspectiva sobre o QoE do usuário.
</p>
<h4>
Justificativa:
</h4>
<p>
&emsp;&emsp;O nosso projeto propõe um serviço que entrega o monitoramento de KPI da rede das plataformas streaming. Sua principal vantagem reside na possibilidade de se obter Métricas Objetivas monitorando parâmetros como Delay, Variação do Atraso (Jitter), Perda de Pacotes (Packet Loss), que podem indicar, através de cálculos de performance, de uma forma rápida e precisa o estado da rede num determinado momento. Dessa forma, através do uso de um ferramental Open Source, é possível ter indicadores do estado da QoE do cliente com os dados do monitoramento as empresas de streaming terão previsões do estado da rede a todo momento, e com isso poderão mensurar a qualidade da experiência do cliente de forma objetiva e mais próxima da realidade. Estudos na área demonstram que as métricas objetivas são capazes de mensurar as medidas subjetivas de forma cada vez mais próxima do real [3]. Os métodos de avaliação objetivos são totalmente isentos da presença humana para avaliação, são baseados em cálculos matemáticos que são capazes de automatizar, além de medir o grau de degradação que o vídeo sofreu durante a transmissão. O uso dessas métricas resulta na economia de tempo e dinheiro já que possuem o menor custo de implementação, além de ser capaz de mostrar degradações ainda mais imperceptíveis, tornando - se de grande relevância. Chegando à conclusão de que uso de métricas objetivas conseguidas através do monitoramento da KPI da rede é de grande valia para plataformas de streaming que se preocupam cada vez mais com a percepção de seus clientes. Além disso, o nosso serviço foi pensado visando futuras melhorias relacionadas à Aprendizado de Máquina (ML) para as decisões de QoS e QoE.
Ao analisar o Plano de Conteúdo do Cronograma (PPC) do curso de Redes de Computadores, foram identificadas as seguintes disciplinas relevantes:
</p>
<p>
Administração de Sistemas Abertos (ASA) - Pág. 75:<br>
(Configuração do ambiente de prova de conceito e dos serviços de monitoramento)<br>
1.   Configuração do ambiente de Rede<br>
2. Administração de serviços de rede<br>
&emsp;2.4. Servidor Web (HTTPS)<br>
</p>
<p>
Programação para Redes - Pág. 66:<br>
(Exportação de dados de APIs, configuração de Banco de dados e automação de processos via Script )<br>
2. Acesso ao Banco de Dados<br>
&emsp;2.3. Conexão com o banco <br>
&emsp;2.4. Consulta ao Banco de Dados<br>
4. Geração de Scripts para automatização de tarefas.<br>
</p>
<p>
Introdução aos Sistemas Abertos - Pág. 67:<br>
(Conhecimentos básicos em linux, agendamento de tarefas com crontab e criação de topologia simples e parâmetros da rede)<br>
&emsp;1. Noções básicas do uso de Shell<br>
&emsp;12. Configurações básicas de rede<br>
&emsp;15. Agendamento de tarefas<br>
</p>
<p>
<h4>
Objetivo Geral:<br>
</h4>
&emsp;&emsp;Com esse projeto visamos desenvolver e lançar com sucesso um serviço voltado para empresas que buscam identificar como o seu conteúdo está sendo entregue. Tal serviço provê um monitoramento com o uso de KPIs de rede, e a visão do QoE na perspectiva do usuário. Dessa maneira nosso serviço contribuirá para ser possível que o provedor consiga ter uma visão de como está a qualidade do vídeo recebido com determinados parâmetros da rede e identificando se precisa tomar medidas para a melhorar essa qualidade.<br>
&emsp;&emsp;Este projeto tem como objetivo desenvolver um serviço de monitoramento de KPIs de rede direcionado para plataformas de streaming que além de monitorar oferece a perspectiva do nível de QoE do usuário fazendo-se o uso de métricas objetivas da rede. Dessa maneira nosso serviço contribuirá para que as plataformas tenham uma visão geral da rede pelas KPIs e o QoE do vídeo na perspectiva do usuário para identificar se atende a demanda ou é necessário melhorias. 
</p>

<p>
Objetivo específicos :<br>
1 - Criação do ambiente para obtenção de dados controlados.<br>
&emsp;1.1  Criação do ambiente para extração dos dados.<br>
&emsp;1.2 Implementação do Prometheus para as KPIs e Grafana para criação de Dashboards<br>
&emsp;1.3 Configuração funcional do Prometheus e Grafana e coleta das métricas<br>
2 - Análise dos dados e preparação do ambiente para retirada do QoE<br>
&emsp;2.1 Análise do amostral do dados para preparação do ambiente<br>
&emsp;2.2 Criação do ambiente e o tratamento do vídeo para realizar a prova de conceitos<br>
3 - Retirada das métricas de QoE e visualizar como está a percepção do usuário<br>
&emsp;3.1 captura de métricas de QoE e provisionamento de SSIM mapeado para MOS<br>
</p>

<p>
<h4>
Sprints:<br>
</h4>

SPRINT 1 - (Criação do ambiente para extração dos dados.)<br>
Julio: Criar uma API Flask para a coleta de métricas<br>
Gabriel: Script com comandos para manipular os parâmetros da rede<br>
 Ruth: Agendamento do crontab para automatizar a alteração do estado da rede<br>

SPRINT 2 - (Implementação do Prometheus para as KPIs e Grafana para criação de Dashboards)<br>
Julio: Criação do Container do Prometheus<br>
Gabriel: Criação do Container do Grafana<br> 
Ruth: Integração do Grafana com o Prometheus<br>

SPRINT 3 - (Configuração funcional do Prometheus, Grafana, e coleta das métricas) <br>
Julio: Configurar Prometheus para realizar o Scraping da API Flask<br> 
Gabriel: Configuração dos Dashboard com os dados obtidos<br>
Ruth: Acompanhamento da coleta das métricas e manipulação da rede<br>

SPRINT 4 - (Análise do amostral do dados para preparação do ambiente)<br>
Julio: Criação dos Dockerfiles para empacotamento das aplicações do ambiente <br>
Gabriel: Separação de amostras para prover a análise de QoE<br>
Ruth: Análise exploratória dos dados das KPIs e tratamento dos dados<br>

SPRINT 5 - (Criação do ambiente e o tratamento do vídeo para realizar a prova de conceitos)<br>
Julio: Scripts para alteração de parâmetros da rede simulada<br>
Gabriel: Automatização do ambiente containerizado para simular o streaming<br>
Ruth: Escolha e tratamento do vídeo para transmissão<br>

SPRINT 6 - (Capturar as métricas de QoE e prover o SSIM mapeado para MOS)<br>
Julio: Captura das métricas do SSIM com base no vídeo recebido e o original<br>
Gabriel: Mapeamento do conjunto resultado do SSIM para a métrica comum MOS<br>
Ruth: Exibição da perspectiva do vídeo ao usuário

SPRINT 7 (RECUPERAÇÃO)<br> 
</p>
