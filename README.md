# 🚀 Projeto Integrado: Extração, Armazenamento e Relatório de Produtos

**Automatize, Armazenes e Analise Dados de Produtos!**  
Este projeto é uma solução completa que envolve a extração de dados de uma API externa, o armazenamento estruturado desses dados em um banco de dados relacional MySQL e a geração de relatórios interativos em Excel. Além disso, a automação de testes garante que todas as etapas do processo funcionem corretamente após cada alteração ou deploy. 

---

## 🌟 Funcionalidades

### 1. **Extração de Dados com FastAPI & MySQL**
A primeira parte do projeto lida com a extração de dados de uma API externa chamada **FakeStore API**, que fornece informações sobre produtos, incluindo nome, descrição, preço e categoria.

- 📥 **Consumo da API FakeStore:** O script se comunica com a API FakeStore em tempo real para obter os dados. A cada consulta, é registrado um **timestamp** (data e hora) para garantir que os dados extraídos sejam identificados com o momento da consulta, o que ajuda a monitorar a atualização das informações.
  
- 🗃️ **Armazenamento Eficiente no Banco de Dados:**  
  - Os dados extraídos são armazenados em um banco de dados **MySQL**. Utilizamos a **ORM SQLAlchemy** para facilitar o gerenciamento dos dados no banco.
  - A tabela no MySQL é estruturada para armazenar as informações dos produtos de forma organizada e otimizada. Cada produto possui atributos como nome, preço, descrição e categoria, e cada linha da tabela representa um produto.

- **Endpoints da API FastAPI:**
  - `POST /produtos`: Este endpoint é utilizado para **inserir** os produtos extraídos da API FakeStore no banco de dados MySQL. 
    - Ao receber os dados no corpo da requisição, o sistema insere um novo produto na tabela, atribuindo o timestamp da consulta. 
  - `GET /produtos`: Este endpoint permite **recuperar** os produtos armazenados no banco de dados. Utilizamos **Stored Procedures** para filtrar os produtos de acordo com categorias específicas, otimizando a consulta e tornando-a mais eficiente.
    - A consulta pode ser feita com filtros como "Categoria de Produto", retornando apenas os produtos de uma categoria específica, se necessário.

- ⚡ **Consultas Rápidas e Performance:**  
  Utilizamos **Stored Procedures (SP)** no MySQL para garantir que as consultas, especialmente as filtragens por categoria, sejam rápidas e escaláveis, mesmo que o volume de dados cresça.

### 2. **Relatório Excel Profissional**
Após a extração e o armazenamento dos dados, geramos um relatório detalhado em Excel, que é formatado de acordo com as necessidades do projeto e proporciona insights valiosos sobre os produtos.

- 📊 **Geração de Relatório Excel com Pandas e OpenPyXL:**
  - Usamos a biblioteca **Pandas** para manipulação de dados e **OpenPyXL** para a criação e formatação do arquivo Excel.
  - Cada produto extraído da API e armazenado no banco de dados é incluído em uma aba principal do Excel.

- 🎨 **Coloração Condicional:**  
  Para melhorar a visualização e destacar produtos de alto valor, aplicamos coloração condicional:
  - Produtos com **preço acima de $100** são destacados em **vermelho** para facilitar a identificação.
  
- 📈 **Estatísticas Avançadas:**  
  - Além dos dados dos produtos, o relatório inclui uma aba extra com estatísticas sobre os produtos, como a **média de preços por categoria**. Isso ajuda a visualizar o comportamento de preços e analisar a distribuição dos valores.
  - A aba de estatísticas é gerada automaticamente a partir dos dados dos produtos, utilizando funções do **Pandas** para calcular a média de preços e outras métricas relevantes.

- ✅ **Validação do Relatório:**  
  O relatório gerado é validado automaticamente através do **Playwright**, uma ferramenta de automação de testes. Ele simula a interação com o arquivo Excel e valida se a formatação, como as cores e a estrutura das abas, está correta.
  - Após a validação, o arquivo Excel é enviado para **WeTransfer** para garantir que ele esteja acessível e pronto para ser compartilhado.

