# Abrigo de Animais

Este é um site para gerenciar um abrigo de animais, permitindo o cadastro de animais disponíveis para adoção, gerenciamento de informações e exibição de detalhes para potenciais adotantes.

## Funcionalidades

- Cadastro de animais disponíveis para adoção.
- Busca e exibição de detalhes dos animais.
- Gerenciamento de informações do abrigo.

## Requisitos

- Python 3.10+
- Django 4.2.6
- Pillow (para manipulação de imagens)

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd abrigo-de-animais
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

1. Configure as variáveis de ambiente no arquivo `.env` (se necessário).
2. Certifique-se de que o banco de dados SQLite está configurado corretamente.

## Execução

1. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

2. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

3. Acesse o site no navegador em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Estrutura do Projeto

- `adocoes/`: Aplicação para gerenciar adoções e animais.
- `base/`: Aplicação base com templates e arquivos estáticos.
- `media/`: Diretório para armazenar imagens carregadas.
- `projeto_abrigo/`: Configurações principais do projeto Django.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
