# ==============================================================================
# DIOGO RAMIRES - EXECUTIVE PORTFOLIO & INTERACTIVE CV
# ==============================================================================
import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Diogo Ramires | Technical Business Analyst & Data Architect",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. SOPHISTICATED EDITORIAL CSS (NO AI CLICHÉS)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #0f172a;
}

/* Main Headings */
h1 {
    font-weight: 700 !important;
    letter-spacing: -0.03em !important;
    color: #0f172a !important;
    font-size: 2.2rem !important;
    margin-bottom: 0.2rem !important;
}
h2, h3 {
    font-weight: 600 !important;
    letter-spacing: -0.02em !important;
    color: #0f172a !important;
}
h4 {
    font-weight: 600 !important;
    color: #1e293b !important;
    margin-top: 1.2rem !important;
    margin-bottom: 0.4rem !important;
}

/* Subtle Subtitle */
.hero-subtitle {
    font-size: 1.05rem;
    color: #475569;
    line-height: 1.6;
    margin-bottom: 1.8rem;
    max-width: 900px;
}

/* Executive KPI Cards */
.kpi-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 18px 20px;
    box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
    height: 100%;
}
.kpi-label {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #64748b;
    font-weight: 600;
}
.kpi-value {
    font-size: 1.55rem;
    font-weight: 700;
    color: #0f172a;
    margin: 6px 0 4px 0;
    letter-spacing: -0.02em;
}
.kpi-context {
    font-size: 0.8rem;
    color: #0284c7;
    font-weight: 500;
}

/* Role & Experience Cards */
.role-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 6px;
    margin-top: 20px;
    margin-bottom: 10px;
}
.role-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #0f172a;
}
.role-company {
    color: #0284c7;
    font-weight: 600;
}
.role-date {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #64748b;
}

/* Tech Stack Pills (Monkey See, Monkey Do for Recruiters) */
.tech-stack-bar {
    margin-top: 8px;
    margin-bottom: 18px;
}
.tech-pill {
    display: inline-block;
    background-color: #f1f5f9;
    color: #334155;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 3px 9px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.74rem;
    margin-right: 6px;
    margin-bottom: 6px;
    font-weight: 500;
}

