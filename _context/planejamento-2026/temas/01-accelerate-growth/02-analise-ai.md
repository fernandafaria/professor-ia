# Análise: 🚀 Accelerate Growth

**Analisado em:** 2025-11-07  
**Analyst:** Head de AI  
**Status:** Em Progresso

---

## 📊 Resumo Executivo

O tema Accelerate Growth visa expandir o Zé além do core beer, capturando R$ 7Bi adicionais em categorias de conveniência através da digitalização de ocasiões cotidianas. Foco em aumentar YAB via duas frentes: (1) expansão de portfólio e presença em novas ocasiões e (2) engajamento profundo da base através de personalização e lifecycle management.

**Potencial Total Identificado:**
- TAM adicional: +R$ 7Bi
- MAB incremental: +796k usuários/ano
- GMV incremental: +R$ 107,9Mi (apenas Engagement 3.0)
- Aumento frequência: +20-25%

---

## 🎯 Prioridades Identificadas

### Top 3 Prioridades Estratégicas

1. **Expansão de Ocasiões**
   - Ganhar TOM em 5 ocasiões cotidianas (gap de -10pp a -31pp vs competidores)
   - Reposicionar marca de "app de cerveja" para "plataforma de diversão"
   - Ampliar portfólio: non-beer, snacks, conveniência

2. **Engajamento e Retenção**
   - Crescer MAB através de personalização e lifecycle
   - Reduzir churn (caiu 13% em 2025)
   - Aumentar FMRR/RMRR com vínculos estratégicos

3. **Omnicanalidade (Zé Everywhere)**
   - Expandir pontos de acesso: WhatsApp, Social, Search
   - Reduzir atrito entre intenção e compra
   - 83% compram no app, mas descoberta acontece fora

---

## 📈 Dimensionamento Total do Tema

### Potencial Identificado

| Fonte | Impacto |
|-------|---------|
| **Consumer Engagement 3.0** | +796k MAB/ano, +R$ 107,9 Mi GMV |
| **Commercial Calendar (Holidays/KSMs)** | +R$ 133 MM GMV/ano |
| **TAM Expansion (Non-beer)** | +R$ 7 Bi addressable |
| **Frequência (Ocasiões)** | +20-25% |

**Total Incremental Quantificado:** +R$ 240 Mi GMV/ano

---

## 🤖 Oportunidades de AI

### 🔥 ALTA PRIORIDADE - Quick Wins

#### 1. LLM para Recomendação Contextual por Ocasião
**Problema:** Usuários não sabem que Zé oferece portfólio completo (apenas 37% sabem de snacks)

**Solução AI:**
- Search semântico no app ("o que combina com churrasco?")
- Recomendações por ocasião ("para relaxar assistindo Netflix")
- Cross-sell inteligente beer + non-beer + snacks

**Impacto Esperado:**
- Aumento de basket size (AOV)
- Descoberta de produtos complementares
- Educação passiva sobre portfólio

**Complexidade:** Média  
**Time to Value:** 2-3 meses  
**Dependencies:** 
- Catálogo completo taggeado com ocasiões
- Integração com produto (home + busca)
- Dados de comportamento por ocasião

**Owner:** Produto + AI

---

#### 2. Modelo Preditivo de Reativação (Otimização de Churn)
**Problema:** Investimento em reativação não otimizado. Taxa de reativação atual pode crescer +11% com modelo direcionado.

**Solução AI:**
- Modelo de propensão a reativação (score 0-100)
- Segmentação automática por probabilidade
- Otimização de investimento (foco em high-propensity)
- Recomendação de melhor alavanca por usuário (cupom vs frete vs categoria)

**Impacto Esperado:**
- +11% taxa de reativação (já validado)
- ROI de campanha de reativação
- 131k MAB incrementais
- R$ 10,8Mi GMV incremental

**Complexidade:** Média-Alta  
**Time to Value:** 2-3 meses  
**Dependencies:**
- Histórico de churn/reativação
- Features: RFM, categorias, alavancas, sazonalidade
- Integração com Braze

**Owner:** Growth & Dados + AI

---

#### 3. Triggers Comportamentais Inteligentes
**Problema:** Oportunidades de conversão perdidas por falta de timing adequado. Calendário genérico não considera contexto individual.

