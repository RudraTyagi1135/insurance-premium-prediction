# 💰 Insurance Premium Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![Prediction](https://img.shields.io/badge/Prediction-Risk_Analytics-purple?style=for-the-badge)
![MLOps](https://img.shields.io/badge/MLOps-Deployment-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

</p>

---

# 🌐 Live Application

🚀 **Streamlit Deployment:**  
https://insurance-premium-predictor-1135.streamlit.app/

---

# 📌 Project Overview

The **Insurance Premium Prediction System** is a deployment-ready machine learning application that estimates insurance premium risk categories using customer demographic and lifestyle information.

The application performs:
- feature engineering
- risk scoring
- premium category prediction
- probability estimation
- prediction logging

through an interactive Streamlit dashboard.

Built using:

- Streamlit
- Pandas
- Pydantic
- YAML configuration
- scikit-learn-compatible inference pipeline

---

# 🎯 What This Application Actually Does

The application collects:

- age
- height
- weight
- annual income
- smoking status
- city
- occupation

and transforms them into model-ready engineered features.

The inference pipeline then predicts:

| Output | Meaning |
|---|---|
| Low | Lower estimated insurance premium risk |
| Medium | Moderate estimated premium risk |
| High | Higher estimated premium risk |

The system also generates:
- confidence score
- class probabilities
- structured prediction logs

---

# 🧠 Prediction Workflow

```text
User Input
        ↓
Pydantic Validation
        ↓
Feature Engineering
        ↓
Model Inference
        ↓
Probability Estimation
        ↓
Prediction Logging
        ↓
Streamlit Dashboard Output
```

---

# 📊 How The Prediction Logic Works

The current deployment uses a transparent rule-based demo model.

The model evaluates factors such as:

- age group
- BMI
- smoking behavior
- city tier
- annual income
- occupation category

and generates a premium-risk score.

Higher-risk combinations increase the likelihood of:

```text
High Premium Category
```

---

# 📌 Example Interpretation

### Example 1

Input:
- smoker
- high BMI
- high-income individual
- tier-1 city

Likely Result:

```text
High Premium Category
```

Reason:
- elevated lifestyle and financial risk indicators

---

### Example 2

Input:
- younger age
- healthy BMI
- non-smoker
- lower-risk city tier

Likely Result:

```text
Low Premium Category
```

Reason:
- lower estimated health and lifestyle risk

---

# 🏗️ System Architecture

```text
User Input
        ↓
Validation Layer (Pydantic)
        ↓
Feature Engineering Pipeline
        ↓
Serialized ML Model
        ↓
Prediction & Probability Engine
        ↓
Prediction Logging System
        ↓
Streamlit Interactive Dashboard
```

---

# ⚙️ Architecture Breakdown

## 🖥️ Streamlit UI Layer

Responsible for:
- user interaction
- input collection
- prediction rendering
- probability visualization

---

## 🧹 Validation Layer

Implemented using:

- Pydantic

Responsibilities:
- schema validation
- input sanitization
- feature consistency

---

## ⚙️ Feature Engineering Layer

Transforms raw user input into:

```text
bmi
age_group
lifestyle_risk
city_tier
income_lpa
occupation
```

These features are consumed by the inference model.

---

## 🤖 Inference Layer

Loads:

```text
model/model.pkl
```

Supports:
- predict()
- predict_proba()
- classes_

interfaces.

---

## 📝 Prediction Logging Layer

Logs:
- request ID
- timestamps
- model version
- engineered features
- prediction outputs

in JSONL format.

---

# ✨ Core Features

## 📊 Premium Risk Prediction

Predicts:
- Low premium category
- Medium premium category
- High premium category

---

## 🧠 Feature Engineering Pipeline

Automatically derives:
- BMI
- lifestyle risk
- age groups
- city tiers

from raw user inputs.

---

## 📈 Probability Estimation

Displays:
- class probabilities
- confidence scores
- prediction certainty

---

## 📝 Structured Prediction Logging

Every inference request is logged with:
- metadata
- engineered features
- model version
- output prediction

---

## ⚡ Deployment-Ready Architecture

The application is fully deployable using:
- Streamlit Cloud
- bundled model artifacts
- YAML configuration

without requiring external APIs or backend services.

---

# 📂 Project Structure

```text
insurance-premium-prediction/
│
├── streamlit_app.py
├── requirements.txt
├── config.yaml
│
├── config/
│   ├── city_tier.py
│   └── settings.py
│
├── model/
│   ├── demo_model.py
│   ├── model.pkl
│   └── prediction.py
│
└── schema/
    └── user_input.py
```

---

# 📊 Feature Engineering

| Raw Input | Engineered Feature |
|---|---|
| Weight + Height | BMI |
| Age | Age Group |
| Smoking + BMI | Lifestyle Risk |
| City | City Tier |
| Income | Income LPA |
| Occupation | Occupation Category |

---

# 🧠 Current Model Note

The deployed model is currently:

```text
DemoInsuranceModel
```

The bundled model is:
- deterministic
- rule-based
- fully transparent

This allows:
- deployment testing
- UI validation
- feature engineering verification
- inference workflow demonstration

without requiring proprietary insurance datasets.

---

# ⚠️ Important Disclaimer

This project is intended for:
- educational purposes
- ML system demonstration
- deployment workflows
- inference architecture learning

It should NOT be treated as:
- actuarial advice
- medical advice
- real insurance underwriting

---

# ⚙️ Configuration

Runtime settings are managed through:

```text
config.yaml
```

Example:

```yaml
model:
  path: model/model.pkl
  version: 1.0.0

prediction_logging:
  enabled: true
  path: logs/predictions.jsonl
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive dashboard |
| Pandas | Data processing |
| Pydantic | Input validation |
| YAML | Configuration management |
| Pickle | Model serialization |

---

# ⚙️ Local Setup & Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/insurance-premium-prediction.git
cd insurance-premium-prediction
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
streamlit run streamlit_app.py
```

---

# 🌐 Deployment

The application is deployed using:

- Streamlit Cloud

Deployment link:

:contentReference[oaicite:1]{index=1}

---

# 📊 Engineering Highlights

- End-to-end inference workflow
- Structured feature engineering pipeline
- Pydantic validation architecture
- Model serialization workflow
- Probability estimation pipeline
- Prediction logging system
- YAML-driven configuration management
- Deployment-ready Streamlit application
- Modular ML inference architecture

---

# 📈 Potential Future Improvements

Planned enhancements include:

- Real trained ML model integration
- SHAP explainability support
- FastAPI inference service
- Docker deployment
- AWS cloud deployment
- ML experiment tracking
- Model monitoring
- User authentication
- Database-backed prediction storage
- CI/CD integration

---

# 🎯 What This Project Demonstrates

This project demonstrates practical understanding of:

- ML inference systems
- Deployment-ready ML architecture
- Feature engineering workflows
- Model serialization pipelines
- Probability estimation systems
- Structured prediction logging
- Streamlit deployment workflows
- Modular ML application design

---

# 📌 Strategic Engineering Value

This project demonstrates significantly more engineering depth than notebook-only ML projects because it includes:

- deployable inference architecture
- feature engineering pipelines
- configuration-driven workflows
- modular project organization
- structured prediction logging
- production-oriented ML deployment design

---

# 📸 Recommended Screenshot Section

Add screenshots here for stronger recruiter impact:

```markdown
![Prediction Dashboard](your-image-link)
![Probability Output](your-image-link)
![Feature Engineering Flow](your-image-link)
```

---

# 👨‍💻 Author

## Rudra Tyagi

### Focus Areas

- ML Systems
- MLOps
- AI Infrastructure
- Applied Machine Learning
- Production ML Engineering

---

# ⭐ Recruiter Notes

This repository demonstrates:

- ML inference engineering
- Deployment-ready ML systems
- Modular ML architecture
- Feature engineering pipelines
- Prediction logging systems
- Production-style ML deployment workflows

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
