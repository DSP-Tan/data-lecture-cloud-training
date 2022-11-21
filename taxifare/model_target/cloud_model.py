from google.cloud import storage
from taxifare.ml_logic.params import LOCAL_REGISTRY_PATH

import glob
import os

def save_cloud_model(model, suffix):

    # save the model
    if model:


        model_path = os.path.join(os.environ.get("LOCAL_REGISTRY_PATH"), "models",
                                  suffix + ".pickle")
        model.save(model_path)

        # list model files
        files = glob.glob(f"{model_path}/**/*.*", recursive=True)
        print(model_path)
        for file in files:
            storage_filename = file[17:]
            print(storage_filename)

            client = storage.Client()
            bucket = client.bucket(os.environ["BUCKET_NAME"])
            blob = bucket.blob(storage_filename)
            blob.upload_from_filename(file)