**Solução AI:**
- Predição de próxima compra (when)
- Contexto enriquecido: clima + geolocalização + histórico
- Triggers adaptivos (não apenas tempo, mas comportamento)
  - Abandono de navegação inteligente
  - "Está perto do seu POC favorito" + ocasião
  - "Clima quente + sexta à tarde" → cerveja gelada

**Impacto Esperado:**
- Aumento de conversão em triggers
- Redução de fadiga de comunicação (right time)
- Uplift em ocasiões não planejadas

**Complexidade:** Alta  
**Time to Value:** 3-4 meses  
**Dependencies:**
- Dados de clima (API)
- Geofence ativo
- Integração CDP + Braze
- Modelo de predição next order

**Owner:** CRM + Growth & Dados + AI

---

### 🎯 INVESTIMENTO ESTRATÉGICO - Alto Impacto

#### 4. Sistema de Personas Dinâmicas + Personalização 1:1
**Problema:** 6 personas identificadas, mas personalização ainda limitada. Potencial de +47% FMRR com mais categorias e +72% FMRR com burn ZEC nos primeiros 30d.

**Solução AI:**
- Clustering dinâmico (não estático)
- Score de afinidade por:
  - Categoria
  - Ocasião
  - Horário/dia preferido
  - Sensibilidade a preço
  - Marca preferida
- Personalização em escala:
  - Home dinâmica por persona
  - CRM 1:1 (mensagem + oferta + timing)
  - Descontos direcionados

**Impacto Esperado:**
- +47% FMRR (mais categorias nos primeiros 30d)
- +72% FMRR (burn ZEC nos primeiros 30d)
- +120% RET30 (enriquecimento de base)
- Aumento de CTR e conversão

**Complexidade:** Alta  
**Time to Value:** 4-6 meses  
**Dependencies:**
- Dados enriquecidos (marca preferida, ocasião)
- Integração profunda Braze
- Espaços personalizáveis no app
- Backlog produto para home dinâmica

**Owner:** Growth & Dados + Produto + CRM + AI

---

#### 5. Orquestração Inteligente de Campanhas
**Problema:** Sobrecarga de comunicação. Necessidade de equilibrar frequência por cluster (15-17 pushes/semana) mantendo relevância.

**Solução AI:**
- Otimização de cadência por usuário (não apenas cluster)
- Prevenção de fadiga (score de saturação)
- Priorização de mensagens quando múltiplas campanhas competem
- Aprendizado contínuo: "qual canal/horário/mensagem converte esse usuário?"
- A/B testing automatizado

**Impacto Esperado:**
- Redução de opt-out
- Aumento de CTR/conversão
- Melhor ROI de campanhas
- Automação do "Orquestrador" mencionado

**Complexidade:** Alta  
**Time to Value:** 4-6 meses  
**Dependencies:**
- Histórico de interação por canal
- Integração Braze + CDP
- Ferramenta Digital Insights

**Owner:** CRM + Growth & Dados + AI

---

#### 6. Análise e Predição de Ocasiões
**Problema:** Calendário comercial fixo. Oportunidade de antecipar picos e identificar micro-ocasiões.

**Solução AI:**
- Predição de demanda por ocasião (feriados, eventos, finais de semana)
- Identificação de novas ocasiões emergentes (data mining)
- Forecast de GMV por ocasião → otimizar estoque/comercial
- Alertas para comercial: "pico de 'relaxing' esperado em X dias"

**Impacto Esperado:**
- Preparação comercial proativa
- Redução de out-of-stock em picos
- Descoberta de long-tail de ocasiões
- Aumento de share em momentos-chave

**Complexidade:** Média-Alta  
**Time to Value:** 3-4 meses  
**Dependencies:**
- Histórico de vendas taggeado por ocasião
- Calendário de eventos (futebol, feriados)
- Dados externos (clima, eventos locais)

**Owner:** Growth & Dados + Comercial + AI

---

### 🎯 INVESTIMENTO ESTRATÉGICO - Commercial Calendar

#### 10. Predição e Otimização de KSMs/Holidays
**Problema:** 37% do GMV em 9-10 semanas. Efeito rebote pós-pico (-8% freq, -10pp ret). Operação reativa em 2025.

**Solução AI:**
- **Forecast de demanda por KSM:** Predizer volume esperado com 2-4 semanas de antecedência
- **Otimização de incentivos (pré/durante/pós):**
  - Pré-feriado: identificar quem antecipar (propensão a comprar early)
  - Durante: alocação dinâmica de subsídio (frete vs cupom vs cashback)
  - Pós-feriado: modelo de "ritual digital" - quem trazer de volta e com qual mecânica
