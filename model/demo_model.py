class ClassLabels(list):
    def tolist(self):
        return list(self)


class DemoInsuranceModel:
    classes_ = ClassLabels(["Low", "Medium", "High"])

    def _score(self, row) -> float:
        score = 0.0
        bmi = float(row["bmi"])
        income_lpa = float(row["income_lpa"])

        if row["age_group"] == "senior":
            score += 2.0
        elif row["age_group"] == "middle_aged":
            score += 1.2
        elif row["age_group"] == "adult":
            score += 0.6

        if row["lifestyle_risk"] == "high":
            score += 2.0
        elif row["lifestyle_risk"] == "medium":
            score += 1.0

        if bmi > 32:
            score += 1.0
        elif bmi > 28:
            score += 0.5

        if int(row["city_tier"]) == 1:
            score += 0.4
        elif int(row["city_tier"]) == 2:
            score += 0.2

        if income_lpa > 25:
            score += 1.0
        elif income_lpa > 15:
            score += 0.5

        if row["occupation"] in {"business_owner", "freelancer"}:
            score += 0.4
        elif row["occupation"] in {"student", "unemployed"}:
            score -= 0.4

        return score

    def predict(self, X):
        predictions = []
        for _, row in X.iterrows():
            score = self._score(row)
            if score >= 4.0:
                predictions.append("High")
            elif score >= 2.0:
                predictions.append("Medium")
            else:
                predictions.append("Low")
        return predictions

    def predict_proba(self, X):
        probabilities = []
        for _, row in X.iterrows():
            score = self._score(row)
            high = min(max((score - 1.5) / 4.0, 0.05), 0.9)
            medium = min(max(1.0 - abs(score - 3.0) / 3.0, 0.05), 0.8)
            low = min(max((3.2 - score) / 3.2, 0.05), 0.9)
            total = low + medium + high
            probabilities.append([low / total, medium / total, high / total])
        return probabilities
