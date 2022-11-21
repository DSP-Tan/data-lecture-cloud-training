from taxifare.ml_logic.params import LOCAL_REGISTRY_PATH
from tensorflow.keras import Model, models
from colorama import Fore, Style
import os
import pickle


def save_flocal_model(model, suffix):

    if model:

        model_path = os.path.join(LOCAL_REGISTRY_PATH, "models",
                                  suffix + ".pickle")

        print(f"- model path: {model_path}")

        model.save(model_path)

def save_local_model(model: Model = None,
                     params: dict = None,
                     metrics: dict = None,
                     suffix=None) -> None:
    """
    persist trained model, params and metrics
    """
    print(Fore.BLUE + "\nSave model to local disk..." + Style.RESET_ALL)

    # save params
    if params is not None:
        params_path = os.path.join(LOCAL_REGISTRY_PATH, "params", suffix + ".pickle")
        print(f"- params path: {params_path}")
        with open(params_path, "wb") as file:
            pickle.dump(params, file)

    # save metrics
    if metrics is not None:
        metrics_path = os.path.join(LOCAL_REGISTRY_PATH, "metrics", suffix + ".pickle")
        print(f"- metrics path: {metrics_path}")
        with open(metrics_path, "wb") as file:
            pickle.dump(metrics, file)

    # save model
    if model is not None:
        model_path = os.path.join(LOCAL_REGISTRY_PATH, "models", suffix)
        print(f"- model path: {model_path}")
        model.save(model_path)

    print("\n✅ model saved locally")

    return None