### 3. **Testes Automatizados com Pytest**
Testes automatizados são fundamentais para garantir que todas as etapas do processo funcionem corretamente, especialmente em um ambiente de desenvolvimento dinâmico, onde alterações podem ser feitas constantemente.

- ✔️ **Testes Abrangentes com Pytest:**
  - **Testes de API (POST e GET):** Utilizamos o **Pytest** para testar os endpoints da API FastAPI. Isso inclui:
    - Verificar se o `POST /produtos` insere os dados corretamente no banco de dados.
    - Verificar se o `GET /produtos` retorna os dados corretamente, com a capacidade de filtrar produtos por categoria.
  
  - **Testes de Extração de Dados:** Testamos a comunicação com a FakeStore API para garantir que os dados sejam extraídos corretamente e que o timestamp de consulta seja gerado corretamente.
  
  - **Testes de Formatação do Excel:** Validamos a estrutura e a formatação do arquivo Excel, incluindo:
    - Verificar se as colunas estão corretas.
    - Testar a coloração condicional.
    - Verificar se as estatísticas da aba extra estão corretas.

- 🤖 **Automação de Testes:**  
  O uso de Pytest e Playwright garante que o sistema seja testado automaticamente sempre que houver mudanças no código, proporcionando maior confiabilidade ao projeto.

---

## 🛠️ Tecnologias Utilizadas

| **Backend**       | **Banco de Dados** | **Testes**         |
|-------------------|--------------------|--------------------|
| Python 3.10+      | MySQL 8.0          | Pytest             |
| FastAPI           | SQLAlchemy (ORM)   | Playwright         |
| Requests          | Pandas             | WeTransfer API     |
|                   | OpenPyXL           |                    |

- **FastAPI:** Framework rápido e moderno para a criação de APIs RESTful.
- **MySQL:** Banco de dados relacional utilizado para armazenar os dados de produtos.
- **SQLAlchemy:** ORM para interação com o banco de dados MySQL de maneira eficiente.
- **Pandas:** Biblioteca poderosa para manipulação de dados em Python, usada para gerar o relatório em Excel.
- **OpenPyXL:** Biblioteca para criar e manipular arquivos Excel, usada para gerar o relatório visual.
- **Playwright:** Ferramenta para automação de testes de front-end, usada para validar a formatação do Excel.
- **Pytest:** Framework de testes para Python, utilizado para garantir a qualidade da API e da extração de dados.

---

## ⚡ Como Executar?

### 📌 Requisitos
Antes de começar, certifique-se de que você tem os seguintes pré-requisitos instalados:

- **Python 3.10+**
- **MySQL Server** (versão 8.0 ou superior)
  
### 🔧 Passo 1: Configuração do Banco de Dados
Primeiro, crie o banco de dados e configure as variáveis de ambiente necessárias:

```bash
# Criar banco de dados
mysql -u root -p -e "CREATE DATABASE produtos_db;"

# Configurar variáveis de ambiente no .env
echo "DB_HOST=localhost" >> .env
echo "DB_USER=seu_user" >> .env
echo "DB_PASSWORD=sua_senha" >> .env
echo "DB_NAME=produtos_db" >> .env
```

### 🚀 Passo 2: Executar o Servidor FastAPI
Inicie o servidor FastAPI para começar a consumir a API FakeStore e permitir as interações com o banco de dados:

```bash
uvicorn main:app --reload
```


### 📊 Passo 3: Gerar Relatório Excel

Agora, execute o script para gerar o relatório Excel com os produtos extraídos e formatados:

```bash
python gerar_relatorio.py
```


### 🛡️ Testes Automatizados
Para garantir que tudo esteja funcionando corretamente, execute os testes automatizados:

```bash
pytest
```



### 🚀 Contribuições são bem-vindas!
Sinta-se à vontade para sugerir melhorias ou enviar pull requests. Vamos construir algo incrível juntos!




