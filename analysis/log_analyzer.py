class LogAnalyzer:

    def extract_failure_context(self, logs):
        lines = logs.splitlines()

        last_lines = lines[-200:]

        return "\n".join(last_lines)