import urllib.request
import json

run_id = "27400888717"
url = f"https://api.github.com/repos/TheStrokeForge/zmk-config-corne-xiao-frans/actions/runs/{run_id}/artifacts"

req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        for art in data.get('artifacts', []):
            print(f"Artifact: {art['name']}")
            print(f"  Size: {art['size_in_bytes']} bytes")
            print(f"  URL: {art['archive_download_url']}")
except Exception as e:
    print(f"Error: {e}")
