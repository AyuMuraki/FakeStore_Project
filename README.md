# 🚀 Projeto Integrado: Extração, Armazenamento e Relatório de Produtos

**Automatize, Armazene, Analise!**  
Um projeto completo que extrai dados de uma API, armazena em banco de dados e gera relatórios inteligentes em Excel. Tudo testado e garantido! ✨

## 🌟 Funcionalidades

### 1. **Extração de Dados com FastAPI & MySQL**
   - 📥 **Importação em Tempo Real:** Consome a API FakeStore e adiciona timestamps dinâmicos.
   - 🗃️ **Armazenamento Inteligente:** Estrutura otimizada no MySQL com endpoints REST:
     - `POST /produtos` → Insere dados com um comando.
     - `GET /produtos` → Recupera dados filtrados por Stored Procedures.
   - ⚡ **Performance:** Consultas rápidas com SP para filtrar por categoria.

### 2. **Relatório Excel Profissional**
   - 📊 **Dashboard Visual:** Gera arquivos Excel com:
     - 🎨 **Cores Dinâmicas:** Preços > $100 destacados em vermelho.
     - 📈 **Estatísticas Avançadas:** Média de preços por categoria em aba separada.
   - ✅ **Teste Automatizado:** Validação do Excel via Playwright + WeTransfer.

### 3. **Testes Robustos com Pytest**
   - ✔️ **100% Coverage:** Testes para API, extração de dados e estrutura do Excel.
   - 🤖 **Automatização Confiável:** Garante que tudo funcione após cada deploy.

---

## 🛠️ Tecnologias Utilizadas

| **Backend**       | **Data**         | **Testes**       |
|-------------------|-----------------|------------------|
| Python 3.10+      | MySQL 8.0        | Pytest           |
| FastAPI           | Pandas           | Playwright       |
| Requests          | OpenPyXL         | WeTransfer API   |
| SQLAlchemy (ORM)  | Coloração Condicional |  |

---

## ⚡ Como Executar?

### 📌 Requisitos
- Python 3.10+
- MySQL Server instalado
- Instalar dependências:
```bash
pip install -r requirements.txt
```

### 🔧 Passo 1: Configurar Banco de Dados
```bash
# Criar banco de dados
mysql -u root -p -e "CREATE DATABASE produtos_db;"

# Configurar variáveis de ambiente no .env
echo "DB_HOST=localhost" >> .env
echo "DB_USER=seu_user" >> .env
echo "DB_PASSWORD=sua_senha" >> .env
echo "DB_NAME=produtos_db" >> .env
```

### 🚀 Passo 2: Executar o Servidor
```bash
uvicorn main:app --reload
```

### 📊 Passo 3: Gerar Relatório Excel
```bash
python gerar_relatorio.py
```

---

## 🛡️ Testes Automatizados
Para rodar os testes, utilize:
```bash
pytest
```

---

## 📌 Próximos Passos
- 🔹 Melhorar interface do dashboard Excel.
- 🔹 Implementar autenticação JWT na API.
- 🔹 Adicionar suporte a mais fontes de dados.

🚀 **Contribuições são bem-vindas!**

