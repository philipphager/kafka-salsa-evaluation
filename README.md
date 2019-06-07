## kafka-salsa-evaluation
This repository contains code to evaluate the [kafka-salsa](https://github.com/torbsto/kafka-salsa) tweet recommendation engine.

## Setup
1. Make sure you have docker installed.
2. Build the image: `docker build --rm -t kafka-salsa/evaluation .`
3. Download a graph dataset from [twitter-dataset](https://github.com/philipphager/twitter-dataset/) and place it in `data/`.
4. Run the image and mount the `out/` directory to the container: `docker run -it -p 8888:8888 -v /path/to/kafka-salsa-evaluation/out:/home/jovyan/out --rm kafka-salsa/evaluation`
