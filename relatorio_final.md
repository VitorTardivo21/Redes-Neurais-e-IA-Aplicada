# Relatório Técnico do Projeto ChatAvare

## Introdução

O projeto denominado ChatAvare consiste em um sistema computacional desenvolvido para realizar o processamento e a classificação automática de informações extraídas dos Diários Oficiais do município de Avaré. A estrutura identificada no projeto evidencia a aplicação de técnicas de Processamento de Linguagem Natural (PLN) e Aprendizado de Máquina, permitindo a automatização da análise de documentos públicos e a categorização de conteúdos de acordo com suas características textuais.

A organização do sistema demonstra a adoção de uma metodologia estruturada de desenvolvimento, contemplando desde a coleta dos dados até a disponibilização de um modelo treinado para utilização em ambiente de produção.

## Estrutura Geral do Sistema

A análise dos arquivos presentes no projeto permitiu identificar uma arquitetura baseada em etapas sequenciais de processamento. O ponto central da aplicação é representado pelo arquivo *app.py*, que aparentemente atua como interface principal do sistema, sendo responsável pela interação com o usuário e pela execução das funcionalidades relacionadas à classificação dos textos.

O fluxo de processamento inicia-se com a obtenção dos documentos por meio do módulo *etapa1_coleta.py*. Este componente tem como finalidade coletar os Diários Oficiais, armazenando-os localmente para posterior tratamento. Em seguida, os dados são submetidos a procedimentos de limpeza e normalização implementados no arquivo *etapa2_tratamento.py*, etapa essencial para garantir a qualidade das informações utilizadas pelo sistema.

Após o tratamento, os dados são preparados para utilização em modelos de aprendizado de máquina através do módulo *etapa3_preparacao.py*. Nesta fase, são realizadas operações típicas de pré-processamento textual, incluindo a construção de vocabulários, codificação de categorias e adequação dos dados ao formato exigido pelo algoritmo de treinamento.

O treinamento propriamente dito é executado pelo módulo *etapa4_treinamento.py*, responsável pela criação do modelo de inteligência artificial e pela avaliação de seu desempenho com base em métricas específicas.

## Organização dos Dados

O projeto utiliza diferentes conjuntos de dados distribuídos em arquivos CSV e em um banco de dados SQLite. Os arquivos *diarios_avare.csv* e *diarios_tratados.csv* representam, respectivamente, os dados em seu estado bruto e após a aplicação dos processos de limpeza e normalização.

No diretório destinado aos dados processados encontram-se arquivos fundamentais para o funcionamento do sistema. Entre eles destacam-se a base textual consolidada, uma amostra previamente rotulada para treinamento supervisionado, o banco de dados SQLite contendo os registros estruturados, além dos arquivos de mapeamento de classes e vocabulário utilizados durante as etapas de treinamento e inferência.

A existência desses componentes demonstra a preocupação com a organização dos dados e a reprodutibilidade dos experimentos realizados durante o desenvolvimento do projeto.

## Modelo de Inteligência Artificial

A presença do arquivo *modelo.pt* indica a utilização do framework PyTorch para o desenvolvimento e armazenamento do modelo treinado. Esse formato é amplamente empregado em aplicações de aprendizado profundo devido à sua eficiência e flexibilidade na construção de arquiteturas neurais.

A estrutura do projeto sugere que o modelo foi desenvolvido para executar tarefas de classificação textual, recebendo como entrada trechos extraídos dos Diários Oficiais e retornando uma categoria previamente definida durante o treinamento. Entre as possíveis categorias encontram-se licitações, contratos, portarias, decretos e outros tipos de documentos administrativos.

O processo de inferência é realizado por meio do módulo *inferencia.py*, responsável por aplicar os mesmos procedimentos de pré-processamento utilizados durante o treinamento antes de encaminhar os dados ao modelo para classificação.

## Componentes de Processamento de Texto

Os módulos localizados no diretório *src* concentram as funcionalidades relacionadas ao tratamento dos dados. O arquivo *extract_text.py* é responsável pela extração do conteúdo textual dos documentos PDF, enquanto o módulo *preprocess.py* realiza as operações de limpeza e preparação dos textos.

O gerenciamento dos dados utilizados no treinamento é realizado pelo arquivo *dataset.py*, que organiza as informações de forma compatível com o framework de aprendizado de máquina empregado. Já o arquivo *model.py* contém a definição da arquitetura da rede neural utilizada pelo sistema.

Essa divisão modular favorece a manutenção, a escalabilidade e a reutilização do código, características desejáveis em projetos de software que envolvem técnicas de inteligência artificial.

## Avaliação e Documentação

A presença de relatórios técnicos e gráficos de análise demonstra a realização de um processo formal de avaliação do modelo desenvolvido. Entre os artefatos identificados encontram-se gráficos de curva de treinamento, matriz de confusão, distribuição de classes e distribuição do comprimento dos textos.

Essas ferramentas permitem analisar aspectos importantes do desempenho do modelo, como sua capacidade de generalização, a ocorrência de erros de classificação e o equilíbrio entre as diferentes categorias presentes na base de dados.

Além disso, a existência de documentação referente às etapas de preparação e treinamento evidencia a preocupação com o registro metodológico do desenvolvimento, aspecto fundamental para projetos acadêmicos e científicos.

## Considerações Finais

Com base na estrutura identificada, conclui-se que o ChatAvare constitui uma aplicação de inteligência artificial voltada à classificação automática de documentos administrativos extraídos dos Diários Oficiais do município de Avaré. O sistema apresenta uma arquitetura completa de ciência de dados, contemplando as etapas de coleta, tratamento, preparação, treinamento, avaliação e utilização de modelos de aprendizado de máquina.

A organização dos arquivos e a separação das responsabilidades entre os módulos demonstram a adoção de boas práticas de desenvolvimento de software, contribuindo para a manutenção e evolução futura da aplicação. Dessa forma, o projeto representa uma solução tecnológica relevante para automatizar a análise de grandes volumes de documentos públicos, reduzindo o esforço manual necessário para sua categorização e consulta.

