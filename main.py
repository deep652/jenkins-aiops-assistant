from monitor.jenkins_client import JenkinsClient
from analysis.log_analyzer import LogAnalyzer
from ai.ai_client import AIClient
from notifications.email_service import EmailService

import os
from dotenv import load_dotenv

load_dotenv()

job_name = "pipeline-demo"

analyzer = LogAnalyzer()
ai = AIClient()
email = EmailService()

jenkins = JenkinsClient(
    base_url=os.getenv("JENKINS_URL"),
    username=os.getenv("JENKINS_USER"),
    api_token=os.getenv("JENKINS_API_TOKEN"),
)
build = jenkins.get_last_build(job_name)
print(build["result"])
print(build["number"])

if build["result"] == "FAILURE":
    logs = jenkins.get_console_logs(
        job_name,
        build["number"]
    )

    relevant_logs = analyzer.extract_failure_context(logs)

    summary = ai.summarize(relevant_logs)
    subject = (
        f"* Jenkins pipeline failed - "
        f"{job_name} (Build #{build['number']})"
    )
    email_body = f"""
    Pipeline Name : {job_name}
    Build Number  : #{build['number']}
    Status        : {build['result']} 

    ---------------------------------------------

    AI Analysis
    {summary}

    ---------------------------------------------

    Jenkins Build

    {os.getenv("JENKINS_URL")}/job/{job_name}/{build['number']}/

    """

    email.send(
        subject=subject,
        body=email_body
    )