- **Simulação de P&L:** Testar cenários de mix de incentivos antes de executar
- **Propensity to Convert por KSM:** Usuários com maior probabilidade de engajar em cada tipo de evento

**Impacto Esperado:**
- Reduzir custo de mídia emergencial em -10% (R$ 7MM economia)
- Recuperar +3pp retenção pós-KSM (+R$ 8,4MM GMV)
- Aumentar GMV nos picos em +5% (+R$ 60MM)
- **Total:** +R$ 75MM incremental

**Complexidade:** Alta  
**Time to Value:** 3-4 meses (modelo pronto antes Carnaval 2026)  
**Dependencies:**
- Histórico de KSMs 2023-2025 (volume, subsídios, retenção)
- P&L detalhado por evento
- Calendário 2026 consolidado
- Integração com comercial (Leonardo)

**Owner:** AI + Comercial + Growth & Dados

---

#### 11. Sincronização Inteligente Mídia × CRM (Audience Unification)
**Problema:** Sobreposição de investimento. Mesmo usuário impactado por mídia e CRM sem coordenação. CAC não otimizado.

**Solução AI:**
- **Modelo de "Next Best Action":** Para cada usuário, qual canal usar (CRM vs Mídia vs Ambos)?
- **Supressão inteligente:** Não bombardear com mídia quem já recebeu CRM e converteu
- **Orquestração de frequência:** Considerar todos os touchpoints (push, email, Meta, Google) e distribuir ao longo do tempo
- **Lookalike otimizado:** Criar audiências para mídia baseadas em quem responde melhor a CRM (e vice-versa)
- **Medição de incrementalidade:** A/B por célula para saber o que é realmente incremental

**Impacto Esperado:**
- Redução de CAC médio (economia em verba)
- Aumento de conversão por real investido
- Evitar wasted impressions
- Janela de conversão <7d

**Complexidade:** Média-Alta  
**Time to Value:** 4-5 meses  
**Dependencies:**
- CDP configurado (unificação de ID)
- Integrações Meta + Google + Braze
- Modelo de atribuição multi-touch
- Colaboração com Ana Porchat + Larissa (CRM) + Yohanna/Felipe (Mídia)

**Owner:** AI + CRM + Marketing

---

#### 12. Rituals Engine: Gamificação Pós-KSM
**Problema:** Picos não viram hábito. Usuários compram no feriado e desaparecem.

**Solução AI:**
- **Identificação de "ritual potencial":** Quais usuários têm maior propensão a criar hábito após um KSM?
- **Missões personalizadas pós-evento:**
  - Ex: "Comprou no Carnaval? Complete 2 compras nas próximas 2 semanas e ganhe X pontos ZEC"
  - Progressão visível no app (gamification)
- **Predição de próxima ocasião:** "Você comprou para o churrasco, que tal um jantar em família na quarta?"
- **Triggers de ritual:** Notificações contextuais para manter o momentum

**Impacto Esperado:**
- Mitigar efeito rebote (-8% freq → -2% freq)
- Transformar 20-30% dos "pico buyers" em recorrentes
- Aumentar retenção 30D em +3pp
- MVP "Zé Presente" (mencionado no plano)

**Complexidade:** Média-Alta  
**Time to Value:** 3-4 meses (piloto Carnaval)  
**Dependencies:**
- Integração com Zé Compensa (gamificação)
- Produto: espaço no app para missões
- Dados enriquecidos de ocasiões

**Owner:** AI + Produto + CRM + Marketing

---

### 🎨 BRANDING & EXPERIÊNCIA - Build an Iconic Fun Brand

#### 13. AI-Powered Brand Health Monitor
**Problema:** Zé investe 3% da categoria mas tem 75% de lembrança. Necessidade de monitorar percepção de marca em tempo real para otimizar criatividade como amplificador.

**Solução AI:**
- **Análise de Sentiment em tempo real:**
  - Social listening (Twitter, Instagram, TikTok)
  - Sentiment analysis de menções (positivo/negativo/neutro)
  - Detecção de momentos virais
  - Tracking de associações: "Zé" + "diversão" vs "Zé" + "preço"
- **Brand Health Score:**
  - Meaningful (affinity + meet needs)
  - Saliência (top of mind)
  - Confiança
  - Worth perception
