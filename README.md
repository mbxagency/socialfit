# 🏋️ Social FIT Data Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

> **Plataforma de Inteligência de Dados** que integra dados de ERP de academia com analytics de redes sociais para gerar insights de negócio acionáveis.

## 🎯 Visão Geral

O **Social FIT** é uma plataforma completa de ETL e Business Intelligence que:

- 📊 **Processa dados** de estudantes e planos de academia
- 📱 **Analisa métricas** do Instagram e redes sociais  
- 🔗 **Correlaciona** engajamento social com matrículas
- 📈 **Gera insights** acionáveis para o negócio
- 🌐 **Dashboard interativo** acessível publicamente

## 🚀 Quick Start

### 1. Setup do Projeto
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/social_fit.git
cd social_fit

# Instale dependências
pip install -r requirements.txt

# Configure credenciais
cp env_example.txt .env
# Edite .env com suas credenciais do Supabase
```

### 2. Execute o Pipeline ETL
```bash
# Execute o pipeline completo
python main.py

# Ou execute componentes individuais
python -m src.etl.etl_pipeline
```

### 3. Acesse o Dashboard
```bash
# Configure o dashboard
python dashboard/setup_dashboard.py

# Abra o dashboard
open dashboard/dashboard.html
```

## 📁 Estrutura do Projeto

```
social_fit/
├── 📊 dashboard/                 # Dashboard HTML interativo
│   ├── dashboard.html           # Dashboard principal
│   ├── setup_dashboard.py       # Script de configuração
│   └── README_DASHBOARD.md      # Documentação do dashboard
├── 🗄️ metabase/                  # Metabase (alternativa)
│   ├── metabase.jar            # Executável do Metabase
│   ├── docker-compose.yml      # Configuração Docker
│   ├── setup_metabase.sh       # Script de setup
│   └── README_METABASE.md      # Documentação Metabase
├── 🔧 src/                      # Código fonte principal
│   ├── etl/                    # Pipeline ETL
│   ├── analytics/              # Engine de analytics
│   ├── database/               # Gerenciamento de banco
│   ├── models/                 # Modelos de dados
│   └── config/                 # Configurações
├── 🧪 tests/                   # Testes automatizados
├── 📚 docs/                    # Documentação técnica
├── 🛠️ scripts/                 # Scripts utilitários
└── 📋 data/                    # Dados de exemplo
```

## 🌐 Dashboard Público

### **Acesso Principal**
- **URL**: `https://seu-usuario.github.io/social_fit/dashboard/dashboard.html`
- **Tipo**: HTML interativo com Chart.js
- **Acesso**: Público, sem login necessário
- **Atualização**: Tempo real via Supabase

### **Funcionalidades**
- 📊 **KPIs em tempo real** (alunos, receita, engajamento)
- 📈 **Gráficos interativos** (pizza, barras, linha, scatter)
- 📋 **Tabelas dinâmicas** (top alunos, posts)
- 🎯 **Insights acionáveis** (gerados pelo pipeline)
- 📱 **Responsivo** (desktop, tablet, mobile)

## 🔧 Tecnologias

### **Backend**
- **Python 3.9+** - Linguagem principal
- **Pydantic** - Validação de dados
- **Pandas** - Processamento de dados
- **Supabase** - Banco de dados PostgreSQL
- **Loguru** - Logging estruturado

### **Frontend**
- **HTML5** - Estrutura do dashboard
- **Bootstrap 5** - Framework CSS
- **Chart.js** - Gráficos interativos
- **Supabase JS** - Cliente JavaScript

### **DevOps**
- **GitHub Actions** - CI/CD
- **GitHub Pages** - Hospedagem do dashboard
- **Docker** - Containerização (Metabase)

## 📊 Dados Processados

### **Estudantes**
- Informações pessoais e demográficas
- Planos e valores de mensalidade
- Status de atividade e Gympass
- Distribuição por bairros

### **Instagram**
- Métricas de engajamento (likes, comments, saves)
- Alcance e visitas ao perfil
- Performance de hashtags
- Novos seguidores

### **Analytics**
- Correlação entre redes sociais e matrículas
- Insights acionáveis para o negócio
- Métricas de performance
- Tendências temporais

## 🚀 Deploy

### **Dashboard HTML (Recomendado)**
```bash
# 1. Configure credenciais
python dashboard/setup_dashboard.py

# 2. Commit e push
git add dashboard/dashboard.html
git commit -m "Update dashboard"
git push origin main

# 3. Configure GitHub Pages
# Settings > Pages > Deploy from branch > main
```

### **Metabase (Alternativa)**
```bash
# Execute setup do Metabase
cd metabase
./setup_metabase_jar.sh

# Acesse: http://localhost:3000
```

## 🧪 Testes

```bash
# Execute todos os testes
make test

# Testes unitários
pytest tests/unit/

# Testes de integração
pytest tests/integration/

# Testes específicos
pytest tests/ -k "test_etl"
```

## 📚 Documentação

- **[API Documentation](docs/API.md)** - Endpoints e integrações
- **[Development Guide](docs/DEVELOPMENT.md)** - Guia de desenvolvimento
- **[Dashboard Guide](dashboard/README_DASHBOARD.md)** - Configuração do dashboard
- **[Metabase Guide](metabase/README_METABASE.md)** - Setup do Metabase

## 🔐 Segurança

- **Credenciais** gerenciadas via variáveis de ambiente
- **Row Level Security** configurado no Supabase
- **Chave anônima** usada no dashboard público
- **HTTPS** obrigatório em produção

## 🤝 Contribuição

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/seu-usuario/social_fit/issues)
- **Documentação**: [docs/](docs/)
- **Dashboard**: [dashboard/](dashboard/)

---

**🎉 Social FIT - Transformando dados em insights acionáveis para academias!**