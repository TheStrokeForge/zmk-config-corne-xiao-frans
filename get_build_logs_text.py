import urllib.request
import json
import re

job_id = "82275942021"
# We can get job logs using the api
url = f"https://api.github.com/repos/TheStrokeForge/zmk-config-corne-xiao-frans/actions/jobs/{job_id}/logs"

req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

try:
    with urllib.request.urlopen(req) as response:
        log_text = response.read().decode('utf-8')
        # Print lines containing "overlay" or "seeeduino_xiao_ble"
        lines = log_text.split('\n')
        print(f"Total log lines: {len(lines)}")
        
        # Let's search for devicetree processing or overlay inclusion
        for idx, line in enumerate(lines):
            if any(x in line.lower() for x in ["overlay", "seeeduino_xiao_ble.overlay", "dts", "devicetree"]):
                print(f"L{idx}: {line}")
except Exception as e:
    print(f"Error: {e}")