- **Competitive Intelligence:**
  - Share of voice vs competidores
  - Análise de campanhas concorrentes
  - Identificação de ameaças de branding

**Impacto Esperado:**
- Detectar early signals de mudança de percepção
- Otimizar campanhas em real-time
- Validar se stunts estão gerando conexão emocional
- ROI de investimento criativo

**Complexidade:** Média  
**Time to Value:** 2-3 meses  
**Dependencies:**
- APIs de social media
- Histórico de campanhas + resultados
- Integração com KPIs de marca (Meaningful, Saliência)

**Owner:** AI + Marketing

---

#### 14. Creative Effectiveness Predictor
**Problema:** Investir em stunts criativos sem saber se gerarão lembrança. Como prever viralidade e impacto de marca antes de executar?

**Solução AI:**
- **Predição de viralidade:**
  - Score de potencial viral para cada conceito criativo
  - Análise de elementos que historicamente geraram buzz
  - Benchmark vs campanhas passadas (Zé e mercado)
- **A/B testing criativo:**
  - Testar variações de mensagem/visual com micro-audiências
  - Predizer performance antes de investir full budget
- **Creative Spectrum Score:**
  - Avaliar se criativo está "safe" ou "disruptivo"
  - Balancear portfólio de campanhas (alguns safe, alguns punch)

**Impacto Esperado:**
- Reduzir risco de campanhas que não performam
- Aumentar hit rate de stunts memoráveis
- Otimizar produção criativa (focar no que funciona)

**Complexidade:** Alta  
**Time to Value:** 4-6 meses  
**Dependencies:**
- Histórico de campanhas com KPIs de resultado
- Parceria com agências criativas
- Dados de mercado (virais passados)

**Owner:** AI + Marketing

---

#### 15. Sacooler Personalization & Monetization Engine
**Problema:** Sacooler como DBA. Como maximizar impacto via personalização e monetizar via collabs?

**Solução AI:**
- **Recomendação de Sacooler:**
  - Qual sacooler oferecer para cada usuário? (times, ídolos, ocasiões)
  - Predição de propensão a comprar combo sacooler
  - Cross-sell inteligente: "Adicione sacooler do [seu time]"
- **Otimização de Collabs:**
  - Quais marcas/ídolos têm maior afinidade com base?
  - Predição de demanda para cada tipo de sacooler
  - Forecast de estoque por regional
- **Dynamic Pricing Sacooler:**
  - Precificação por demanda (ex: sacooler do Flamengo em jogo decisivo)
  - Monetização de parceiros

**Impacto Esperado:**
- Aumentar % de orders com sacooler
- AOV incremental por combos
- Receita de monetização de collabs
- Fill rate otimizado (menos out-of-stock)

**Complexidade:** Média-Alta  
**Time to Value:** 3-4 meses  
**Dependencies:**
- Feature de combo sacooler (Produto)
- Dados de preferências (time, ídolo, ocasião)
- Integração com comercial (Fabio Glezer)

**Owner:** AI + Produto + Comercial

---

#### 16. Experience Quality Score (5-6 Estrelas)
**Problema:** Brand stewardship exige consistência em todos touchpoints. Como garantir experiência "UAU" em escala?

**Solução AI:**
- **Predição de NPS por pedido:**
  - Antes de entregar, prever se pedido terá problema
  - Fatores: tempo entrega, temperatura, motoca equipado, produto certo
  - Intervenção proativa (ex: compensação antes de reclamar)
- **Quality Score por POC/Motoca:**
  - Ranking de sellers por experiência entregue
  - Identificar motocas que precisam de treinamento/equipamento
  - Priorizar investimento em praças/sellers que mais impactam NPS
- **Root Cause Analysis automático:**
  - Quando NPS baixo, identificar automaticamente causa raiz
  - Dashboards para operações (Fabio Glezer)

**Impacto Esperado:**
- Aumentar NPS consumer
- Fill rate e one score otimizados
- Reduzir churn por má experiência
- Direcionar investimento em experiência 5-6 estrelas

**Complexidade:** Média-Alta  
**Time to Value:** 3-4 meses  
**Dependencies:**
- Dados operacionais (tempo entrega, temperatura, etc.)
- NPS por pedido
- Integração com operações

**Owner:** AI + Operações

---

#### 17. Brandbook 2.0: AI-Assisted Brand Consistency
**Problema:** Evoluir brandbook para consistência em todos canais. Como garantir que materiais seguem guidelines sem gargalo de aprovação?

