import itertools
import papermill as pm
import yaml

### Parameters ###
with open("evaluation.yaml", "r") as file:
   params = yaml.load(file)

### Paths ###
sample_path = "out/dataset.json"

### Sample users from dataset ###
pm.execute_notebook(
   "src/sample_users.ipynb",
   "out/sample_users.ipynb",
   parameters = {
       "data": params["dataset"]["path"],
       "output": sample_path,
       "sample": params["dataset"]["sample_size"],
   }
)

### Fetch recommendations from API ###
for application in params["applications"]:
   salsa = params["salsa"]
   configurations = list(itertools.product(salsa["walks"], salsa["walk_length"], salsa["limit"]))
   app_id = application["id"]

   for configuration in configurations:
      walks, walk_length, limit = configuration
      print(f"Query recommendations: ", app_id, " walks: ", walks, " walk_length: ", walk_length, " limit: ", limit)

      name = f"{app_id}_{walks}walks_{walk_length}length_{limit}limit"
      recommendation_path = f"out/{name}_recommendations.json"

      pm.execute_notebook(
         "src/query_recommendations.ipynb",
         f"out/query__{name}_recommendations.ipynb",
         parameters = {
            "host": application["host"],
            "port": application["port"],
            "users": sample_path,
            "output": recommendation_path,
            "walks": walks,
            "walk_length": walk_length,
            "limit": limit,
         }
      )

### Anaylse recommendations of each application ###

### Compare recommendations between applications ###
