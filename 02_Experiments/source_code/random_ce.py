import numpy as np

class RandomCE:
    def __init__(self, model, feature_bounds, max_iter=100):
        """
        Random Counterfactual Explanation baseline
        :param model: trained classifier with predict method
        :param feature_bounds: dict {feature_idx: (min_val, max_val)}
        :param max_iter: maximum random tries
        """
        self.model = model
        self.feature_bounds = feature_bounds
        self.max_iter = max_iter

    def generate(self, x, target_class):
        import pandas as pd
        for _ in range(self.max_iter):
            x_cf = x.copy()
            for j in range(len(x)):
                low, high = self.feature_bounds[j]
                x_cf[j] = np.random.uniform(low, high)
            # If using LightGBM, ensure DataFrame input for predictions
            if hasattr(self.model, "predict") and hasattr(self.model, "booster_"):
                X_df = pd.DataFrame([x_cf], columns=[f"f{j}" for j in range(len(x_cf))])
                if self.model.predict(X_df)[0] == target_class:
                    return x_cf
            else:
                if self.model.predict([x_cf])[0] == target_class:
                    return x_cf
        return None