**Solução AI:**
- **Brand Compliance Checker:**
  - Upload de material (banner, post, OOH)
  - AI valida se segue brandbook (cores, fontes, tom, logos)
  - Score de compliance + sugestões de correção
- **Asset Generation:**
  - Gerar variações de materiais respeitando guidelines
  - Ex: "Criar banner Instagram para Carnaval mantendo brand"
- **Dilema Amarelo:**
  - Analisar presença de amarelo em competidores
  - Sugerir variações de paleta que mantêm distinctiveness

**Impacto Esperado:**
- Escala de produção de materiais
- Consistência de marca em todos touchpoints
- Reduzir tempo de aprovação
- Liberar time criativo para estratégia

**Complexidade:** Média  
**Time to Value:** 3-4 meses  
**Dependencies:**
- Brandbook digitalizado (guidelines claras)
- Parceria com Gut design
- Biblioteca de assets aprovados

**Owner:** AI + Marketing

---

### 💡 EXPLORATÓRIO - Médio Prazo

#### 7. Zé Everywhere: Conversational Commerce com IA
**Problema:** Expansão para WhatsApp e canais conversacionais. Benchmark iFood (Ailo).

**Solução AI:**
- Chatbot/assistente para WhatsApp
- Compreensão de linguagem natural: "quero algo pro churrasco de amanhã"
- Recomendação + checkout conversacional
- Reordenar via voz/texto

**Impacto Esperado:**
- Aumento de MAU por novo canal
- Redução de atrito (compra onde está o usuário)
- Conversão de usuários que não querem baixar app

**Complexidade:** Alta  
**Time to Value:** 6+ meses  
**Dependencies:**
- Infraestrutura WhatsApp Business
- Integração pagamento/carrinho via API
- LLM + RAG (contexto catálogo)
- Piloto AILO by Zé (já mencionado no plano)

**Owner:** Produto + AI

---

#### 8. Geração de Conteúdo para Comunicações
**Problema:** Produção contínua de conteúdo para 5 ocasiões + calendário fun moments. Toolkits flexíveis para app, CRM, mídia.

**Solução AI:**
- Geração de copy para push notifications (teste A/B)
- Sugestões de bundles por ocasião
- Personalização de mensagem mantendo brand voice
- Asset variations (headlines, CTAs)

**Impacto Esperado:**
- Escala de produção de conteúdo
- Velocidade de test & learn
- Personalização de mensagens

**Complexidade:** Média  
**Time to Value:** 2-3 meses (piloto)  
**Dependencies:**
- Guidelines de brand voice
- Aprovação legal/compliance
- Integração com fluxo criativo

**Owner:** Marketing + AI

---

#### 9. Otimização Dinâmica de Preços e Promos
**Problema:** Playbook de ofertas fixo. Oportunidade de precificação dinâmica por usuário/ocasião/estoque.

**Solução AI:**
- Elasticidade de preço por usuário/categoria
- Sugestão de descontos ótimos (não deixar dinheiro na mesa)
- Otimização de bundles (quais produtos juntos maximizam AOV)
- Promoções preditivas (quando oferecer desconto a cada usuário)

**Impacto Esperado:**
- Aumento de margeм
- AOV otimizado
- Conversão sem over-discount

**Complexidade:** Alta  
**Time to Value:** 6+ meses  
**Dependencies:**
- Dados de elasticidade
- Regras de negócio comercial
- Simulações financeiras

**Owner:** Comercial + Growth & Dados + AI

---

## 📋 Matriz de Priorização AI

### Quick Wins & Alta Prioridade

| # | Oportunidade | Impacto | Impacto $ | Complexidade | Time to Value | Prioridade |
|---|--------------|---------|-----------|--------------|---------------|------------|
| 1 | LLM Recomendação Contextual | Alto | GMV ↑ | Média | 2-3 meses | 🔥 ALTA |
| 2 | Modelo Preditivo Reativação | Alto | +R$ 10,8 Mi | Média-Alta | 2-3 meses | 🔥 ALTA |
| 3 | Triggers Comportamentais | Alto | Conversão ↑ | Alta | 3-4 meses | 🔥 ALTA |
| 10 | **Predição/Otimização KSMs** | **Muito Alto** | **+R$ 75 MM** | Alta | 3-4 meses | 🔥 **ALTA** |
| 13 | **Brand Health Monitor** | **Alto** | **ROI Criativo** | Média | 2-3 meses | 🔥 **ALTA** |

