# ==============================================================================
# INTERACTIVE CV DIOGO RAMIRES - MULTI-LANGUAGE (EN/PT) FULL-STACK
# ==============================================================================
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Diogo Ramires | Interactive CV",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. DESIGN (Custom CSS)
st.markdown("""
<style>
.metric-container { background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
h1, h2, h3 { color: #1e3d59; }
</style>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL & SELETOR DE IDIOMA
with st.sidebar:
    lang = st.radio("🌐 Language / Idioma", ["🇬🇧 EN", "🇵🇹 PT"])
    st.divider()
    
    st.markdown("### 👨‍💻 Diogo Ramires")
    st.caption("Lead Analytics Engineer | AI Solutions Architect")
    st.divider()
    
    if lang == "🇬🇧 EN":
        st.markdown("📍 **Location:** Costa de Caparica, PT")
        st.markdown("✉️ **Email:** dbramires@gmail.com")
        st.markdown("📱 **Phone:** (+351) 964470366")
        st.divider()
        st.info("💡 Cognitive approach built on systemic thinking, synthesis of complex ecosystems, and structural data problem-solving.")
    else:
        st.markdown("📍 **Local:** Costa de Caparica, PT")
        st.markdown("✉️ **Email:** dbramires@gmail.com")
        st.markdown("📱 **Tel:** (+351) 964470366")
        st.divider()
        st.info("💡 Abordagem cognitiva assente em pensamento sistémico, facilidade de síntese de ecossistemas complexos e resolução de problemas estruturais de dados.")

# 4. CABEÇALHO PRINCIPAL
if lang == "🇬🇧 EN":
    st.title("Bridging Complex Data Architecture with CX Strategy")
    st.markdown("*Data Translator and Architect with 15+ years of experience. I transform legacy ecosystems into Single Sources of Truth and connect analytical infrastructure to financial and customer impact.*")
else:
    st.title("A Ligar Arquitetura de Dados Complexa à Estratégia de CX")
    st.markdown("*Data Translator e Arquiteto com 15+ anos de experiência. Transformo ecossistemas legados em Single Sources of Truth e ligo a infraestrutura analítica ao impacto financeiro e ao cliente.*")

# 5. KPIs EXECUTIVOS
if lang == "🇬🇧 EN":
    st.markdown("### 🚀 Key Impact Metrics")
    m_sla, m_csat, m_etl, m_cost = "Omnichannel SLA", "Customer Satisfaction", "ETL Processing", "Infrastructure Cost"
    m_sla_desc, m_csat_desc, m_etl_desc, m_cost_desc = "IKEA Service Level", "CSAT Growth", "BringGlobal (Pharma)", "Serverless MVPs Cloud"
else:
    st.markdown("### 🚀 Key Impact Metrics")
    m_sla, m_csat, m_etl, m_cost = "SLA Omnichannel", "Satisfação do Cliente", "Processamento ETL", "Custo de Infraestrutura"
    m_sla_desc, m_csat_desc, m_etl_desc, m_cost_desc = "Nível de Serviço IKEA", "Crescimento CSAT", "BringGlobal (Pharma)", "Cloud Serverless (MVPs)"

col1, col2, col3, col4 = st.columns(4)
col1.metric(m_sla, "<9% ➔ +90%", m_sla_desc)
col2.metric(m_csat, "35 ➔ 85", m_csat_desc)
col3.metric(m_etl, "24h ➔ 15m", m_etl_desc)
col4.metric(m_cost, "$0/mês", m_cost_desc)

st.divider()

# 6. MENU DE NAVEGAÇÃO
st.write("")
if lang == "🇬🇧 EN":
    menu_options = ["Executive Summary", "Career Journey", "Startup MVPs & Arch", "Tech & AI Skills", "Cognitive & Soft Skills"]
else:
    menu_options = ["Resumo Executivo", "Percurso Profissional", "Startup MVPs & Cloud", "Skills Técnicas e IA", "Perfil Cognitivo & Soft Skills"]

menu = option_menu(
    menu_title=None,
    options=menu_options,
    icons=["person-vcard", "rocket", "box-seam", "cpu", "brain"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "border-radius": "10px"},
        "icon": {"font-size": "16px"},
        "nav-link": {"font-size": "14px", "text-align": "center", "margin":"0px", "--hover-color": "rgba(30, 61, 89, 0.1)"},
        "nav-link-selected": {"background-color": "#1e3d59", "color": "white"},
    }
)

st.divider()

# ================= SEÇÕES DE CONTEÚDO =================

if menu in ["Executive Summary", "Resumo Executivo"]:
    if lang == "🇬🇧 EN":
        st.subheader("The Professional Profile")
        st.write("I operate at the intersection of Data Engineering (Cloud/ETL) and C-Level Strategy (CX/Operations). My career is defined by deep technical modernizations (Legacy ➔ Cloud), mathematical modeling for decision support, and Change Management leadership that democratizes data access.")
        st.markdown("#### Core Value Proposition:")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("* **Engineering & Architecture (SSOT):** Expert in refactoring legacy systems (SQL/PostgreSQL), migrating to Microsoft Fabric/Azure, and creating Data Marts that eradicate operational silos.\n* **CX & Business Partnering:** Translating data into business decisions. Track record of managing insights that influenced 10-20% of a national operation generating €1.5M/day.")
        with col_b:
            st.markdown("* **Full-Stack & Cloud Serverless:** Mastery of the MS ecosystem (Power BI, Fabric), recent expansion into GCP (BigQuery, Cloud Run, Vertex AI) and Frontend development (React, TypeScript).\n* **Advanced Analytics & AI:** Predictive modeling and LLM integration (Gemini, Vertex AI). Specialist in RAG pipelines and semantic normalization via Vector Embeddings.")
    else:
        st.subheader("O Perfil Profissional")
        st.write("Atuo na interseção entre a Engenharia de Dados (Cloud/ETL) e a Estratégia C-Level (CX/Operações). A minha carreira é marcada por modernizações técnicas profundas (Legacy ➔ Cloud), criação de modelação matemática para suporte à decisão, e liderança de Change Management que democratiza o acesso aos dados.")
        st.markdown("#### Core Value Proposition:")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("* **Engenharia & Arquitetura (SSOT):** Especialista em Refactoring de sistemas legados (SQL/PostgreSQL), migração para MS Fabric/Azure, e criação de Data Marts que erradicam silos operacionais.\n* **CX & Business Partnering:** Tradução de dados em decisões de negócio. Histórico na gestão de insights que influenciaram 10-20% de uma operação nacional com faturação de 1.5M€/dia.")
        with col_b:
            st.markdown("* **Full-Stack & Cloud Serverless:** Domínio do ecossistema Microsoft, expansão recente para GCP (BigQuery, Cloud Run, Vertex AI) e desenvolvimento Frontend (React, TypeScript).\n* **Advanced Analytics & IA:** Modelação preditiva e integração de LLMs. Especialista em RAG e normalização semântica via Vector Embeddings (Cosine Similarity).")

elif menu in ["Career Journey", "Percurso Profissional"]:
    if lang == "🇬🇧 EN":
        st.subheader("Professional Journey & Impact")
        st.markdown("#### **BringGlobal** | Senior BI & Data Engineer *(2022 - 2026)*")
        st.markdown("* **Pharmaceutical Turnaround:** Led the architectural rebuild of a collapsing system. Refactored +5000 lines of SQL routines and reduced tables by 50%. Cut ETL times from 24h to 15 minutes, saving >€100k/year.\n* **Telecommunications (McKinsey):** Unblocked the delivery of complex models in Apache Superset within weeks, leveraging B2B expansion.\n* **Banking Big Data:** Mapped massive banking ecosystems using Erwin Data Modeler, PySpark, and MATLAB.")
        st.markdown("---")
        st.markdown("#### **IKEA** | Customer Insights Lead & Data Architect *(2014 - 2022)*")
        st.markdown("* **Global Frameworks & KPIs:** Led the development of PIs/KPIs that inspired the Global Performance framework (VoC).\n* **SSOT & Change Management:** Replaced 'Excel Hell' with a Single Source of Truth via Data Marts, reducing sales errors (30% ➔ <7%) and logistical costs.\n* **Omnichannel Automation:** Integrated Avaya/Genesys telemetry. Developed automations saving 20 headcounts, supporting the SLA jump from <9% to >90%.\n* **C-Level Modeling & AI:** Used NLP (Brandwatch) to quantify CSAT and applied Structural Equation Modeling (SEM) to link CX to financial results.")
        st.markdown("---")
        st.markdown("#### **Early Career & B2B Foundation** | Banco BPI & Central de Cervejas *(Up to 2014)*")
        st.markdown("* **Sales & CX Operations:** Managed B2B portfolios and frontline financial customer service. This forged the vision that guides my engineering today: technology must solve real business pain points.")
    else:
        st.subheader("Percurso Profissional & Impacto")
        st.markdown("#### **BringGlobal** | Senior BI & Data Engineer *(2022 - 2026)*")
        st.markdown("* **Turnaround Farmacêutico:** Reconstrução de um sistema em rutura. Refatorou rotinas SQL de +5000 linhas. Baixou tempos de ETL de 24h para 15 minutos, poupando >100k€/ano.\n* **Telecomunicações (McKinsey):** Desbloqueou em semanas a entrega de modelos em Apache Superset, alavancando expansão B2B.\n* **Arquitetura Banca:** Integração de ecossistemas massivos utilizando Erwin Data Modeler e PySpark.")
        st.markdown("---")
        st.markdown("#### **IKEA** | Customer Insights Lead & Data Architect *(2014 - 2022)*")
        st.markdown("* **Global Frameworks:** Liderou o desenvolvimento de KPIs que inspiraram a framework Global de Performance (VoC).\n* **SSOT:** Substituiu o 'Excel Hell' por Data Marts (SSOT), reduzindo erros de vendas (30% ➔ <7%) e custos logísticos.\n* **Automação Omnichannel:** Integrou telemetria Avaya/Genesys. Automações pouparam 20 headcounts e alavancaram o SLA de <9% para >90%.\n* **Modelação & AI:** NLP (Brandwatch) para CSAT e Modelação de Equações Estruturais (SEM) para ligar operações a finanças.")
        st.markdown("---")
        st.markdown("#### **Early Career & B2B Foundation** | Banco BPI & Central de Cervejas *(Até 2014)*")
        st.markdown("* **Vendas & Operações CX:** Linha da frente comercial e B2B. Forjou a visão de que a tecnologia é o meio para resolver a dor real do negócio.")

elif menu in ["Startup MVPs & Arch", "Startup MVPs & Cloud"]:
    if lang == "🇬🇧 EN":
        st.subheader("Independent Solutions Architect | Startup MVPs (2025 - Present)")
        st.markdown("#### 🏛️ Polanyi Lakehouse (Architecture & CI/CD)\n* **Medallion Architecture:** Data Lakehouse in BigQuery (Bronze, Silver, Gold) for socioeconomic data.\n* **CI/CD & FinOps:** Automated pipelines via Cloud Build and GitHub with cost auditing.\n* **Data Science (SEM):** Quantitative modeling normalizing indicators via Z-scores for GIS rendering.")
        st.markdown("#### 🧠 Inventory & Nutrition (Hybrid AI & NLP)\n* **Serverless GCP:** Microservices on Cloud Run triggered by webhooks.\n* **NLP & Vector Embeddings:** Replaced VLOOKUPs with Hybrid AI (Gemini 1.5 + Cosine Similarity) for semantic normalization.\n* **Trust Funnel:** LLM acts as an arbiter to protect relational database integrity.")
        st.markdown("#### 📱 TripMillennium (React & Offline-First)\n* **Frontend:** Modular logistics platform in React.js, TypeScript, and Tailwind CSS.\n* **Edge Caching:** Asynchronous database consumption via Google Edge Network (PapaParse) mitigating API limits.\n* **BLOB Storage:** Webhooks for decoding base64 payloads to Object Storage (Google Drive).")
    else:
        st.subheader("Arquiteto Independente | Startup MVPs (2025 - Presente)")
        st.markdown("#### 🏛️ Polanyi Lakehouse (Arquitetura & CI/CD)\n* **Medallion Architecture:** Lakehouse físico no BigQuery para centralização de dados socioeconómicos.\n* **CI/CD & FinOps:** Pipelines automatizados via Cloud Build com testes de Data Quality e auditoria FinOps.\n* **Data Science:** Modelação quantitativa via Z-scores em SQL para renderização GIS no Looker Studio.")
        st.markdown("#### 🧠 Inventário & Nutrição (IA Híbrida & NLP)\n* **Serverless GCP:** Cloud Run com microsserviços ativados por webhooks.\n* **Vector Embeddings:** Substituiu VLOOKUP por IA Híbrida (Gemini 1.5) e Similaridade de Cosseno.\n* **Governança:** Funil de Confiança onde o LLM atua como árbitro para proteger a integridade do stock.")
        st.markdown("#### 📱 TripMillennium (React & Offline-First)\n* **Frontend:** Plataforma logística em React.js, TypeScript e Tailwind CSS.\n* **Edge Caching:** Consumo via Google Edge Network. Processamento local no browser (Offline-first).\n* **BLOB Storage:** Webhooks assíncronos para PDFs/Imagens alojados como Object Storage com injeção automática de URLs na DB.")

elif menu in ["Tech & AI Skills", "Skills Técnicas e IA"]:
    st.subheader("Hybrid Skillset (Tech, Data & CX)")
    col_radar, col_skills = st.columns([1.5, 1])
    with col_radar:
        categories = ['Advanced SQL / BigQuery', 'Cloud Run / AppSheet', 'React & TypeScript', 'Python, LLMs & RAG', 'BI & Analytics', 'CI/CD & FinOps']
        fig_radar = go.Figure(go.Scatterpolar(r=[5, 4.5, 4, 4.5, 5, 4], theta=categories, fill='toself', line_color='#1e3d59'))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False, margin=dict(t=20, b=20, l=20, r=20), height=400, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_radar, use_container_width=True)
    with col_skills:
        st.markdown("#### 🛠️ Tech Stack & Ecosystems")
        st.progress(95, text="Data & DBs: Adv. SQL, BigQuery, PostgreSQL, PySpark")
        st.progress(95, text="Cloud & Backend: GCP, Serverless, Webhooks")
        st.progress(85, text="Frontend: React.js, TypeScript, Tailwind CSS")
        st.progress(90, text="AI/ML: Vertex AI, Gemini 1.5, RAG, Embeddings")
        st.progress(90, text="BI & Ops: Power BI, Looker Studio, CI/CD, Git")
        st.markdown("#### 🎓 Education")
        if lang == "🇬🇧 EN":
            st.markdown("- **PG Digital Enterprise Management** (Nova IMS)\n- **MSc Management - Thesis 18/20** (ISEG UL)\n- **BSc Political Science** (ISCSP UL)")
        else:
            st.markdown("- **PG Digital Enterprise Management** (Nova IMS)\n- **MSc Gestão - Tese 18 Val** (ISEG UL)\n- **BSc Ciência Política** (ISCSP UL)")

elif menu in ["Cognitive & Soft Skills", "Perfil Cognitivo & Soft Skills"]:
    if lang == "🇬🇧 EN":
        st.subheader("Cognitive & Operational Style")
        st.write("A high-performance analytical perspective focused on complex problem-solving, ethical integrity, and adaptability in dynamic data environments.")
        cat_soft = ['Systemic Thinking', 'Problem Solving', 'Immersive Hyperfocus', 'Integrity & Ethics', 'Empathy & Collaboration', 'Exponential Learning']
        texts = ["Systemic Thinking: SSOT vision and 360º conceptual architecture", "Problem Solving: Pattern recognition in complex data", "Immersive Hyperfocus: High delivery rate on high-value technical topics", "Integrity & Ethics: Leadership by example and strong team loyalty", "Empathy & Collaboration: Assertive communication and trusted relationships", "Exponential Learning: Rapid absorption of new technologies"]
    else:
        st.subheader("Perfil Cognitivo & Estilo Operacional")
        st.write("Uma perspetiva analítica de alto desempenho focada na resolução de problemas complexos, integridade ética e adaptabilidade em ambientes de dados dinâmicos.")
        cat_soft = ['Pensamento Sistémico', 'Resolução de Problemas', 'Superfoco Imersivo', 'Integridade & Ética', 'Empatia & Colaboração', 'Aprendizagem Exponencial']
        texts = ["Pensamento Sistémico: Visão SSOT e arquitetura conceptual 360º", "Resolução de Problemas: Reconhecimento de padrões em dados complexos", "Superfoco Imersivo: Elevada taxa de entrega em temas de alto valor técnico", "Integridade & Ética: Liderança pelo exemplo e forte lealdade à equipa", "Empatia & Colaboração: Comunicação assertiva e relações de confiança", "Aprendizagem Exponencial: Velocidade de absorção rápida de novas tecnologias"]

    col_radar_soft, col_skills_soft = st.columns([1.5, 1])
    with col_radar_soft:
        fig_radar_soft = go.Figure(go.Scatterpolar(r=[5.0, 4.8, 4.7, 5.0, 4.5, 4.9], theta=cat_soft, fill='toself', line_color='#1e3d59'))
        fig_radar_soft.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False, margin=dict(t=20, b=20, l=20, r=20), height=400, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_radar_soft, use_container_width=True)
    
    with col_skills_soft:
        st.markdown(f"#### 🧠 Soft Power & Cognitive Fit")
        scores = [98, 95, 95, 100, 90, 95]
        for t, s in zip(texts, scores):
            st.progress(s, text=t)
            
    st.divider()
    
    col_style1, col_style2 = st.columns(2)
    with col_style1:
        if lang == "🇬🇧 EN":
            st.markdown("#### ⚙️ Operational Dynamics (How I Work)")
            st.markdown("* **Strategic Anchoring Phase:** Begins with rigorous mapping and structured questioning to ensure solid foundations.\n* **Multifocal Dynamism:** High performance when managing 2 to 3 simultaneous projects.\n* **Flow Protection:** Benefits from consolidated time blocks for complex context switching.")
        else:
            st.markdown("#### ⚙️ Dinâmica Operacional (Como Trabalho)")
            st.markdown("* **Fase de Ancoragem Estratégica:** Início marcado por um mapeamento rigoroso e questionamento estruturado para garantir que as bases são sólidas.\n* **Dinamismo Multifocal:** Elevado desempenho ao gerir 2 a 3 projetos em simultâneo.\n* **Proteção do Fluxo:** Beneficia de blocos de tempo consolidados para transições de contexto complexas.")
    with col_style2:
        if lang == "🇬🇧 EN":
            st.markdown("#### 🤝 Collaboration & Leadership")
            st.markdown("* **Leadership by Example:** Authority earned through competence and moral integrity.\n* **High-Impact Selective Communication:** Conveys complex knowledge with enthusiasm and conceptual clarity.\n* **Growth Philosophy:** Aligned with the maxim that 'when one grows, everyone grows'.")
        else:
            st.markdown("#### 🤝 Colaboração & Liderança")
            st.markdown("* **Liderança pelo Exemplo:** Autoridade conquistada através da competência e integridade moral.\n* **Comunicação Seletiva de Alto Impacto:** Transmite conhecimentos complexos com entusiasmo e clareza conceptual.\n* **Filosofia do Crescimento:** Alinhamento com a máxima de que 'onde um cresce, crescem todos'.")