/* Content Box */
.info-card {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3px solid #0f172a;
    padding: 16px 20px;
    border-radius: 6px;
    margin-bottom: 16px;
}
.info-card-title {
    font-weight: 600;
    font-size: 0.95rem;
    color: #0f172a;
    margin-bottom: 6px;
}
.info-card-body {
    font-size: 0.88rem;
    color: #475569;
    line-height: 1.55;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background-color: #f8fafc;
    border-right: 1px solid #e2e8f0;
}
.sidebar-name {
    font-size: 1.25rem;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.02em;
    margin-bottom: 2px;
}
.sidebar-role {
    font-size: 0.82rem;
    color: #0284c7;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 16px;
}
.sidebar-meta {
    font-size: 0.84rem;
    color: #475569;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

def render_pills(items):
    pills_html = "".join([f'<span class="tech-pill">{item}</span>' for item in items])
    st.markdown(f'<div class="tech-stack-bar">{pills_html}</div>', unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    lang = st.radio("Language / Idioma", ["EN", "PT"], horizontal=True)
    st.divider()
    
    st.markdown('<div class="sidebar-name">Diogo Ramires</div>', unsafe_allow_html=True)
    if lang == "EN":
        st.markdown('<div class="sidebar-role">Technical Business Analyst & Data Solutions Architect</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sidebar-meta">
        <strong>Location:</strong> Costa da Caparica, Lisbon<br>
        <strong>Email:</strong> dbramires@gmail.com<br>
        <strong>Phone:</strong> (+351) 964 470 366
        </div>
        """, unsafe_allow_html=True)
        st.divider()
        st.caption("PROFILE SYNTHESIS")
        st.write(
            "Analytical approach grounded in systemic thinking, translating complex legacy ecosystems "
            "into scalable data architectures and clear product specifications."
        )
    else:
        st.markdown('<div class="sidebar-role">Technical Business Analyst & Arquiteto de Dados</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sidebar-meta">
        <strong>Localização:</strong> Costa da Caparica, Lisboa<br>
        <strong>Email:</strong> dbramires@gmail.com<br>
        <strong>Telefone:</strong> (+351) 964 470 366
        </div>
        """, unsafe_allow_html=True)
        st.divider()
        st.caption("SÍNTESE DE PERFIL")
        st.write(
            "Abordagem analítica assente em pensamento sistémico, traduzindo ecossistemas legados complexos "
            "em arquiteturas de dados escaláveis e especificações claras de produto."
        )

# 4. HERO SECTION
if lang == "EN":
    st.title("Bridging Data Architecture with Product & Business Strategy")
    st.markdown(
        '<div class="hero-subtitle">'
        'With 15+ years across banking/financial operations, enterprise analytics, and customer experience, '
        'I translate business, regulatory, and user needs into scalable technical solutions, Single Sources of Truth (SSOT), '
        'and measurable P&L impact.'
        '</div>',
        unsafe_allow_html=True
    )
    kpis = [
        ("Transaction Scale", "€70M+ / yr", "Regulated Pharma & Banking Ecosystems"),
        ("ETL Refactoring", "24h → 15m", "75% Reduction in Maintenance Effort"),
        ("Omnichannel SLA", "<9% → >90%", "Enabled via SSOT & Workflow Design"),
        ("Enterprise Adoption", "400+ Users", "Daily Active Power BI & SAP Data Marts"),
    ]
    nav_options = ["Executive Summary", "Corporate Experience", "Cloud & SaaS Projects", "Technical Stack", "Operational Style"]
else:
    st.title("Arquitetura de Dados Alinhada à Estratégia de Produto e Negócio")
    st.markdown(
        '<div class="hero-subtitle">'
        'Com mais de 15 anos de experiência em operações bancárias/financeiras, dados empresariais e Customer Experience, '
        'traduzo necessidades de negócio, regulatórias e de utilizador em soluções técnicas escaláveis, Single Sources of Truth (SSOT) '
        'e impacto direto no P&L.'
        '</div>',
        unsafe_allow_html=True
    )
    kpis = [
        ("Escala Transacional", "€70M+ / ano", "Ecossistemas Regulados (Banca & Farma)"),
        ("Refactoring ETL", "24h → 15m", "Redução de 75% em Esforço de Manutenção"),
        ("SLA Omnichannel", "<9% → >90%", "Viabilizado via SSOT & Desenho de Workflows"),
        ("Adoção Corporativa", "400+ Users", "Utilizadores Diários em Data Marts SSOT"),
    ]
    nav_options = ["Resumo Executivo", "Experiência Corporativa", "Projetos Cloud & SaaS", "Stack Tecnológico", "Estilo Operacional"]

# 5. KPI CARDS
cols = st.columns(4)
for col, (label, val, ctx) in zip(cols, kpis):
    with col:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{val}</div>
            <div class="kpi-context">{ctx}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# 6. NAVIGATION MENU
menu = option_menu(
    menu_title=None,
    options=nav_options,
    icons=["file-earmark-text", "building", "layers", "terminal", "sliders"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "4px", "background-color": "#f1f5f9", "border-radius": "8px"},
        "icon": {"font-size": "14px", "color": "#475569"},
        "nav-link": {
            "font-size": "13.5px",
            "font-weight": "500",
            "text-align": "center",
            "margin": "0px 2px",
            "border-radius": "6px",
            "color": "#334155",
            "--hover-color": "#e2e8f0"
        },
        "nav-link-selected": {"background-color": "#0f172a", "color": "#ffffff", "font-weight": "600"},
    }
)

st.write("")

# ==============================================================================
# TAB 1: EXECUTIVE SUMMARY
# ==============================================================================
if menu in ["Executive Summary", "Resumo Executivo"]:
    if lang == "EN":
        st.markdown("#### Core Value Proposition")
        st.write(
            "I operate at the intersection of Data Engineering (Cloud/ETL) and Product/Business Analysis. "
            "Unlike purely functional analysts or isolated backend engineers, I audit legacy business logic directly in SQL, "
            "define functional requirements with stakeholders, and architect the underlying data models and APIs."
        )
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="info-card">
                <div class="info-card-title">Business Analysis & Product Delivery</div>
                <div class="info-card-body">
                Translation of business, regulatory, and operational bottlenecks into clear functional specifications, 
                User Stories, As-Is/To-Be workflows, and Acceptance Criteria. Proven track record in Backlog Refinement, 
                UAT, data reconciliation, and cross-functional alignment across Engineering, Product, and C-Level teams.
                </div>
            </div>
            <div class="info-card">
                <div class="info-card-title">Enterprise Data Architecture (SSOT)</div>
                <div class="info-card-body">
                Specialist in refactoring high-volume legacy systems (SQL/PostgreSQL), preparing migration roadmaps to 
                Microsoft Fabric/Azure, and designing centralized Data Marts that eliminate departmental silos ("Excel Hell").
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="info-card">
                <div class="info-card-title">CX Operations & Financial Impact</div>
                <div class="info-card-body">
                Integration of contact center telemetry (Genesys, Avaya) with core ERP/billing systems (SAP, OCP). 
                Application of Cost-to-Serve and root-cause analysis (including SEM modeling) to connect operational 
                performance directly to national P&L margins.
                </div>
            </div>
            <div class="info-card">
                <div class="info-card-title">Modern Cloud, APIs & Applied AI</div>
                <div class="info-card-body">
                Hands-on architecture across GCP (BigQuery, Cloud Run, Cloud Build), REST APIs, Webhooks, and React/TypeScript. 
                Pragmatic implementation of RAG pipelines and LLM validation (Vertex AI/Gemini) focused on data integrity and ROI.
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("#### Proposta de Valor Central")
        st.write(
            "Atuo na interseção entre a Engenharia de Dados (Cloud/ETL) e a Análise de Negócio e Produto. "
            "Ao contrário de analistas puramente funcionais ou engenheiros isolados do negócio, audito a lógica legada diretamente em SQL, "
            "defino os requisitos funcionais com os stakeholders e desenho a arquitetura de dados e APIs que suporta o produto."
        )
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="info-card">
                <div class="info-card-title">Business Analysis & Entrega de Produto</div>
                <div class="info-card-body">
                Tradução de estrangulamentos operacionais, de negócio e regulatórios em especificações funcionais claras, 
                User Stories, mapeamento de processos As-Is/To-Be e Critérios de Aceitação. Experiência sólida em Backlog Refinement, 
                UAT, reconciliação de dados e alinhamento entre Engenharia, Produto e C-Level.
                </div>
            </div>
            <div class="info-card">
                <div class="info-card-title">Arquitetura de Dados Empresarial (SSOT)</div>
                <div class="info-card-body">
                Especialista em refactoring de sistemas legados de elevado volume (SQL/PostgreSQL), preparação de roadmaps 
                de migração para Microsoft Fabric/Azure e criação de Data Marts centralizados que erradicam silos operacionais.
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="info-card">
                <div class="info-card-title">Operações CX & Impacto no P&L</div>
                <div class="info-card-body">
                Integração de telemetria de contact center (Genesys, Avaya) com sistemas core de faturação/ERP (SAP, OCP). 
                Aplicação de análises Cost-to-Serve e root-cause analysis (incluindo modelação SEM) para ligar a qualidade 
                operacional às margens financeiras.
                </div>
            </div>
            <div class="info-card">
                <div class="info-card-title">Cloud Moderna, APIs & IA Aplicada</div>
                <div class="info-card-body">
                Arquitetura prática em GCP (BigQuery, Cloud Run, Cloud Build), REST APIs, Webhooks e React/TypeScript. 
                Implementação pragmática de pipelines RAG e validação por LLMs (Vertex AI/Gemini) focada em integridade de dados e ROI.
                </div>
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# TAB 2: CORPORATE EXPERIENCE (PRIORITIZED)
# ==============================================================================
elif menu in ["Corporate Experience", "Experiência Corporativa"]:
    if lang == "EN":
        st.markdown("""
        <div class="role-header">
            <div><span class="role-company">BringGlobal</span> &nbsp;|&nbsp; <span class="role-title">Senior BI & Data Engineer / Technical Business Analyst</span></div>
            <div class="role-date">2022 – 2025 | Lisbon, PT</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        * **Regulated & High-Volume Ecosystems:** Mapped and optimized banking and pharmaceutical data ecosystems supporting 85+ retail pharmacies, laboratory integrations, and over €70M in annual transaction volume, ensuring strict compliance and data reconciliation.
        * **Requirement Translation & System Refactoring:** Audited legacy business logic and operational bottlenecks, translating business needs into functional and technical specifications. Led the architectural rebuild (refactoring 5,000+ lines of SQL and reducing database tables by 50%) while preparing the migration roadmap to Microsoft Fabric.
        * **Operational & Financial Impact:** Cut critical ETL processing times from 24 hours to 15 minutes and reduced architectural maintenance effort by 75% (from ~1,600h to ~400h/year), securing a €100k+/year contract and restoring reporting reliability for the CFO.
        * **Cross-Functional Delivery (McKinsey):** Acted as the bridge between McKinsey strategy consultants and engineering teams to clarify requirements, unblock data dependencies, and deliver complex analytical models in Apache Superset within weeks for B2B telecom expansion.
        """)
        render_pills(["Advanced SQL", "PostgreSQL", "Microsoft Fabric", "Azure Data Factory", "Power BI", "Apache Superset", "PySpark", "Erwin Data Modeler", "Agile/Scrum"])

        st.markdown("""
        <div class="role-header">
            <div><span class="role-company">IKEA</span> &nbsp;|&nbsp; <span class="role-title">Customer Insights Lead & Business Data Architect</span></div>
            <div class="role-date">2014 – 2022 | Lisbon, PT</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        * **User Insights & Product Analytics:** Led the design of Voice of Customer (VoC) KPIs that informed the Global Performance framework. Analyzed customer feedback and user behavior (via NLP/Brandwatch and web telemetry) to identify operational pain points and structure the frontline Knowledge Base.
        * **Cross-System Integration & SSOT:** Eliminated departmental silos ("Excel Hell") by integrating contact center telemetry (Avaya, Genesys) with core ERP/billing systems (SAP, OCP) into centralized Power BI Data Marts serving 400+ daily users.
        * **Workflow Optimization & Operational Support:** Defined functional workflows, monitoring tools, and system requirements that enabled operational and sales teams to reduce sales errors from 30% to <7%, cut logistics costs by 20–30%, and increase Omnichannel SLA performance from <9% to >90%.
        * **Change Management & Executive Alignment:** Maintained functional documentation, led user onboarding and training across operations, and partnered with executive leadership using Cost-to-Serve and root-cause analysis (including SEM modeling) to link operational quality to national P&L margins.
        """)
        render_pills(["Power BI", "SQL", "SAP", "OCP", "Genesys", "Avaya", "Brandwatch (NLP)", "Data Marts (SSOT)", "Process Mapping"])

        st.markdown("""
        <div class="role-header">
            <div><span class="role-company">Banco BPI & Central de Cervejas</span> &nbsp;|&nbsp; <span class="role-title">Sales & CX Operations Analyst</span></div>
            <div class="role-date">Up to 2014 | Portugal</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        * **Banking & Commercial Foundation:** Managed B2B portfolios and frontline banking customer service at Banco BPI, building a strong foundation in financial products, credit/commercial workflows, and translating end-user pain points into reporting requirements.
        """)
        render_pills(["Banking Operations", "Credit Workflows", "B2B Portfolio Management", "CRM", "Operational Reporting"])

    else:
        st.markdown("""
        <div class="role-header">
            <div><span class="role-company">BringGlobal</span> &nbsp;|&nbsp; <span class="role-title">Senior BI & Data Engineer / Technical Business Analyst</span></div>
            <div class="role-date">2022 – 2025 | Lisboa, PT</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        * **Ecossistemas Regulados de Elevado Volume:** Mapeou e otimizou ecossistemas de dados bancários e farmacêuticos suportando +85 farmácias, integrações laboratoriais e mais de 70M€ em volume transacional anual, garantindo compliance e reconciliação financeira.
        * **Tradução de Requisitos & Refactoring:** Auditou lógica de negócio legada e estrangulamentos operacionais, traduzindo necessidades em especificações funcionais e técnicas. Liderou a reconstrução arquitetural (+5.000 linhas de SQL refatoradas e redução de 50% nas tabelas) e preparou o roadmap para Microsoft Fabric.
        * **Impacto Operacional e Financeiro:** Reduziu o processamento ETL crítico de 24 horas para 15 minutos e cortou o esforço de manutenção arquitetural em 75% (de ~1.600h para ~400h/ano), assegurando um contrato de >100k€/ano e devolvendo fiabilidade ao CFO.
        * **Entrega Cross-Functional (McKinsey):** Atuou como ponte entre consultores da McKinsey e equipas de engenharia para clarificar requisitos, desbloquear dependências e entregar modelos analíticos em Apache Superset em semanas para expansão B2B em telecomunicações.
        """)
        render_pills(["Advanced SQL", "PostgreSQL", "Microsoft Fabric", "Azure Data Factory", "Power BI", "Apache Superset", "PySpark", "Erwin Data Modeler", "Agile/Scrum"])

        st.markdown("""
        <div class="role-header">
            <div><span class="role-company">IKEA</span> &nbsp;|&nbsp; <span class="role-title">Customer Insights Lead & Business Data Architect</span></div>
            <div class="role-date">2014 – 2022 | Lisboa, PT</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        * **User Insights & Product Analytics:** Liderou o desenho de KPIs de Voice of Customer (VoC) que informaram a framework Global de Performance. Analisou feedback e comportamento do utilizador (via NLP/Brandwatch e telemetria web) para identificar pontos de fricção e estruturar a Knowledge Base da operação.
        * **Integração de Sistemas & SSOT:** Eliminou silos departamentais ("Excel Hell") integrando telemetria de contact center (Avaya, Genesys) com sistemas ERP/faturação (SAP, OCP) em Data Marts centralizados em Power BI utilizados diariamente por 400+ colaboradores.
        * **Otimização de Workflows & Suporte Operacional:** Definiu workflows funcionais, ferramentas de monitorização e requisitos que permitiram às equipas operacionais e comerciais reduzir erros de vendas de 30% para <7%, cortar custos logísticos em 20–30% e elevar o SLA Omnichannel de <9% para >90%.
        * **Change Management & Alinhamento Executivo:** Manteve documentação funcional, liderou o onboarding de utilizadores e apoiou a direção executiva com análises Cost-to-Serve e root-cause analysis (incluindo modelação SEM) ligando qualidade operacional às margens do P&L.
        """)
        render_pills(["Power BI", "SQL", "SAP", "OCP", "Genesys", "Avaya", "Brandwatch (NLP)", "Data Marts (SSOT)", "Process Mapping"])

        st.markdown("""
        <div class="role-header">
            <div><span class="role-company">Banco BPI & Central de Cervejas</span> &nbsp;|&nbsp; <span class="role-title">Sales & CX Operations Analyst</span></div>
            <div class="role-date">Até 2014 | Portugal</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        * **Fundação Bancária e Comercial:** Gestão de carteiras B2B e atendimento bancário na linha da frente no Banco BPI, consolidando domínio sobre produtos financeiros, fluxos comerciais/crédito e tradução de dores do utilizador em requisitos de reporting.
        """)
        render_pills(["Operações Bancárias", "Fluxos de Crédito", "Gestão B2B", "CRM", "Reporting Operacional"])

# ==============================================================================
# TAB 3: CLOUD & SAAS PROJECTS (MVPs)
# ==============================================================================
elif menu in ["Cloud & SaaS Projects", "Projetos Cloud & SaaS"]:
    if lang == "EN":
        st.markdown("""
        <div class="role-header">
            <div><span class="role-company">Independent Product & Data Consultant</span> &nbsp;|&nbsp; <span class="role-title">Technical BA & Solutions Architect (SaaS MVPs)</span></div>
            <div class="role-date">2025 – Present | Lisbon, PT</div>
        </div>
        """, unsafe_allow_html=True)
        st.write(
            "End-to-end product specification and cloud architecture across four functional MVPs, "
            "translating operational bottlenecks into User Stories, Acceptance Criteria, serverless microservices, and automated data pipelines."
        )

        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.markdown("#### Polanyi Lakehouse — Medallion Architecture & CI/CD")
            st.markdown("""
            * **Architecture:** Physical Data Lakehouse in Google BigQuery (Bronze, Silver, Gold layers) centralizing socioeconomic datasets (Eurostat/World Bank) processed via Python.
            * **CI/CD & FinOps:** Automated deployment pipelines via Google Cloud Build triggered by GitHub webhooks, incorporating Data Quality tests and compute cost auditing.
            * **Quantitative Modeling:** SQL Z-score normalization and official NUTS geographic polygon integration for GIS rendering in Looker Studio.
            """)
            render_pills(["BigQuery", "Python", "Cloud Build", "GitHub CI/CD", "Looker Studio", "GIS"])

            st.markdown("#### TripMillennium — React & Offline-First Logistics")
            st.markdown("""
            * **Product Requirement:** Field logistics users required uninterrupted data access in low-connectivity areas without hitting API quota bottlenecks.
            * **Frontend & Edge Caching:** Modular web application built in React.js, TypeScript, and Tailwind CSS, consuming relational data via Google Edge Network with local browser parsing (PapaParse) for offline-first resilience.
            * **Asynchronous Storage:** Webhook microservices decoding base64 payloads into Object Storage with automated relational URL injection.
            """)
            render_pills(["React.js", "TypeScript", "Tailwind CSS", "REST APIs", "Webhooks", "Offline-First"])

        with col_p2:
            st.markdown("#### Inventory & Nutrition — Hybrid AI & Data Governance")
            st.markdown("""
            * **Product Requirement:** Replace fragile exact-match spreadsheet lookups with automated semantic reconciliation while preventing database corruption.
            * **Serverless & NLP:** Microservices on GCP Cloud Run combining multimodal OCR (Gemini 1.5 Flash) and Vector Embeddings (`gemini-embedding-001`) with Cosine Similarity calculations.
            * **Trust Funnel Governance:** Multi-stage validation workflow where the LLM acts as a binary arbiter for intermediate confidence thresholds (65%–82%) before committing records.
            """)
            render_pills(["GCP Cloud Run", "Vertex AI", "Gemini 1.5", "Vector Embeddings", "Cosine Similarity"])

            st.markdown("#### Poke-Prices — Analytical Modeling & Tactical RAG")
            st.markdown("""
            * **Data Modeling:** Galaxy Schema architecture in BigQuery enforcing idempotency and deduplication through analytical window functions (`ROW_NUMBER`).
            * **Applied RAG:** Retrieval-Augmented Generation engine intersecting qualitative market reports with quantitative pricing time-series via Gemini 1.5 Flash.
            """)
            render_pills(["BigQuery", "Galaxy Schema", "Window Functions", "RAG", "Gemini API"])

    else:
        st.markdown("""
        <div class="role-header">
            <div><span class="role-company">Independent Product & Data Consultant</span> &nbsp;|&nbsp; <span class="role-title">Technical BA & Solutions Architect (SaaS MVPs)</span></div>
            <div class="role-date">2025 – Presente | Lisboa, PT</div>
        </div>
        """, unsafe_allow_html=True)
        st.write(
            "Especificação de produto end-to-end e arquitetura cloud em quatro MVPs funcionais, "
            "traduzindo estrangulamentos operacionais em User Stories, Critérios de Aceitação, microsserviços serverless e pipelines automatizados."
        )

        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.markdown("#### Polanyi Lakehouse — Arquitetura Medallion & CI/CD")
            st.markdown("""
            * **Arquitetura:** Data Lakehouse físico no Google BigQuery (camadas Bronze, Silver, Gold) para centralização de dados socioeconómicos (Eurostat/Banco Mundial) processados em Python.
            * **CI/CD & FinOps:** Pipelines automatizados via Google Cloud Build ativados por webhooks do GitHub, com testes de Data Quality e auditoria de custos de computação.
            * **Modelação Quantitativa:** Normalização via Z-scores em SQL e integração de polígonos geográficos oficiais (NUTS) para visualização GIS no Looker Studio.
            """)
            render_pills(["BigQuery", "Python", "Cloud Build", "GitHub CI/CD", "Looker Studio", "GIS"])

            st.markdown("#### TripMillennium — Logística React & Offline-First")
            st.markdown("""
            * **Requisito de Produto:** Equipas no terreno necessitavam de acesso contínuo a dados em zonas sem rede sem esgotar quotas de API.
            * **Frontend & Edge Caching:** Aplicação modular em React.js, TypeScript e Tailwind CSS, consumindo dados via Google Edge Network com processamento local no browser (PapaParse) para resiliência offline-first.
            * **Storage Assíncrono:** Microsserviços via webhooks para descodificar payloads base64 em Object Storage com injeção automática de URLs na base de dados.
            """)
            render_pills(["React.js", "TypeScript", "Tailwind CSS", "REST APIs", "Webhooks", "Offline-First"])

        with col_p2:
            st.markdown("#### Inventário & Nutrição — IA Híbrida & Governança")
            st.markdown("""
            * **Requisito de Produto:** Substituir procuras exatas frágeis por reconciliação semântica automatizada sem comprometer a integridade relacional do stock.
            * **Serverless & NLP:** Microsserviços em GCP Cloud Run combinando OCR multimodal (Gemini 1.5 Flash) e Vector Embeddings (`gemini-embedding-001`) com Similaridade de Cosseno.
            * **Funil de Confiança:** Workflow de validação onde o LLM atua como árbitro binário em limiares intermédios (65%–82%) antes da consolidação na base de dados.
            """)
            render_pills(["GCP Cloud Run", "Vertex AI", "Gemini 1.5", "Vector Embeddings", "Cosine Similarity"])

            st.markdown("#### Poke-Prices — Modelação Analítica & RAG Tático")
            st.markdown("""
            * **Modelação de Dados:** Arquitetura Galaxy Schema no BigQuery garantindo idempotência e desduplicação via funções de janela analítica (`ROW_NUMBER`).
            * **RAG Aplicado:** Motor de Retrieval-Augmented Generation que cruza relatórios qualitativos com séries temporais quantitativas através do Gemini 1.5 Flash.
            """)
            render_pills(["BigQuery", "Galaxy Schema", "Window Functions", "RAG", "Gemini API"])

# ==============================================================================
# TAB 4: TECHNICAL STACK & EDUCATION
# ==============================================================================
elif menu in ["Technical Stack", "Stack Tecnológico"]:
    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        if lang == "EN":
            st.markdown("#### Core Competencies & Technical Stack")
            st.markdown("**1. Business Analysis & Product Delivery**")
            render_pills([
                "Requirements Gathering", "User Stories", "Acceptance Criteria",
                "As-Is / To-Be Process Mapping", "Functional Specifications",
                "Backlog Refinement", "UAT & Data Reconciliation", "Agile / Scrum",
                "Confluence", "Jira / Azure DevOps"
            ])

            st.markdown("**2. Data Architecture & Enterprise Analytics**")
            render_pills([
                "Advanced SQL (PostgreSQL, T-SQL, KQL)", "Google BigQuery",
                "Microsoft Fabric", "Azure Data Factory", "Power BI", "Apache Superset",
                "Looker Studio", "Data Marts (SSOT)", "Medallion Architecture",
                "Erwin Data Modeler", "PySpark", "Voice of Customer (VoC) KPIs"
            ])

            st.markdown("**3. Cloud, APIs, Enterprise Systems & AI**")
            render_pills([
                "REST APIs", "Webhooks", "GCP Cloud Run", "Cloud Build (CI/CD)",
                "SAP (Data Extraction)", "Genesys / Avaya", "Salesforce / CRM",
                "Vertex AI / Gemini", "RAG Pipelines", "Vector Embeddings",
                "Brandwatch (NLP)", "React.js", "TypeScript", "Git"
            ])
        else:
            st.markdown("#### Competências Centrais & Stack Tecnológico")
            st.markdown("**1. Business Analysis & Entrega de Produto**")
            render_pills([
                "Levantamento de Requisitos", "User Stories", "Critérios de Aceitação",
                "Mapeamento As-Is / To-Be", "Especificações Funcionais",
                "Backlog Refinement", "UAT & Reconciliação de Dados", "Agile / Scrum",
                "Confluence", "Jira / Azure DevOps"
            ])

            st.markdown("**2. Arquitetura de Dados & Enterprise Analytics**")
            render_pills([
                "Advanced SQL (PostgreSQL, T-SQL, KQL)", "Google BigQuery",
                "Microsoft Fabric", "Azure Data Factory", "Power BI", "Apache Superset",
                "Looker Studio", "Data Marts (SSOT)", "Medallion Architecture",
                "Erwin Data Modeler", "PySpark", "KPIs Voice of Customer (VoC)"
            ])

            st.markdown("**3. Cloud, APIs, Sistemas Empresariais & IA**")
            render_pills([
                "REST APIs", "Webhooks", "GCP Cloud Run", "Cloud Build (CI/CD)",
                "SAP (Extração)", "Genesys / Avaya", "Salesforce / CRM",
                "Vertex AI / Gemini", "Pipelines RAG", "Vector Embeddings",
                "Brandwatch (NLP)", "React.js", "TypeScript", "Git"
            ])

    with col_right:
        st.markdown("#### Domain Distribution")
        categories = [
            'SQL & Data Modeling (SSOT)',
            'Business Analysis & Requirements',
            'BI & Executive Reporting',
            'Cloud & APIs (GCP/Azure)',
            'Applied AI & NLP (RAG)',
            'Frontend (React/TS)'
        ]
        fig = go.Figure(go.Scatterpolar(
            r=[5.0, 4.8, 5.0, 4.5, 4.5, 4.0],
            theta=categories,
            fill='toself',
            fillcolor='rgba(2, 132, 199, 0.15)',
            line=dict(color='#0f172a', width=2)
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 5], tickfont=dict(size=10, color='#64748b')),
                angularaxis=dict(tickfont=dict(size=11, color='#0f172a'))
            ),
            showlegend=False,
            margin=dict(t=30, b=30, l=40, r=40),
            height=320,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("#### Academic Background")
        if lang == "EN":
            st.markdown("""
            * **Post-Graduate Degree in Digital Enterprise Management** — *Nova IMS*
            * **MSc in Management (Thesis Grade: 18/20)** — *ISEG, University of Lisbon*
            * **BSc in Political Science** — *ISCSP, University of Lisbon*
            """)
        else:
            st.markdown("""
            * **Pós-Graduação em Digital Enterprise Management** — *Nova IMS*
            * **Mestrado em Gestão (Tese: 18/20)** — *ISEG, Universidade de Lisboa*
            * **Licenciatura em Ciência Política** — *ISCSP, Universidade de Lisboa*
            """)

