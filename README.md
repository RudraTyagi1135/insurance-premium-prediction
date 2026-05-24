# Insurance Premium Prediction

A Streamlit app that estimates an insurance premium category from customer profile inputs. The app is deployment-ready for Streamlit Cloud and includes a bundled demo model artifact so the UI can run without a separate backend service.

Live app:


https://insurance-premium-predictor-1.streamlit.app/


## What This Project Does

The app collects:

- Age
- Weight and height
- Annual income in LPA
- Smoking status
- City
- Occupation

It derives model-ready features, loads a serialized model from `model/model.pkl`, and returns:

- Predicted premium category: `Low`, `Medium`, or `High`
- Confidence score
- Class probability table

Every prediction is also logged as JSON lines using the path configured in `config.yaml`.

## Important Model Note

This repository currently uses a demo model, not a production-trained insurance model.

The included `model/model.pkl` serializes `DemoInsuranceModel` from `model/demo_model.py`. It uses transparent scoring rules based on age group, lifestyle risk, BMI, city tier, income, and occupation. This keeps the Streamlit app fully deployable and testable even when the original training dataset is not available.

For real use, replace `model/model.pkl` with a trained scikit-learn-compatible model that supports:

```text
predict(input_dataframe)
predict_proba(input_dataframe)
classes_
```

The expected model input columns are:

```text
bmi
age_group
lifestyle_risk
city_tier
income_lpa
occupation
```

## Project Structure

```text
insurance-premium-prediction/
|-- streamlit_app.py          # Streamlit UI and app entrypoint
|-- requirements.txt          # Runtime dependencies
|-- config.yaml               # Model and prediction logging config
|-- config/
|   |-- city_tier.py          # City tier reference lists
|   `-- settings.py           # Config loading and path helpers
|-- model/
|   |-- demo_model.py         # Demo model class used by current pickle
|   |-- model.pkl             # Serialized model artifact loaded at runtime
|   `-- prediction.py         # Model loading, inference, and prediction logging
`-- schema/
    `-- user_input.py         # Pydantic validation and feature engineering
```

## Feature Engineering

The UI collects raw customer inputs. `schema/user_input.py` validates them and computes the features used by the model.

| Raw input | Derived model feature |
| --- | --- |
| `weight`, `height` | `bmi` |
| `age` | `age_group` |
| `smoker`, `bmi` | `lifestyle_risk` |
| `city` | `city_tier` |
| `income_lpa` | `income_lpa` |
| `occupation` | `occupation` |

City tiers are defined in `config/city_tier.py`.

## Demo Model Logic

The bundled demo model is deterministic and rule-based. It increases the premium-risk score for signals such as:

- Older age groups
- High lifestyle risk
- Higher BMI
- Tier 1 or tier 2 cities
- Higher income
- Business owner or freelancer occupation

It then maps the score to `Low`, `Medium`, or `High`, and returns normalized class probabilities.

This is useful for demonstration and deployment validation. It should not be treated as actuarial, financial, or medical advice.

## Configuration

Runtime settings live in `config.yaml`:

```yaml
model:
  path: model/model.pkl
  version: 1.0.0

prediction_logging:
  enabled: true
  path: logs/predictions.jsonl
```

Prediction logs include request ID, timestamp, model version, derived input features, and prediction output.

## Run Locally

Create a virtual environment, install dependencies, and start Streamlit:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy On Streamlit Cloud

Use this main file path:

```text
streamlit_app.py
```

Required files for deployment:

```text
streamlit_app.py
requirements.txt
config.yaml
config/
schema/
model/model.pkl
model/demo_model.py
model/prediction.py
```

After pushing changes to GitHub, reboot the Streamlit Cloud app if it is still serving an older commit.

## Replacing The Demo Model

To use a real model:

1. Train a model or pipeline using the expected model input columns.
2. Ensure the object exposes `predict`, `predict_proba`, and `classes_`.
3. Serialize it to `model/model.pkl`.
4. Keep `config.yaml` pointing to that file.
5. Redeploy the Streamlit app.

If your real model artifact is too large for normal Git hosting, use Git LFS or download it during deployment from external storage.

## Tech Stack

- Streamlit
- Pydantic
- Pandas
- scikit-learn-compatible model interface
- YAML configuration

## Limitations

- The included model is a demo scoring model.
- No real training dataset is included.
- Predictions are for product demonstration only.
- Local verification requires a working Python installation.
