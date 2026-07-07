import urllib.request
import json

run_id = "27802662061"
url = f"https://api.github.com/repos/TheStrokeForge/zmk-config-corne-xiao-frans/actions/runs/{run_id}/jobs"

req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        for job in data.get('jobs', []):
            print(f"Job: {job['name']}")
            print(f"  Status: {job['status']}")
            print(f"  Conclusion: {job['conclusion']}")
            print(f"  HTML URL: {job['html_url']}")
            print(f"  Steps:")
            for step in job.get('steps', []):
                print(f"    - {step['name']}: {step['status']} ({step['conclusion']})")
except Exception as e:
    print(f"Error: {e}")
