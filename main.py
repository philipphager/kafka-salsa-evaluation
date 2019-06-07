import papermill as pm

pm.execute_notebook(
   "dataset.ipynb",
    "out/dataset-out.ipynb",
   parameters = {
       "data": "data/tweets-dedupe.csv",
       "sample": 100,
       "results": "out/tweets-dedupe.json",
       "top_n": 50
   }
)
