import streamlit as st

from model.prediction import MODEL_VERSION, ModelArtifactNotFoundError, get_model_path, predict_output
from schema.user_input import UserInput


st.set_page_config(page_title="Insurance Premium Predictor")

st.title("Insurance Premium Category Predictor")
st.caption(f"Model version: {MODEL_VERSION}")

age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ["retired", "freelancer", "student", "government_job", "business_owner", "unemployed", "private_job"],
)

if st.button("Predict Premium Category"):
    try:
        validated_input = UserInput(
            age=age,
            weight=weight,
            height=height,
            income_lpa=income_lpa,
            smoker=smoker,
            city=city,
            occupation=occupation,
        )

        model_input = {
            "bmi": validated_input.bmi,
            "age_group": validated_input.age_group,
            "lifestyle_risk": validated_input.lifestyle_risk,
            "city_tier": validated_input.city_tier,
            "income_lpa": validated_input.income_lpa,
            "occupation": validated_input.occupation,
        }
        result = predict_output(model_input)

        st.success(f"Predicted category: {result['predicted_category']}")
        st.metric("Confidence", f"{result['confidence']:.1%}")
        st.subheader("Class probabilities")
        st.dataframe(
            [
                {"category": category, "probability": probability}
                for category, probability in result["class_probabilities"].items()
            ],
            use_container_width=True,
            hide_index=True,
        )

    except ModelArtifactNotFoundError:
        st.error(f"Model file not found at `{get_model_path()}`.")
        st.info(
            "Add the trained `model.pkl` artifact to `model/model.pkl` before deploying, "
            "or change `model.path` in `config.yaml` to the deployed artifact location."
        )
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
