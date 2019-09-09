# Kafka Salsa Evaluation

## Abstract

## Repository Overview
This repository is part of a larger project. Here is a list of all related repositories:
* [kafka-salsa](https://github.com/torbsto/kafka-salsa): Reference implementation and project documentation.
* [kafka-salsa-evaluation](https://github.com/philipphager/kafka-salsa-evaluation): Evaluation suite for [kafka-salsa](https://github.com/torbsto/kafka-salsa).
* [twitter-cralwer](https://github.com/philipphager/twitter-crawler): Twitter API crawler for user-tweet-interaction data.
* [twitter-dataset](https://github.com/philipphager/twitter-dataset): Crawled datasets of user-tweet-interactions used in evaluations.

## Installation
1. Clone the repository: `git clone git@github.com:philipphager/kafka-salsa-evaluation.git`
2. Install and start [Docker](https://www.docker.com/products/docker-desktop).
3. Navigate into the repository: `cd ./kafka-salsa-evaluation/`
4. Build the Docker image: `docker build --rm -t kafka-salsa/evaluation .`
5. Download a tweet dataset from [twitter-dataset](https://github.com/philipphager/twitter-dataset/) and place it in `data/`: `wget -P ./data/ https://media.githubusercontent.com/media/philipphager/twitter-dataset/master/v1/tweets-dedupe.csv`
6. Run the image and mount the `out/` directory to the container to obtain the evaluation results: `docker run -it -p 8888:8888 -v $(pwd)/kafka-salsa-evaluation/out:/home/jovyan/out --rm kafka-salsa/evaluation`
