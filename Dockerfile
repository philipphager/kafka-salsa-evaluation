FROM jupyter/minimal-notebook

# Add dependencies
RUN pip install pandas
RUN pip install requests
RUN pip install papermill
RUN pip install ipywidgets

# Code
COPY data/* data/
COPY *.ipynb .
COPY *.py .

# Jupyter
EXPOSE 8888

CMD python main.py