### Investimento Estratégico

| # | Oportunidade | Impacto | Impacto $ | Complexidade | Time to Value | Prioridade |
|---|--------------|---------|-----------|--------------|---------------|------------|
| 4 | Personas Dinâmicas + 1:1 | Muito Alto | +R$ 50 Mi | Alta | 4-6 meses | 🎯 ESTRATÉGICO |
| 5 | Orquestração Campanhas | Alto | ROI ↑ | Alta | 4-6 meses | 🎯 ESTRATÉGICO |
| 11 | Sincronização Mídia × CRM | Alto | CAC ↓ | Média-Alta | 4-5 meses | 🎯 ESTRATÉGICO |
| 12 | Rituals Engine (Gamificação) | Alto | +R$ 8 Mi | Média-Alta | 3-4 meses | 🎯 ESTRATÉGICO |
| 6 | Predição de Ocasiões | Médio-Alto | Estoque ↑ | Média-Alta | 3-4 meses | 🎯 ESTRATÉGICO |
| 15 | **Sacooler Personalization** | **Médio-Alto** | **AOV + Monetização** | Média-Alta | 3-4 meses | 🎯 **ESTRATÉGICO** |
| 16 | **Experience Quality Score** | **Alto** | **NPS ↑** | Média-Alta | 3-4 meses | 🎯 **ESTRATÉGICO** |

### Exploratório

| # | Oportunidade | Impacto | Impacto $ | Complexidade | Time to Value | Prioridade |
|---|--------------|---------|-----------|--------------|---------------|------------|
| 14 | Creative Effectiveness Predictor | Alto | Hit Rate ↑ | Alta | 4-6 meses | 💡 EXPLORATÓRIO |
| 17 | Brandbook 2.0 (AI Consistency) | Médio | Eficiência | Média | 3-4 meses | 💡 EXPLORATÓRIO |
| 7 | Conversational Commerce | Alto | MAU ↑ | Alta | 6+ meses | 💡 EXPLORATÓRIO |
| 8 | Geração de Conteúdo | Médio | Eficiência | Média | 2-3 meses | 💡 EXPLORATÓRIO |
| 9 | Otimização Preços Dinâmica | Alto | Margem ↑ | Alta | 6+ meses | 💡 EXPLORATÓRIO |

---

## 🔗 Conecta com Outras Áreas/Temas

### Prováveis Conexões

- **🦀 Delight Our Ecosystem:** Personalização beneficia sellers e consumidores
- **🍷 Develop Categories:** Recomendações cross-category impulsionam novas categorias
- **🔄 Drive Advantage Through:** IA como diferencial competitivo
- **🍺 Elevate Experiences:** Conversational commerce e personalização melhoram UX
- **🧮 Optimize Foundations:** Automação libera time para estratégia

---

## 💼 Recursos Necessários (AI)

### Time de AI

**Imediato (Q1 2026):**
- 2 ML Engineers (modelos preditivos)
- 1 Data Scientist (análise de ocasiões, personas)
- 1 LLM/NLP Specialist (recomendações, conversational)
- 1 AI Product Manager (priorização, roadmap)

**Médio Prazo (Q2-Q3 2026):**
- +1 ML Engineer (escala)
- +1 MLOps Engineer (infraestrutura, deploy)

### Infraestrutura

- **Compute:** GPU para treinamento de modelos
- **LLM API:** OpenAI/Anthropic para recomendações e conversational
- **Feature Store:** Centralizar features para modelos
- **MLOps:** Deploy, monitoring, retraining automatizado

### Dados

- **Enriquecimento urgente:**
  - Marca preferida (usuários ativos)
  - Ocasião de consumo (survey + inferência)
  - Preferências de categoria
  
- **Integrações:**
  - Clima (API externa)
  - Eventos (calendário esportivo, feriados)
  - Geolocalização enriquecida

### Budget Estimado

**Inicial (6 meses):**
- Headcount: R$ 600k (5 pessoas)
- Infraestrutura: R$ 80k (GPU, APIs)
- Ferramentas: R$ 40k (MLOps, monitoramento)
- **Total:** R$ 720k

**Retorno Esperado (baseado em hipóteses do plano):**
- Reativação: R$ 10,8 Mi GMV
- FMRR: R$ 11,7 Mi GMV
- Personas/Retenção: R$ 39,2 Mi GMV
- **KSMs/Holidays (novo):** R$ 75 MM GMV
- **Rituals Engine:** R$ 8 Mi GMV
- **Total conservador:** R$ 145 Mi GMV (ROI >200x)

