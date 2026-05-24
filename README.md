# Insurance Premium Prediction

A FastAPI-based machine learning service that predicts an insurance premium category from customer profile data. The project includes a REST API, Pydantic request validation, a prediction layer around a serialized scikit-learn-compatible model, Docker support, and a Streamlit frontend for local demos.

## Features

- Predicts insurance premium category from age, BMI, income, smoking status, city tier, and occupation.
- Validates API input with Pydantic models.
- Computes derived features automatically:
  - BMI from height and weight
  - age group from age
  - lifestyle risk from smoking status and BMI
  - city tier from configured city lists
- Returns predicted class, confidence score, and class probability distribution.
- Provides FastAPI health check endpoint with model version.
- Includes Dockerfile for containerized deployment.
- Includes Streamlit frontend for manual testing.

## Project Structure

```text
insurance_premium_prediction/
|-- app.py                         # FastAPI application and API routes
|-- Dockerfile                     # Container build definition
|-- requirements.txt               # Python dependencies
|-- config/
|   `-- city_tier.py               # City tier configuration
|-- frontend/
|   `-- frontend.py                # Streamlit frontend
|-- model/
|   |-- fastapi_ml_model.ipynb     # Model development notebook
|   `-- prediction.py              # Model loading and prediction logic
`-- schema/
    |-- prediction_response.py     # API response schema
    `-- user_input.py              # API request schema and feature engineering
```

## Tech Stack

- **API:** FastAPI, Uvicorn
- **Validation:** Pydantic v2
- **ML/Data:** scikit-learn, pandas, numpy
- **Frontend:** Streamlit
- **Packaging:** Docker
- **Cloud target:** AWS-ready container deployment

## Runtime Requirements

- Python 3.11+
- A trained model artifact at:

```text
model/model.pkl
```

The model artifact is intentionally ignored by Git through `.gitignore` because serialized ML models can be large and environment-specific. Before running the API, place the trained `model.pkl` file inside the `model/` directory.

The loaded model must support:

- `predict(input_dataframe)`
- `predict_proba(input_dataframe)`
- `classes_`

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Home

```http
GET /
```

Example response:

```json
{
  "Message": "INSURANCE PREMIUM PREDICTION MODEL"
}
```

### Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "OK",
  "model_version": "1.0.0"
}
```

### Predict Premium Category

```http
POST /predict
```

Request body:

```json
{
  "age": 30,
  "weight": 65.0,
  "height": 1.7,
  "income_lpa": 10.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

Allowed occupation values:

```text
retired
freelancer
student
government_job
business_owner
unemployed
private_job
```

The prediction function produces this structured payload:

```json
{
  "predicted_category": "Low",
  "confidence": 0.8732,
  "class_probabilities": {
    "Low": 0.8732,
    "Medium": 0.1021,
    "High": 0.0247
  }
}
```

Note: the current `/predict` route wraps this payload in a string response. For production API clients, return the prediction dictionary directly so the response matches `PredictionResponse`.

Example cURL:

```bash
curl -X POST "http://127.0.0.1:8000/predict" ^
  -H "Content-Type: application/json" ^
  -d "{\"age\":30,\"weight\":65.0,\"height\":1.7,\"income_lpa\":10.0,\"smoker\":false,\"city\":\"Mumbai\",\"occupation\":\"private_job\"}"
```

## Running the Streamlit App

For local or Streamlit Community Cloud deployment, run the Streamlit entrypoint:

```bash
streamlit run streamlit_app.py
```

The Streamlit app runs inference directly through `model/prediction.py`; it does not require a separate FastAPI server or a localhost API URL.

Before deploying, make sure the trained model artifact exists at the configured path:

```text
model/model.pkl
```

This path is controlled by `config.yaml`:

```yaml
model:
  path: model/model.pkl
  version: 1.0.0
```

The repository now allows `model/model.pkl` and `config.yaml` to be committed. If the model file is too large for normal Git hosting, use Git LFS or add a startup step that downloads the artifact from S3 before Streamlit starts.

## Docker Usage

Build the image:

```bash
docker build -t insurance-premium-prediction .
```

Run the container:

```bash
docker run -p 8000:8000 insurance-premium-prediction
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Model Input Features

The API accepts raw customer inputs and derives the model-ready fields internally.

| Raw input | Derived / used feature |
| --- | --- |
| `weight`, `height` | `bmi` |
| `age` | `age_group` |
| `smoker`, `bmi` | `lifestyle_risk` |
| `city` | `city_tier` |
| `income_lpa` | `income_lpa` |
| `occupation` | `occupation` |

The prediction layer sends this feature set to the model:

```text
bmi
age_group
lifestyle_risk
city_tier
income_lpa
occupation
```

## AWS Deployment Notes

The application is container-ready and can be deployed to AWS using services such as:

- Amazon ECS or EKS for the FastAPI container
- AWS Lambda with a container image for lightweight inference workloads
- Amazon SageMaker endpoint if model hosting should be separated from the API
- Amazon S3 for storing versioned model artifacts
- Amazon CloudWatch for API and prediction logs

For production, avoid baking frequently changing model files directly into the image unless releases are tightly versioned. A scalable AWS pattern is:

1. Store trained model artifacts in S3.
2. Load the selected model version during service startup.
3. Emit structured prediction logs to CloudWatch or a durable analytics store.
4. Track model version, request ID, prediction, confidence, and timestamp for each inference.

## Production Checklist

- Move environment-specific values into `config.yaml` or environment variables.
- Replace hardcoded local paths and URLs with configuration.
- Add structured logging for every prediction request and response.
- Add request IDs for traceability.
- Add unit tests for schemas, feature engineering, and prediction response formatting.
- Add integration tests for `/health` and `/predict`.
- Add model artifact versioning.
- Add CI checks for linting, tests, and Docker build.
- Add authentication or network-level protection before exposing the API publicly.

## Known Implementation Notes

- `model/model.pkl` is required at runtime but is not committed to the repository.
- The current FastAPI response model expects a structured prediction response. The prediction function already returns that structure, but the route currently wraps it in a string.
- The Streamlit frontend currently uses a local API URL. Update `API_URL` before deploying the frontend separately.
- City tier data currently lives in `config/city_tier.py`. For stricter configuration management, move it to `config.yaml`.


