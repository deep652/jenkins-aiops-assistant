# 🤖 Jenkins AIOps Assistant

## Overview

Jenkins AIOps Assistant is a Proof of Concept (PoC) that demonstrates how Large Language Models (LLMs) can be integrated into a DevOps workflow.

The application monitors Jenkins pipelines using the Jenkins REST API, retrieves build information and console logs for failed builds, extracts the most relevant failure context, summarizes the failure using Google Gemini, and sends a formatted email notification to help engineers troubleshoot issues more quickly.

The project was built to explore REST API integrations, modular software design, and practical applications of AI in DevOps automation.

## Features

- Monitor Jenkins pipeline status using the Jenkins REST API
- Retrieve build metadata and console logs
- Extract relevant failure information from large logs
- Summarize failures using Google Gemini
- Send formatted email notifications using Gmail SMTP
- Modular architecture with clear separation of responsibilities

## Architecture

flowchart TD
    A[Jenkins Pipeline] --> B[Jenkins REST API]
    B --> C[JenkinsClient]
    C --> D[LogAnalyzer]
    D --> E[AIClient<br/>Google Gemini]
    E --> F[EmailService]
    F --> G[Email Notification]



## Project Structure


jenkins-aiops-assistant/
│
├── ai/
│ └── ai_client.py
│
├── analysis/
│ └── log_analyzer.py
│
├── monitor/
│ └── jenkins_client.py
│
├── notifications/
│ └── email_service.py
│
├── demo-pipelines/
│
├── docs/
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md

## Technologies Used

- Python 3
- Jenkins REST API
- Google Gemini API
- Gmail SMTP
- Requests
- python-dotenv

## Environment Variables

Create a `.env` file.

| Variable | Description |
|----------|-------------|
| JENKINS_URL | Jenkins server URL |
| JENKINS_USER | Jenkins username |
| JENKINS_API_TOKEN | Jenkins API Token |
| GEMINI_API_KEY | Google Gemini API Key |
| EMAIL_ADDRESS | Gmail address |
| EMAIL_APP_PASSWORD | Gmail App Password |
| JENKINS_JOB_NAME | Jenkins job to monitor |


## Running the Project

Clone the repository

```bash
git clone <repo-url>
cd jenkins-aiops-assistant

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

Run
python main.py


## Future Improvements

- Microsoft Teams notifications
- Slack integration
- Multiple Jenkins job monitoring
- HTML email templates
- Docker deployment
- Scheduled execution
- Support for additional LLM providers


## What I Learned

This project helped me understand:

- REST API integration
- API authentication using tokens
- JSON parsing
- AI-assisted log analysis
- Modular software design
- Email automation using SMTP
- Building end-to-end DevOps workflows

