FROM jupyter/minimal-notebook

# Add dependencies
RUN pip install pandas
RUN pip install requests
RUN pip install papermill
RUN pip install ipywidgets

# Code
COPY src/ src/
COPY data/ data/
COPY main.py main.py

# Jupyter
EXPOSE 8888

CMD python main.py
