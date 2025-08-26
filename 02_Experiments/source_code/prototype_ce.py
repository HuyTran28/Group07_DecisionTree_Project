import numpy as np
from sklearn.metrics import pairwise_distances

class PrototypeCE:
    def __init__(self, model, X_train, y_train):
        """
        Prototype-based Counterfactual Explanation
        :param model: trained classifier
        :param X_train: training data (numpy array)
        :param y_train: training labels
        """
        self.model = model
        self.X_train = X_train
        self.y_train = y_train

    def generate(self, x, target_class):
        import pandas as pd
        candidates = self.X_train[self.y_train == target_class]
        if len(candidates) == 0:
            return None

        # chọn prototype gần nhất
        dists = pairwise_distances([x], candidates)[0]
        nearest_idx = np.argmin(dists)
        prototype = candidates[nearest_idx]

        # If using LightGBM, ensure DataFrame input for predictions
        if hasattr(self.model, "predict") and hasattr(self.model, "booster_"):
            X_df = pd.DataFrame([prototype], columns=[f"f{j}" for j in range(len(prototype))])
            if self.model.predict(X_df)[0] == target_class:
                return prototype
            else:
                return None
        else:
            return prototype
