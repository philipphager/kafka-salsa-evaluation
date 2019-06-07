import papermill as pm

pm.execute_notebook(
   "src/sample_users.ipynb",
    "out/sample_users.ipynb",
   parameters = {
       "data": "data/tweets-dedupe.csv",
       "output": "out/users.json",
       "sample": 100,
   }
)

pm.execute_notebook(
   "src/query_recommendations.ipynb",
    "out/query_recommendations.ipynb",
   parameters = {
       "users": "out/users.json",
       "output": "out/tweet-recommendations.json",
       "top_n": 50,
   }
)

# Reset evaluation here...
# Query API again

pm.execute_notebook(
   "src/analyse_recommendations.ipynb",
    "out/analyse_recommendations.ipynb",
   parameters = {
       "recommendations": "out/tweet-recommendations.json",
   }
)

