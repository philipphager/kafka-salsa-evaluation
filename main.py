import itertools
import papermill as pm
import yaml

### Parameters ###
with open("evaluation.yaml", "r") as file:
   params = yaml.load(file)

### Paths ###
sample_path = "out/dataset.json"

### Compute variants ###
salsa = params["salsa"]
configurations = list(itertools.product(salsa["walks"], salsa["walk_length"], salsa["limit"]))

### Sample users from dataset ###
total_sample_size = params["dataset"]["sample_size"] * len(configurations)

pm.execute_notebook(
   "src/sample_users.ipynb",
   "out/sample_users.ipynb",
   parameters = {
       "data": params["dataset"]["path"],
       "output": sample_path,
       "sample": total_sample_size,
   }
)

### Fetch recommendations from API ###
for application in params["applications"]:
   app_id = application["id"]

   pm.execute_notebook(
         "src/query_recommendations.ipynb",
         f"out/query__{app_id}_recommendations.ipynb",
         parameters = {
            "host": application["host"],
            "port": application["port"],
            "users": sample_path,
            "output": f"out/{app_id}-recommendations.json",
            "walks": salsa["walks"],
            "walk_length": salsa["walk_length"],
            "limit": salsa["limit"],
            "sample_size": params["dataset"]["sample_size"],
         }
      )

### Anaylse recommendations of each application ###

### Compare recommendations between applications ###
