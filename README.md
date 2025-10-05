# 🏦 Bankalysis

**Bankalysis** is a local-first personal finance analytics toolkit that transforms your **bank transaction CSV exports** into a rich **RDF knowledge graph**. It combines **semantic web technology**, **data science**, and **privacy-first design** to help you explore and understand your finances — all running locally in Docker containers.

---

## ✨ Features

- 🧹 **CSV Preprocessing** — Clean, normalize, and enrich your transaction exports  
- 🏷️ **Categorization Engine** — Automatically classify expenses (groceries, food, petrol, etc.)  
- 🌐 **RDF Generation (RML)** — Convert processed CSVs into RDF triples using RML mappings  
- 🗃️ **Local Triple Store** — Store and query your data with GraphDB or Apache Jena Fuseki  
- 📊 **Analytics Dashboard** — Interactive UI powered by SPARQL and visualized with Plotly  
- 🔒 **Local-First Privacy** — 100% offline; no external API calls or cloud dependencies  

---

## 🧩 Architecture Overview

1. Bank CSV Export
2. Processing
  1. Preprocessing
  2. Categorization
  3. RML Transformation
3. RDF Triple Store
4. UI + Analytics Dashboard
5. Local Storage & Configs


---

## 🛠️ Tech Stack (work in progress)

| Layer | Technology | Purpose |
|-------|-------------|----------|
| Data Preprocessing | Python + pandas | Clean and normalize CSV exports |
| Categorization | Python + rule-based / ML | Map transactions to categories |
| RDF Transformation | [RMLMapper](https://github.com/RMLio/rmlmapper-java) | Convert CSV → RDF triples |
| Storage | GraphDB / Apache Jena Fuseki | SPARQL endpoint and triple store |
| Backend API | FastAPI / Flask | Serve analytics and query results |
| Frontend | React + Plotly / Recharts | Visualize spending trends |
| Orchestration | Docker Compose | Local, reproducible setup |

---

## 🚀 Quick Start (work in progress)

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/bankalysis.git
cd bankalysis
```

2. Add your bank CSV exports

Place your CSV files in the data/input/ directory.
(Example: `data/input/transactions_2025.csv`)

3. Configure environment variables

Edit .env to define:
```
BANKALYSIS_TRIPLESTORE=fuseki
BANKALYSIS_PORT=8080
```

4. Start all containers
`docker-compose up --build`


5. Open the UI
Visit: http://localhost:8080

---

🧠 Example Workflow
1. Export transactions from your online banking as CSV
2. Run preprocessing + categorization pipeline
3. Transform to RDF using RML mapping rules (config/mapping.rml.ttl)
4. Load triples into the local store (Fuseki/GraphDB)
5. Query via SPARQL or explore visually in the dashboard