---

## ⚠️ Riscos e Dependências

### Riscos

1. **Dados insuficientes/baixa qualidade**
   - Mitigação: Começar por enriquecimento de base (já no plano)

2. **Adoção pelo time de produto**
   - Mitigação: Co-criar, mostrar quick wins, evangelização

3. **Complexidade de integração**
   - Mitigação: Começar com POCs desacoplados, evoluir para produção

4. **Privacidade/LGPD**
   - Mitigação: Compliance by design, anonimização quando possível

### Dependências Críticas

- ✅ Braze (já em uso)
- ✅ CDP (já em uso)
- ⚠️ Enriquecimento de base (em progresso)
- ⚠️ Backlog produto (home dinâmica, espaços personalizáveis)
- ❌ Ferramenta orquestrador (Digital Insights - a desenvolver)
- ❌ APIs externas (clima, eventos)

---

## 🎯 Recomendações para Head de AI

### Imediato (Q1 2026)

1. **Alinhar com stakeholders principais:**
   - Yohanna (owner Accelerate Growth)
   - Leonardo Trindade (Comercial - KSMs)
   - Ciro (Growth & Dados)
   - Larissa + Ana Porchat (CRM)
   - Fernanda (Produto)

2. **Definir 2-3 Quick Wins para Q1:**
   - **URGENTE:** Modelo Predição KSMs (precisa estar pronto antes Carnaval 2026)
   - **Sugestão #1:** Predição/Otimização Holidays & KSMs
   - **Sugestão #2:** Modelo Preditivo Reativação
   - **Sugestão #3:** LLM Recomendação Contextual
   - Objetivo: Mostrar valor rápido antes do primeiro grande pico do ano

3. **Estruturar time:**
   - Priorizar contratações críticas
   - Alocar recursos existentes (se houver)

4. **Preparar infraestrutura básica:**
   - Ambiente de desenvolvimento
   - Acesso a dados
   - Integração Braze (sandbox)

### Médio Prazo (Q2-Q3 2026)

5. **Escalar Quick Wins:**
   - Levar pilotos para produção
   - Medir incrementalidade (teste A/B)

6. **Iniciar Investimentos Estratégicos:**
   - Personas Dinâmicas
   - Orquestração de Campanhas

7. **Evangelização:**
   - Showcases mensais
   - Training para times (como usar AI)

### Estrutural

8. **Criar AI Council:**
   - Governança de projetos AI
   - Priorização cross-área
   - Share de aprendizados

9. **Definir Métricas de AI:**
   - Não apenas acurácia, mas impacto negócio
   - Dashboards de AI performance

10. **Roadmap 2026 de AI:**
    - Consolidar após receber todos os temas
    - Alinhar com liderança

---

## 📅 Next Steps

### Urgente (Próximas 2 Semanas)
- [ ] **CRÍTICO:** Agendar sync com Leonardo (Comercial) sobre Calendário KSMs 2026
  - Objetivo: Entender P&L por feriado, dados históricos disponíveis
  - Deadline: Modelo de KSM precisa estar pronto antes Carnaval (fev/mar 2026)
- [ ] Solicitar dados históricos KSMs 2023-2025 (volume, subsídios, retenção pós-evento)
- [ ] Validar acesso a dados comerciais (elasticidade, ROI por evento)

### Curto Prazo (Q4 2025)
- [ ] Receber detalhamento Iniciativas:
  - Comercial 2: Develop Weekdays
  - Comercial 3: Regional Growth
  - Consumer Engagement: Iniciativa 3 (Regional T3/T4)
- [ ] Agendar sync com Yohanna + Ciro + Leonardo para deep dive estratégico
- [ ] Validar feasibility técnica com time de dados (Ciro)
- [ ] Priorizar 2-3 projetos para Q1 2026 (KSMs é obrigatório)
- [ ] Preparar pitch para liderança (ROI de AI: R$ 145Mi+ GMV)

### Médio Prazo (Q1 2026)
- [ ] Kickoff projeto KSMs/Holidays com Comercial
- [ ] POC Modelo Reativação
- [ ] POC LLM Recomendações
- [ ] Definir roadmap H1 2026

---

**Atualizado em:** 2025-11-07

