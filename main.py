import papermill as pm
import yaml

### Parameters ###
with open("evaluation.yaml", "r") as file:
   params = yaml.load(file)

### Sample users from dataset ###
pm.execute_notebook(
   "src/sample_users.ipynb",
    "out/sample_users.ipynb",
   parameters = {
       "data": params["dataset"]["path"],
       "output": "out/dataset.json",
       "sample": params["dataset"]["sample_size"],
   }
)

for application in params["applications"]:
   app_id = application["id"]

   ### Fetch recommendations from API ###
   pm.execute_notebook(
      "src/query_recommendations.ipynb",
      f"out/query_{app_id}_recommendations.ipynb",
      parameters = {
         "host": application["host"],
         "port": application["port"],
         "users": "out/dataset.json",
         "output": f"out/{app_id}-recommendations.json",
         "top_n": params["dataset"]["top_n"],
      }
   )

   ### Anaylse basic recommendation statistics ###
   pm.execute_notebook(
      "src/analyse_recommendations.ipynb",
      f"out/analyse_{app_id}_recommendations.ipynb",
      parameters = {
         "recommendations": f"out/{app_id}-recommendations.json",
      }
   )

### Compare recommendations ###
# TODO: Adjust notebook to support list of applications
simple = params["applications"][0]["id"]
sampled = params["applications"][1]["id"]

pm.execute_notebook(
   "src/compare_recommendations.ipynb",
   "out/compare_recommendations.ipynb",
   parameters = {
       "baseline_recommendations": f"out/{simple}-recommendations.json",
       "sampled_recommendations": f"out/{sampled}-recommendations.json",
   }
)
