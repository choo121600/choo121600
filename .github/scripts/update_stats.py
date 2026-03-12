import re
import os

merged = os.environ.get("MERGED", "0")
reviewed = os.environ.get("REVIEWED", "0")

with open("README.md", "r") as f:
    content = f.read()

merged_url = "https://github.com/apache/airflow/pulls?q=is%3Apr+author%3Achoo121600+is%3Amerged"
reviewed_url = "https://github.com/apache/airflow/pulls?q=is%3Apr+reviewed-by%3Achoo121600"

stats_block = (
    "<!-- AIRFLOW_STATS:START -->\n"
    f"  - [{merged} PRs merged]({merged_url})"
    f" · [{reviewed} PRs reviewed]({reviewed_url})\n"
    "<!-- AIRFLOW_STATS:END -->"
)

content = re.sub(
    r"<!-- AIRFLOW_STATS:START -->.*?<!-- AIRFLOW_STATS:END -->",
    stats_block,
    content,
    flags=re.DOTALL,
)

with open("README.md", "w") as f:
    f.write(content)

print(f"Updated: Merged={merged}, Reviewed={reviewed}")
