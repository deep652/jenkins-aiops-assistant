import requests


class JenkinsClient:
    def __init__(self, base_url, username, api_token):
        self.base_url = base_url
        self.username = username
        self.api_token = api_token

    def get_last_build(self, job_name):
        url = f"{self.base_url}/job/{job_name}/lastBuild/api/json"

        response = requests.get(
            url,
            auth=(self.username, self.api_token)
        )

        return response.json()

    def get_console_logs(self, job_name, build_number):
    	url = f"{self.base_url}/job/{job_name}/{build_number}/consoleText"

    	response = requests.get(
        	url,
        	auth=(self.username, self.api_token)
    	)

    	return response.text
