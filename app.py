# ==============================================================================
# CV INTERATIVO DIOGO RAMIRES - VERSÃO EXECUTIVA FULL-STACK (V_FINAL + MVPs)
# ==============================================================================
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Diogo Ramires | Lead Analytics Engineer & AI Solutions Architect",
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

# 3. BARRA LATERAL
with st.sidebar:
    st.markdown("### 👨‍💻 Diogo Ramires")
    st.caption("Lead Analytics Engineer | AI Solutions Architect")
    st.divider()
    st.markdown("📍 **Local:** Costa de Caparica, PT")
    st.markdown("✉️ **Email:** dbramires@gmail.com")
    st.markdown("📱 **Tel:** (+351) 964470366")
    st.divider()
    st.info("💡 Abordagem cognitiva assente em pensamento sistémico, facilidade de síntese de ecossistemas complexos e resolução de problemas estruturais de dados")

# 4. CABEÇALHO PRINCIPAL
st.title("Bridging Complex Data Architecture with CX Strategy")
st.markdown("*Data Translator e Arquiteto com 15+ anos de experiência. Transformo ecossistemas legados em Single Sources of Truth e ligo a infraestrutura analítica ao impacto financeiro e ao cliente.*")

# 5. KPIs EXECUTIVOS
st.markdown("### 🚀 Key Impact Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Omnichannel SLA", "<9% ➔ +90%", "IKEA Service Level")
col2.metric("Customer Satisfaction", "35 ➔ 85", "CSAT Growth")
col3.metric("ETL Processing", "24h ➔ 15m", "BringGlobal (Pharma)")
col4.metric("Infrastructure Cost", "$0/mês", "Serverless MVPs Cloud")

st.divider()

