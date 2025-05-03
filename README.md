Bem-vindo ao Furia KYF! Este app foi desenvolvido para o desafio FURIA, utilizando Python Flask, LangChain, OpenRouter e Selenium. Ele permite cadastro inteligente de usuários, validação de identidade com IA, login seguro e análise de links relevantes ao perfil do usuário. 🚀
✨ Funcionalidades

    Cadastro de Usuário (/signup)

        Coleta dados pessoais (nome, endereço, CPF, interesses, atividades, eventos e compras do último ano)

        Recebe foto do documento e selfie do usuário 📸

        Valida a identidade usando IA comparando as fotos 🤖

        Armazena preferências e resumo do usuário

    Login Seguro (/signin)

        Autenticação via email e senha criptografada 🔒

    Verificação de Token (/verifytoken)

        Confirma se o token do usuário é válido para acesso seguro 🛡️

    Análise de Links Relacionados (/related-links)

        Recebe links

        Utiliza IA para verificar se o conteúdo é relevante ao perfil/interesses do usuário

        Usa Selenium para automatizar a coleta de informações dos links 🌐

🛠️ Tecnologias Utilizadas

    Python Flask

    LangChain + OpenRouter (IA para análise de conteúdo e validação de identidade)

    Selenium (automação de scraping)

    MongoDB

🚦 Como Usar

    Clone o repositório e instale as dependências:

    bash
    git clone https://github.com/cassmatheuss/kyf-furia-backend.git
    cd furia-kyf-backend
    poetry install
    poetry run python main.py

ENV

    MONGO_DB_URL=
    DB_NAME=
    OPENROUTER_API_KEY=
    OPENROUTER_BASE_URL=
    JWT_SECRET_KEY=

Execute a aplicação:

    bash
    poetry run python main.py

    Use as rotas para cadastrar, logar, validar token e analisar links.

📲 Rotas
  /signup	Cadastro de usuário com dados, preferências e validação de identidade
  /signin	Login com email e senha
  /verifytoken	Verifica se o token do usuário é válido
  /related-links	Analisa se um link é relevante ao perfil usando IA e Selenium
💡 Observações

    Todos os dados são tratados com segurança e criptografia.

    A IA é utilizada tanto para validação de identidade quanto para análise de relevância dos links.
