# Heron Coding Challenge - File Classifier

## Introduction

I delivered:
- basic document preprocessing
- 2.5 classifiers (half-done sklearn clf, openai clf, filename clf)
- a working dockerfile + ci/cd pipeline + basic tests

I explored writing the document preprocessing steps and classifiers in jupyter notebooks.
I prioritized exploring/demonstrating more breadth, rather than shipping super clean code that everyone would be happy to ship to production. There are still some print statements and egregious TODOs. I could totally clean it all up, but I will stick to the 3h recommendation instead.
The initial preprocessing and OpenAI classifier took most of the time. The dockerfile + ci/cd pipeline took another 45min or so. I had about 30-45min left for the sklearn classifier.

## Initial Approach

Based on intro call with Brain, Heron has a lot of work to pick up now, and is hiring to meet work demand. That means, they'll tend index more on people who can fulfill that demand. Given that, I'll demonstrate generalist robust shipping, rather than ability to be experimental/shake things up or depth in any one topic. If you want to see off-the-rails experimentation, check out [these](https://curiousest.com/editing-science-fiction-with-llms/) [two](https://curiousest.com/automating-art-craft/) articles introducing my explorations in writing science fiction with LLMs. Things to demonstrate:
- basic clf prototyping/training/serving
- something towards productionizing clf

ChatGPT conversation: https://chatgpt.com/share/67349c22-33ec-800f-977a-ad789c76b7b1
Code editor: Cursor (so there was a little more genAI than just the conversation above)

## Extending beyond this work

### What is a good starting point for production?

#### Misc
- decide where it will be deployed (Google Cloud Run? Vertex AI? An existing kubernetes cluster?)
- set up accounts, keys, deployment, etc.
- logging, monitoring, alerting

#### OpenAI clf
- billing alerts
- performance monitoring

#### Sklearn clf
- finish writing it
- add tests
- training 
   - more data
   - training CI
   - performance benchmark
   - confidence score, so that OpenAI clf can be used as a backup
- inference, which loads the trained model and serves it
- performance monitoring

### Where could we go next with this?

- look at load and usage patterns, and adapt infrastructure
	- load balancing
	- consider autoscaling (keep real time inference) vs. batch processing pipelines (go more async inference)
- use "more appropriate" GCP services for scaling up & production robustness:
	- VertexAI for training/deployment & model management
	- Cloud pub/sub for scaling up documents ingestion
	- BigQuery for storing metadata and establishing basic business/ops reporting
- improve classifier performance and MLOps
	- abstract away serving from training&inference so the model can be developed independently of the service
		- Why?
			- If a lot more effort goes into training a better model, it has a different dev loop than service deployment.
			- If we want to serve the model in different ways (ex: function call inside a larger model, REST API, batch inside a pipeline, etc.)
	- Speed up training & experimentation: save text embeddings of documents in a vector db
	- Establish a separate "prod for ML" environment, which has different permissions and compute requirements than "prod for services"
- document preprocessing
    - save files to cloud storage
    - save embeddings on files to a db
    - use more than just the text in classification (pdf visual structure, image embeddings, etc.)

## Overview

At Heron, we’re using AI to automate document processing workflows in financial services and beyond. Each day, we handle over 100,000 documents that need to be quickly identified and categorised before we can kick off the automations.

This repository provides a basic endpoint for classifying files by their filenames. However, the current classifier has limitations when it comes to handling poorly named files, processing larger volumes, and adapting to new industries effectively.

**Your task**: improve this classifier by adding features and optimisations to handle (1) poorly named files, (2) scaling to new industries, and (3) processing larger volumes of documents.

This is a real-world challenge that allows you to demonstrate your approach to building innovative and scalable AI solutions. We’re excited to see what you come up with! Feel free to take it in any direction you like, but we suggest:


### Part 1: Enhancing the Classifier

- What are the limitations in the current classifier that's stopping it from scaling?
- How might you extend the classifier with additional technologies, capabilities, or features?


### Part 2: Productionising the Classifier 

- How can you ensure the classifier is robust and reliable in a production environment?
- How can you deploy the classifier to make it accessible to other services and users?

We encourage you to be creative! Feel free to use any libraries, tools, services, models or frameworks of your choice

### Possible Ideas / Suggestions
- Train a classifier to categorize files based on the text content of a file
- Generate synthetic data to train the classifier on documents from different industries
- Detect file type and handle other file formats (e.g., Word, Excel)
- Set up a CI/CD pipeline for automatic testing and deployment
- Refactor the codebase to make it more maintainable and scalable

## Marking Criteria
- **Functionality**: Does the classifier work as expected?
- **Scalability**: Can the classifier scale to new industries and higher volumes?
- **Maintainability**: Is the codebase well-structured and easy to maintain?
- **Creativity**: Are there any innovative or creative solutions to the problem?
- **Testing**: Are there tests to validate the service's functionality?
- **Deployment**: Is the classifier ready for deployment in a production environment?


## Getting Started
1. Clone the repository:
    ```shell
    git clone <repository_url>
    cd heron_classifier
    ```

2. Install dependencies:
    ```shell
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```shell
    python -m src.app
    ```

4. Test the classifier using a tool like curl:
    ```shell
    curl -X POST -F 'file=@path_to_pdf.pdf' http://127.0.0.1:5000/classify_file
    ```

5. Run tests:
   ```shell
    pytest
    ```

## Submission

Please aim to spend 3 hours on this challenge.

Once completed, submit your solution by sharing a link to your forked repository. Please also provide a brief write-up of your ideas, approach, and any instructions needed to run your solution. 
