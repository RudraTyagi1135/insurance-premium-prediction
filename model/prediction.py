#basic import
import pickle
import pandas as pd


#import ml model 
with open("model/model.pkl",'rb') as file:
    model = pickle.load(file)

#mlflow
MODEL_VERSION =   "1.0.0"    


# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()


#predict output function
def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = str(model.predict(df)[0])

    # Get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    probabilities = [float(p) for p in probabilities]

    #confidence 

    confidence = float(max(probabilities))
    
    # Create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, probabilities))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": {k: round(v, 4) for k, v in class_probs.items()}
    }
