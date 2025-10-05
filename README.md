# 🏦 Bankalysis

**Bankalysis** is a local-first personal finance analytics toolkit that transforms your **bank transaction CSV exports** into a rich **RDF knowledge graph**.  
It combines **semantic web technology**, **data science**, and **privacy-first design** to help you explore and understand your finances — all running locally in Docker containers.

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

1. **Bank CSV Export (from online banking)**:
   - Data is exported from online banking in CSV format.

2. **Preprocessing** (Python Container):
   - The raw CSV data is preprocessed using Python libraries such as pandas and scikit-learn.
   - This step includes cleaning and preparing the data for further processing.

3. **Categorization** (Python Container):
   - A custom Python model and rules are applied to categorize the transactions in the CSV data.

4. **RML Transformation** (RMLMapper Container):
   - The categorized data is transformed into RDF triples using RML (RDF Mapping Language).
   - The transformation process is handled by the RMLMapper container.

5. **RDF Triple Store** (Docker):
   - The RDF triples are stored in a GraphDB or Apache Jena Fuseki instance running in a Docker container.
   - This serves as the central storage for all processed data.

6. **UI + Analytics Dashboard**:
   - A user interface is built using React, with a backend powered by Flask or FastAPI.
   - The dashboard allows users to run SPARQL queries to extract stats and insights from the RDF data.
   - Visualizations are generated using libraries such as Plotly or D3.js.

7. **Local Storage & Configs** (Docker Volumes):
   - All local storage and configurations are managed within Docker volumes.
   - No cloud infrastructure is used for storage, ensuring all data remains local.


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
