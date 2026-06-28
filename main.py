from monitor.jenkins_client import JenkinsClient
from analysis.log_analyzer import LogAnalyzer
import os
from dotenv import load_dotenv

load_dotenv()

analyzer = LogAnalyzer()

jenkins = JenkinsClient(
    base_url=os.getenv("JENKINS_URL"),
    username=os.getenv("JENKINS_USER"),
    api_token=os.getenv("JENKINS_API_TOKEN"),
)
build = jenkins.get_last_build("pipeline-demo")
print(build["result"])
print(build["number"])

if build["result"] == "FAILURE":
    logs = jenkins.get_console_logs(
        "pipeline-demo",
        build["number"]
    )

    relevant_logs = analyzer.extract_failure_context(logs)

    print(relevant_logs)