# 6. MENU DE NAVEGAÇÃO
st.write("")
menu = option_menu(
    menu_title=None,
    options=["Executive Summary", "Career Journey", "Startup MVPs & Arch", "Tech & AI Skills", "Cognitive & Soft Skills"],
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

# ----------------- EXECUTIVE SUMMARY -----------------
if menu == "Executive Summary":
    st.subheader("The Professional Profile")
    st.write(
        "Atuo na interseção entre a Engenharia de Dados (Cloud/ETL) e a Estratégia C-Level (CX/Operações). "
        "A minha carreira é marcada por modernizações técnicas profundas (Legacy ➔ Cloud), criação de modelação matemática para suporte à decisão, "
        "e liderança de Change Management que democratiza o acesso aos dados."
    )
    st.markdown("#### Core Value Proposition:")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        * **Engenharia & Arquitetura (SSOT):** Especialista em Refactoring de sistemas legados (SQL/PostgreSQL), migração para Microsoft Fabric/Azure, e criação de *Data Marts* que erradicam silos operacionais.
        * **CX & Business Partnering:** Tradução de dados em decisões de negócio. Histórico na gestão de insights que influenciaram 10-20% de uma operation nacional com faturação de 1.5M€/dia.
        """)
        
    with col_b:
        st.markdown("""
        * **Full-Stack & Cloud Serverless:** Domínio absoluto do ecossistema Microsoft (Power BI, Fabric), expansão recente para o Google Cloud Platform (BigQuery, Cloud Run, Vertex AI) e desenvolvimento Frontend (React, TypeScript).
        * **Advanced Analytics & IA:** Modelação preditiva e integração de LLMs (Gemini, Vertex AI). Especialista em implementações RAG (Retrieval-Augmented Generation) e normalização semântica via Vector Embeddings (Cosine Similarity).
        """)

# ----------------- CAREER JOURNEY (Corporativo) -----------------
elif menu == "Career Journey":
    st.subheader("Professional Journey & Impact")
    
    st.markdown("#### **BringGlobal** | Senior BI & Data Engineer *(2022 - 2026)*")
    st.markdown("""
    * **Turnaround Farmacêutico (Rede Claro):** Liderou a reconstrução arquitetónica de um sistema em rutura. Refatorou rotinas SQL de +5000 linhas, reduziu tabelas em 50%, e resolveu *technical debt* e bugs críticos arrastados há mais de 2 anos. Baixou tempos de ETL de 24h para 15 minutos, viabilizando a migração para MS Fabric e poupando >100k€/ano ao cliente.
    * **Telecomunicações (McKinsey):** Atuou como facilitador analítico, desbloqueando em poucas semanas a entrega de modelos complexos em Apache Superset, garantindo o sucesso do projeto e alavancando a expansão B2B (ex: Intel).
    * **Arquitetura Big Data (Banca):** Mapeamento e integração de ecossistemas bancários massivos utilizando Erwin Data Modeler, PySpark e MATLAB para pipelines de dados.
    """)
    
    st.markdown("---")
    
    st.markdown("#### **IKEA** | Customer Insights Lead & Business Data Analyst *(2014 - 2022)*")
    st.markdown("""
    * **Global Frameworks & KPIs:** Liderou ativamente o desenvolvimento estratégico de PIs e KPIs que inspiraram a framework Global de Performance e Qualidade (Customer Support, Remote Sales e VoC). Colaborou na convergência internacional do *Customer Value Model* (CVM).
    * **Pioneirismo, SSOT & Change Management:** Substituiu o 'Excel Hell' por uma Single Source of Truth através de Data Marts. Infiltrou metodologias de dados nas operações, reduzindo erros de vendas (de 30% ➔ <7%) e custos logísticos (20-30%).
    * **Extração Omnichannel & Automação:** Integrou telemetria complexa (Avaya/Genesys). Desenvolveu automações via Office 365 que pouparam o equivalente a 20 *headcounts*, suportando o aumento do SLA de <9% para >90%.
    * **Modelação C-Level & AI:** Utilizou NLP (Brandwatch/Iris) para quantificar o CSAT e aplicou *Structural Equation Modeling* para ligar a qualidade operacional aos resultados financeiros.
    """)
    
    st.markdown("---")
    
    st.markdown("#### **Early Career & B2B Foundation** | Banco BPI, Millennium & Central de Cervejas *(Até 2014)*")
    st.markdown("""
    * **Sales & CX Operations:** Gestão de carteiras B2B (HORECA) e atendimento ao cliente financeiro na linha da frente. Esta base relacional e comercial forjou a visão que guia hoje a minha engenharia de dados: a tecnologia não é o fim, é o meio para resolver a dor real do negócio e do utilizador final.
    """)

# ----------------- STARTUP MVPs & ARCHITECTURE (Projetos Recentes) -----------------
elif menu == "Startup MVPs & Arch":
    st.subheader("Independent Solutions Architect | Startup MVPs (2025 - Presente)")
    st.write("Fase recente dedicada à exploração das fronteiras da Cloud (GCP) e IA (Vertex AI/Gemini), desenvolvendo arquiteturas serverless de alta performance e custo operacional nulo para fundação de futuras ONGs/Startups.")
    
    st.markdown("#### 🏛️ Polanyi Lakehouse (Arquitetura & CI/CD)")
    st.markdown("""
    * **Medallion Architecture no BigQuery:** Arquitetou um Data Lakehouse físico (Camadas Bronze, Silver, Gold) para centralização de dados socioeconómicos (Eurostat/Banco Mundial) processados em Python.
    * **Pipelines de CI/CD & FinOps:** Implementação de pipelines automatizados via Google Cloud Build monitorizados por webhooks a partir do GitHub, incluindo testes de Data Quality e auditoria física de custos de computação (FinOps).
    * **Data Science (Structural Equation Modeling):** Modelação quantitativa da teoria de Karl Polanyi, normalizando indicadores complexos via Z-scores em SQL e integrando polígonos geográficos oficiais (NUTS) para renderização GIS no Looker Studio.
    """)
    
    st.markdown("#### 🧠 Inventário & Nutrição (IA Híbrida & NLP)")
    st.markdown("""
    * **Arquitetura Serverless:** Infraestrutura alojada em GCP (Cloud Run) com microsserviços ativados por webhooks sob demanda.
    * **NLP & Vector Embeddings:** Substituiu procuras exatas (VLOOKUP) por uma pipeline de Inteligência Artificial Híbrida utilizando a API Gemini 1.5 Flash (OCR) e *gemini-embedding-001*. Implementou cálculos matemáticos de Similaridade de Cosseno para normalização semântica de inventário.
    * **Governança (Funil de Confiança):** Desenvolveu um modelo de triagem onde o LLM atua como árbitro binário para limiares intermédios (65%-82%), assegurando a proteção e integridade relacional do stock.
    """)

    st.markdown("#### 📱 TripMillennium (React & Offline-First)")
    st.markdown("""
    * **Engenharia Frontend & Serverless:** Plataforma de logística modular desenvolvida do zero em React.js, TypeScript e Tailwind CSS (Vite bundler).
    * **Pipeline de Ingestão & Edge Caching:** Consumo assíncrono de bases de dados relacionais servidas via Google Edge Network. Utilizou PapaParse para processamento local (no browser), mitigando limites de quotas de APIs e melhorando tempos de carregamento (Offline-first).
    * **ETL de Ficheiros (BLOB Storage):** Construção de Webhooks assíncronos (Apps Script) para descodificar payloads de base64 provenientes do React, garantindo a gestão de PDFs e imagens como *Object Storage* no Google Drive com injeção automática de URLs na base de dados.
    """)

    st.markdown("#### 🕹️ Poke-Prices (Ecosystem & RAG)")
    st.markdown("""
    * **Modelagem & Idempotência:** Arquitetura *Galaxy Schema* no BigQuery com desduplicação cirúrgica através de funções de janela analítica (ROW_NUMBER).
    * **RAG (Retrieval-Augmented Generation):** Criação de um motor de análise tática que interseta relatórios textuais subjetivos com parâmetros quantitativos utilizando o modelo Gemini 1.5 Flash.
    """)

# ----------------- TECH & AI SKILLS -----------------
elif menu == "Tech & AI Skills":
    st.subheader("Hybrid Skillset (Tech, Data & CX)")
    col_radar, col_skills = st.columns([1.5, 1])
    
    with col_radar:
        categories = ['Advanced SQL / BigQuery', 'Cloud Run / AppSheet', 'React & TypeScript', 'Python, LLMs & RAG', 'BI & Analytics', 'CI/CD & FinOps']
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=[5, 4.5, 4, 4.5, 5, 4],
            theta=categories,
            fill='toself',
            name='Proficiency',
            line_color='#1e3d59'
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
            showlegend=False,
            margin=dict(t=20, b=20, l=20, r=20),
            height=400,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_radar, use_container_width=True)
        
    with col_skills:
        st.markdown("#### 🛠️ Tech Stack & Ecosystems")
        st.progress(95, text="Data & DBs: Adv. SQL, BigQuery, PostgreSQL, PySpark")
        st.progress(95, text="Cloud & Backend: GCP (Cloud Run, Cloud Build), Serverless, Webhooks")
        st.progress(85, text="Frontend: React.js, TypeScript, Tailwind CSS, AppSheet")
        st.progress(90, text="AI/ML: Vertex AI (Embeddings), Gemini 1.5, RAG, Python")
        st.progress(90, text="BI & Ops: Power BI, Looker Studio, CI/CD, Git")
        
        st.markdown("#### 🎓 Education")
        st.markdown("- **PG Digital Enterprise Management** (Nova IMS)")
        st.markdown("- **MSc Gestão - Tese 18 Val** (ISEG UL) *(Foco em SEM)*")
        st.markdown("- **BSc Ciência Política** (ISCSP UL)")

# ----------------- COGNITIVE & SOFT SKILLS -----------------
elif menu == "Cognitive & Soft Skills":
    st.subheader("Cognitive & Operational Style")
    st.write(
        "Uma perspetiva analítica de alto desempenho focada na resolução de problemas complexos, "
        "integridade ética e adaptabilidade em ambientes de dados dinâmicos."
    )
    
    col_radar_soft, col_skills_soft = st.columns([1.5, 1])
    
    with col_radar_soft:
        categories_soft = ['Pensamento Sistémico', 'Resolução de Problemas', 'Superfoco Imersivo', 'Integridade & Ética', 'Empatia & Colaboração', 'Aprendizagem Exponencial']
        fig_radar_soft = go.Figure()
        fig_radar_soft.add_trace(go.Scatterpolar(
            r=[5.0, 4.8, 4.7, 5.0, 4.5, 4.9],
            theta=categories_soft, fill='toself', name='Cognitive Fit', line_color='#1e3d59'
        ))
        fig_radar_soft.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False, margin=dict(t=20, b=20, l=20, r=20), height=400, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_radar_soft, use_container_width=True)
        
    with col_skills_soft:
        st.markdown("#### 🧠 Soft Power & Cognitive Fit")
        st.progress(98, text="Pensamento Sistémico: Visão SSOT e arquitetura conceptual 360º")
        st.progress(95, text="Resolução de Problemas: Reconhecimento de padrões em dados complexos")
        st.progress(95, text="Superfoco Imersivo: Elevada taxa de entrega em temas de alto valor técnico")
        st.progress(100, text="Integridade & Ética: Liderança pelo exemplo e forte lealdade à equipa")
        st.progress(90, text="Empatia & Colaboração: Comunicação assertiva e relações de confiança")
        st.progress(95, text="Aprendizagem Exponencial: Velocidade de absorção rápida de novas tecnologias")
        
    st.divider()
    
    col_style1, col_style2 = st.columns(2)
    with col_style1:
        st.markdown("#### ⚙️ Dinâmica Operacional (Como Trabalho)")
        st.markdown("* **Fase de Ancoragem Estratégica:** Início marcado por um mapeamento rigoroso e questionamento estruturado para garantir que as bases são sólidas.\n* **Dinamismo Multifocal:** Elevado desempenho ao gerir 2 a 3 projetos em simultâneo.\n* **Proteção do Fluxo:** Beneficia de blocos de tempo consolidados para transições de contexto complexas.")
    with col_style2:
        st.markdown("#### 🤝 Colaboração & Liderança")
        st.markdown("* **Liderança pelo Exemplo:** Autoridade conquistada através da competência e integridade moral.\n* **Comunicação Seletiva de Alto Impacto:** Transmite conhecimentos complexos com entusiasmo e clareza conceptual.\n* **Filosofia do Crescimento:** Alinhamento com a máxima de que 'onde um cresce, crescem todos'.")