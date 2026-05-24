# Insurance Premium Prediction

Streamlit app for predicting an insurance premium category from customer profile inputs.

## Project Structure

```text
insurance-premium-prediction/
|-- streamlit_app.py          # Streamlit UI and app entrypoint
|-- requirements.txt          # Streamlit Cloud dependencies
|-- config.yaml               # Runtime config
|-- config/
|   |-- city_tier.py          # City tier lists
|   `-- settings.py           # Config loading helpers
|-- model/
|   |-- demo_model.py         # Demo model class used by the current pickle
|   |-- model.pkl             # Serialized model artifact
|   `-- prediction.py         # Model loading, prediction, and logging
`-- schema/
    `-- user_input.py         # Input validation and feature engineering
```

## Deploy On Streamlit Cloud

Use this as the main file path:

```text
streamlit_app.py
```

The app loads the model from:

```text
model/model.pkl
```

That path is configured in `config.yaml`.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Prediction Inputs

The UI collects raw customer fields and derives the model features:

| Raw input | Model feature |
| --- | --- |
| `weight`, `height` | `bmi` |
| `age` | `age_group` |
| `smoker`, `bmi` | `lifestyle_risk` |
| `city` | `city_tier` |
| `income_lpa` | `income_lpa` |
| `occupation` | `occupation` |

Every prediction is logged to the path configured by `prediction_logging.path` in `config.yaml`.
