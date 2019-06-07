import papermill as pm

### Evaluation parameters ###
sample_users = 100
recommendations_per_user = 10

### Sample users ###
pm.execute_notebook(
   "src/sample_users.ipynb",
    "out/sample_users.ipynb",
   parameters = {
       "data": "data/tweets-dedupe.csv",
       "output": "out/users.json",
       "sample": sample_users,
   }
)

### Fetch recommendations from API ###
# Fetch baseline recommendations
pm.execute_notebook(
   "src/query_recommendations.ipynb",
    "out/query_baseline_recommendations.ipynb",
   parameters = {
       "host": "host.docker.internal",
       "port": "8070",
       "users": "out/users.json",
       "output": "out/baseline-recommendations.json",
       "top_n": recommendations_per_user,
   }
)

# Fetch sampled recommendations
# TODO: Add other host / port configuration
pm.execute_notebook(
   "src/query_recommendations.ipynb",
    "out/query_sampled_recommendations.ipynb",
   parameters = {
       "host": "host.docker.internal",
       "port": "8070",
       "users": "out/users.json",
       "output": "out/sampled-recommendations.json",
       "top_n": recommendations_per_user,
   }
)

### Analysis ###
# Analyse baseline recommendations
pm.execute_notebook(
   "src/analyse_recommendations.ipynb",
    "out/analyse_baseline_recommendations.ipynb",
   parameters = {
       "recommendations": "out/baseline-recommendations.json",
   }
)

# Analyse sampled recommendations
pm.execute_notebook(
   "src/analyse_recommendations.ipynb",
    "out/analyse_sampled_recommendations.ipynb",
   parameters = {
       "recommendations": "out/sampled-recommendations.json",
   }
)

# Compare recommendations
pm.execute_notebook(
   "src/compare_recommendations.ipynb",
    "out/compare_sampled_recommendations.ipynb",
   parameters = {
       "baseline_recommendations": "out/baseline-recommendations.json",
        "sampled_recommendations": "out/sampled-recommendations.json",
   }
)
