Here you will find an end-to-end showcase of production-ready machine learning pipelines, local vector databases, cloud-native API development, and automated CI/CD infrastructures.

---

## 🚀 Projects Showcase

### 1. Automated CI/CD Test Suite for RAG Systems
**Stack:** GitHub Actions, Python, FastAPI, Pytest, Docker, Mock Testing
*Automated quality assurance pipeline that guarantees the semantic integrity of LLM knowledge bases before deployment.*

* **The Problem:** RAG (Retrieval-Augmented Generation) applications are inherently non-deterministic, making them difficult to test in standard automated environments.
* **The Solution:** Built a GitHub Actions workflow that automatically spins up a test FastAPI container, parses updated text sources, updates a ChromaDB vector database, and executes semantic assertion tests.
* **Key Achievement:** Implemented a customizable **Mock LLM Mode** that bypasses live LLM pricing and response variations during build testing, providing 100% deterministic test passes.

📂 **Repo Link:** [Automate Testing with GitHub Actions](https://github.com/yourusername/nextwork-rag-api)

---

### 2. Local Private RAG API
**Stack:** FastAPI, ChromaDB, Ollama (TinyLlama), Python, PowerShell
*An enterprise-grade, completely private Retrieval-Augmented Generation API running locally on Windows to guarantee absolute data privacy.*

* **Architecture:** Users submit natural language queries to a FastAPI backend. The API extracts vector embeddings using ChromaDB, retrieves context-specific documentation, and builds prompts for Ollama.
* **Security & Optimization:** Zero-cloud dependency ensures internal business documents never leave the host machine. Engineered Windows-specific process lifecycles to manage SQLite and data locks cleanly under load.
* **Endpoint:** Exposes a secure POST `/query` endpoint returning structured semantic answers.

📂 **Repo Link:** [Local Private RAG API](https://github.com/yourusername/nextwork-rag-api)

---

### 3. FoodLens AI-Powered Application
**Stack:** Streamlit, Python, Computer Vision, Secret Management, GitHub
*A high-speed, interactive web application designed to analyze food images and parse nutritional details securely in the cloud.*

* **Engineering Highlights:** Deployed natively to Streamlit Community Cloud. Designed a secure "Safe Key Masking" utility that outputs key rotations and masking structures in execution logs without exposing raw credentials.
* **Production Standards:** Avoided path dependencies by structuring relative dynamic path files, ensuring seamless performance translation from local Windows developer environments to remote Unix container builds.

📂 **Repo Link:** [FoodLens App](https://github.com/yourusername/foodlens)

---

### 4. Enterprise Churn Prediction Pipeline
**Stack:** Python, Scikit-Learn, MLflow, Pandas, Matplotlib
*An end-to-end machine learning pipeline built to identify customer attrition risks and optimize corporate retention strategies.*

* **Model Engineering:** Evaluated Logistic Regression vs. Gradient Boosting models under Occam's Razor, selecting the most interpretable and computationally lightweight architecture.
* **Experiment Tracking:** Utilized MLflow to log metrics, capture hyperparameters, and manage baseline models systematically.
* **Business Analytics:** Translated predictions into corporate strategies using a custom 2x2 Decision Matrix mapping Customer Churn Risk against Lifetime Value.

📂 **Repo Link:** [Customer Churn Pipeline](https://github.com/yourusername/churn-prediction)

---

## 🛠️ Technical Toolkit

* **AI & RAG:** Prompt Engineering, Retrieval-Augmented Generation, Vector Embeddings, ChromaDB, Ollama
* **Machine Learning:** Scikit-Learn, Pandas, MLflow Experiment Tracking, Predictive Modeling
* **Backend & Web:** FastAPI, Streamlit, RESTful APIs, Python, JSON-Serialization
* **DevOps & Cloud:** GitHub Actions (CI/CD workflows), PowerShell scripting, Windows local environment configurations, Git repo hygiene (.gitignore optimization)

---
*Connect with me on [LinkedIn](https://linkedin.com/in/yourprofile) or explore my codebases above!*
