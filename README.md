# Kafka Salsa Evaluation
## Abstract
This repository contains code to evaluate the implementation of the [kafka-salsa](https://github.com/torbsto/kafka-salsa) project. Kafka-salsa is an in-memory, graph-based tweet recommender system implemented on [Kafka-Streams](https://kafka.apache.org/documentation/streams/), which uses an interaction graph (e.g., likes, writes, retweets) between users and tweets to recommend new tweets to a given user. The project implements four different approaches to store this interaction graph, potentially also impacting the accuracy of the recommendation. This repository contains a docker-based test suite to evaluate performance and quality differences between the four different implementations. Find the full documentation, evaluation metrics and results in the central repository [kafka-salsa](https://github.com/torbsto/kafka-salsa).

## Repository Overview
This repository is part of a larger project. Here is a list of all related repositories:
* [kafka-salsa](https://github.com/torbsto/kafka-salsa): Reference implementation and project documentation.
* [kafka-salsa-evaluation](https://github.com/philipphager/kafka-salsa-evaluation): Evaluation suite for [kafka-salsa](https://github.com/torbsto/kafka-salsa).
* [twitter-cralwer](https://github.com/philipphager/twitter-crawler): Twitter API crawler for user-tweet-interaction data.
* [twitter-dataset](https://github.com/philipphager/twitter-dataset): Crawled datasets of user-tweet-interactions used in evaluation.

## Installation
1. Clone the repository: `git clone git@github.com:philipphager/kafka-salsa-evaluation.git`
2. Install and start [Docker](https://www.docker.com/products/docker-desktop).
3. Navigate into the repository: `cd ./kafka-salsa-evaluation/`
4. Build the Docker image: `docker build --rm -t kafka-salsa/evaluation .`
5. Download a tweet dataset from [twitter-dataset](https://github.com/philipphager/twitter-dataset/) and place it in `data/`: `wget -P ./data/ https://media.githubusercontent.com/media/philipphager/twitter-dataset/master/v1/tweets-dedupe.csv`
6. Run the image and mount the `out/` directory to the container to obtain the evaluation results: `docker run -it -p 8888:8888 -v $(pwd)/kafka-salsa-evaluation/out:/home/jovyan/out --rm kafka-salsa/evaluation`
7. The evaluation results are published as Jupyter notebooks inside the `out/` directory. We recommend to use [nteract](https://nteract.io) to open the notebooks.


## Evaluation Parameters
Configure the evaluation using the [evaluation.yaml](https://github.com/philipphager/kafka-salsa-evaluation/blob/master/evaluation.yaml) file. Note that the project performs a cross evaluation of all combinations of salsa parameters for each configured kafka-salsa approach (application). 

| Parameter        | Description                        | Default |
| ---------------- | ---------------------------------- | ------- |
| dataset-path  | Path to test dataset.  | ./data/tweets-dedupe.csv |
| dataset-sample_size | Number of users to sample. All evaluation requests will be performed for each sampled user. | 100 |
| applications_id | Name for implementaion appraoch. |  |
| applications_host | IP address of deployed kafka-salsa endpoint. |  |
| applications_port | Port of deployed kafka-salsa endpoint. |  |
| salsa_walks | Number of random SALSA walks performed for each recommendation. |  |
| salsa_length | Length of each random SALSA walk. |  |
| salsa_limit | Top n tweets returned from the API. |  |


