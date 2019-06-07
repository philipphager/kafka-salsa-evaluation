import papermill as pm

pm.execute_notebook(
   "src/query_recommendations.ipynb",
    "out/query_recommendations.ipynb",
   parameters = {
       "data": "data/tweets-dedupe.csv",
       "sample": 100,
       "results": "out/tweets-dedupe.json",
       "top_n": 50
   }
)