# ==============================================================================
# TAB 5: OPERATIONAL STYLE & METHODOLOGY
# ==============================================================================
elif menu in ["Operational Style", "Estilo Operacional"]:
    if lang == "EN":
        st.markdown("#### Operational Methodology & Team Dynamics")
        st.write(
            "How I approach ambiguous problems, structure requirements across teams, and ensure technical delivery aligns with business reality."
        )
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="info-card">
                <div class="info-card-title">1. Strategic Anchoring & Discovery</div>
                <div class="info-card-body">
                Every initiative starts with rigorous As-Is mapping and structured stakeholder questioning. 
                Before writing a single line of SQL or defining a feature, I validate data provenance, edge cases, 
                and the exact operational metric the solution must move.
                </div>
            </div>
            <div class="info-card">
                <div class="info-card-title">2. Systemic Vision (360º Architecture)</div>
                <div class="info-card-body">
                I do not treat tickets in isolation. Whether integrating SAP billing with Genesys telemetry or refactoring 
                ETL pipelines, I map upstream dependencies and downstream reporting impacts to build genuine Single Sources of Truth.
                </div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="info-card">
                <div class="info-card-title">3. Cross-Functional Translation</div>
                <div class="info-card-body">
                Fluency in both executive P&L discussions and engineering codebases eliminates translation friction. 
                I write functional documentation and acceptance criteria that engineers trust and business stakeholders clearly understand.
                </div>
            </div>
            <div class="info-card">
                <div class="info-card-title">4. Ownership & Change Management</div>
                <div class="info-card-body">
                A data product or SaaS feature only succeeds when adopted. I pair technical delivery with clear documentation, 
                feature walkthroughs, and frontline training to ensure teams transition smoothly away from legacy workflows.
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("#### Metodologia Operacional & Dinâmica de Equipa")
        st.write(
            "Como abordo problemas complexos, estruturo requisitos entre equipas e garanto que a execução técnica responde à realidade do negócio."
        )
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="info-card">
                <div class="info-card-title">1. Ancoragem Estratégica & Discovery</div>
                <div class="info-card-body">
                Cada iniciativa começa com um mapeamento rigoroso As-Is e questionamento estruturado aos stakeholders. 
                Antes de escrever SQL ou especificar uma funcionalidade, valido a proveniência dos dados, os edge cases 
                e a métrica operacional exata que a solução tem de mover.
                </div>
            </div>
            <div class="info-card">
                <div class="info-card-title">2. Visão Sistémica (Arquitetura 360º)</div>
                <div class="info-card-body">
                Não trato pedidos de forma isolada. Seja a integrar faturação SAP com telemetria Genesys ou a refatorar 
                pipelines de ETL, mapeio as dependências a montante e o impacto a jusante para construir verdadeiras Single Sources of Truth.
                </div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="info-card">
                <div class="info-card-title">3. Tradução Cross-Functional</div>
                <div class="info-card-body">
                A fluência tanto em discussões executivas de P&L como em bases de código elimina o atrito entre equipas. 
                Produzo documentação funcional e critérios de aceitação em que a engenharia confia e que o negócio compreende.
                </div>
            </div>
            <div class="info-card">
                <div class="info-card-title">4. Ownership & Change Management</div>
                <div class="info-card-body">
                Um produto de dados ou funcionalidade SaaS só tem sucesso quando é adotado. Acompanho a entrega técnica com 
                documentação clara, demos e formação às equipas para garantir a transição efetiva de processos legados.
                </div>
            </div>
            """, unsafe_allow_html=True)