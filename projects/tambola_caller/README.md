# Tambola Caller

## Overview

This project is a Tambola Caller application running in a Docker container with persistent data storage. The first layer, called the "scanning layer," allows users to upload images of numbers, extract the numbers from the image, and store unique numbers in a persistent storage.

## Directory Structure

tambola_caller/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
│
├── scanning_layer/
│ ├── init.py
│ ├── app.py
│ ├── utils.py
│ └── data/
│ └── numbers.txt
│
└── README.md


## Setup

1. **Build the Docker Image**

    ```bash
    docker-compose build
    ```

2. **Run the Docker Container**

    ```bash
    docker-compose up
    ```

## Usage

Upload an image containing numbers via a POST request to the `/upload` endpoint.
