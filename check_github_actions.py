import urllib.request
import json

url = "https://api.github.com/repos/TheStrokeForge/zmk-config-corne-xiao-frans/actions/runs?per_page=5"

req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        for run in data.get('workflow_runs', []):
            print(f"Run #{run['run_number']}:")
            print(f"  Event: {run['event']}")
            print(f"  Status: {run['status']}")
            print(f"  Conclusion: {run['conclusion']}")
            print(f"  Commit: {run['head_commit']['message']}")
            print(f"  URL: {run['html_url']}")
            print()
except Exception as e:
    print(f"Error fetching workflow runs: {e}")
