import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class AIClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def summarize(self, logs):

        prompt = f"""
You are a senior DevOps engineer.

Read the following Jenkins logs.

Explain:

1. Why the pipeline failed.
2. What the likely root cause is.
3. Suggest the next troubleshooting step.

Jenkins Logs:

{logs}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text