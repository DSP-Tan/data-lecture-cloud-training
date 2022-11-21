from taxifare.ml_logic.params          import LOCAL_REGISTRY_PATH
from taxifare.model_target.local_model import save_local_model
from taxifare.model_target.cloud_model import save_cloud_model

import glob
import os
import time

from colorama import Fore, Style

from tensorflow.keras import Model, models


def save_model(model: Model = None,
               params: dict = None,
               metrics: dict = None) -> None:
    """
    persist trained model, params and metrics
    """

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    if os.environ["MODEL_TARGET"]=="local":
        save_local_model(model,params,metrics,timestamp)
        return None
    elif os.environ["MODEL_TARGET"]=="cloud":
        save_cloud_model(model,timestamp)
        return None
    else:
        print(f"MODEL_TARGET variable: {os.environ['MODEL_TARGET']} is invalid")
        return None


def load_model(save_copy_locally=False) -> Model:
    """
    load the latest saved model, return None if no model found
    """
    print(Fore.BLUE + "\nLoad model from local disk..." + Style.RESET_ALL)

    # get latest model version
    model_directory = os.path.join(LOCAL_REGISTRY_PATH, "models")

    results = glob.glob(f"{model_directory}/*")
    if not results:
        return None

    model_path = sorted(results)[-1]
    print(f"- path: {model_path}")

    model = models.load_model(model_path)
    print("\n✅ model loaded from disk")

    return model
