# 🚀 Deploy do Dashboard Social FIT

## 🌐 GitHub Pages

O dashboard está configurado para deploy automático no GitHub Pages.

### **URL do Dashboard**
```
https://murilobiss-dataeng.github.io/social_fit/dashboard/
```

### **Configuração Automática**

1. **GitHub Actions** - Deploy automático configurado
2. **Branch** - `main`
3. **Pasta** - `dashboard/`
4. **Arquivo principal** - `dashboard.html`

### **Como Funciona**

1. **Push para main** → Deploy automático
2. **GitHub Actions** → Build e deploy
3. **GitHub Pages** → Hospedagem gratuita
4. **HTTPS** → Segurança automática

## 🔧 Configuração Manual

### **1. Ativar GitHub Pages**

1. Vá para **Settings** do repositório
2. Role até **Pages**
3. Em **Source**, selecione **Deploy from a branch**
4. Escolha **main** como branch
5. Escolha **/ (root)** como pasta
6. Clique **Save**

### **2. Configurar Actions (Opcional)**

O workflow `.github/workflows/deploy.yml` já está configurado para:
- Deploy automático quando `dashboard/` é alterado
- Build otimizado
- Cache de dependências

## 📱 Acesso

### **URLs Disponíveis**
- **Principal**: `https://murilobiss-dataeng.github.io/social_fit/dashboard/`
- **Dashboard**: `https://murilobiss-dataeng.github.io/social_fit/dashboard/dashboard.html`
- **Index**: `https://murilobiss-dataeng.github.io/social_fit/dashboard/index.html`

### **Redirecionamento**
- `index.html` → redireciona automaticamente para `dashboard.html`
- Acesso direto ao `dashboard.html` também funciona

## 🔐 Segurança

### **Credenciais**
- **Supabase URL**: Configurada no HTML
- **Supabase Key**: Chave anônima (segura para público)
- **HTTPS**: Forçado pelo GitHub Pages

### **Row Level Security**
- Configurado no Supabase
- Apenas dados públicos acessíveis
- Sem dados sensíveis expostos

## 📊 Funcionalidades

### **Dashboard Público**
- ✅ **Acesso gratuito** - Sem login necessário
- ✅ **Tempo real** - Dados do Supabase
- ✅ **Responsivo** - Mobile, tablet, desktop
- ✅ **Interativo** - Gráficos e tabelas dinâmicas
- ✅ **Profissional** - Design moderno

### **KPIs em Tempo Real**
- Total de alunos
- Planos ativos
- Receita mensal
- Engajamento médio

### **Gráficos Interativos**
- Distribuição por plano
- Distribuição por gênero
- Top 10 bairros
- Evolução do engajamento
- Top hashtags

## 🛠️ Manutenção

### **Atualizações**
```bash
# 1. Faça alterações no dashboard
git add dashboard/dashboard.html

# 2. Commit e push
git commit -m "Update dashboard"
git push origin main

# 3. Deploy automático em ~2 minutos
```

### **Monitoramento**
- **GitHub Actions** - Status do deploy
- **GitHub Pages** - Status da hospedagem
- **Supabase** - Status da conexão

## 🚨 Troubleshooting

### **Dashboard não carrega**
1. Verifique se o GitHub Pages está ativo
2. Aguarde 2-5 minutos após push
3. Verifique as credenciais do Supabase
4. Teste localmente primeiro

### **Dados não aparecem**
1. Verifique conexão com Supabase
2. Confirme se há dados nas tabelas
3. Verifique Row Level Security
4. Teste no console do navegador

### **Erro 404**
1. Verifique se o arquivo existe em `dashboard/`
2. Confirme o nome do arquivo
3. Aguarde o deploy completar
4. Force refresh (Ctrl+F5)

## 📈 Próximos Passos

1. ✅ **Deploy configurado**
2. 🔄 **Monitoramento** - Métricas de acesso
3. 🔄 **Melhorias** - Novas funcionalidades
4. 🔄 **SEO** - Otimização para busca
5. 🔄 **Analytics** - Google Analytics

---

**🎉 Dashboard público e acessível em: https://murilobiss-dataeng.github.io/social_fit/dashboard/** 