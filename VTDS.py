import hashlib
import os
import requests
import time

# Your API key from VirusTotal
API_KEY = 'ENTER_HERE_YOUR_API_KEY'

# Define the file path where you want to save the console output
output_file = os.path.join(os.path.expanduser("~"), "Desktop", "virustotal_output.log")

# Keep track of the files that have already been analyzed
analyzed_files = set()

# Count the total number of files to scan
total_files_scanned = 0

# Iterate over all drives on the system
for drive in ['%s:\\' % d for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists('%s:' % d)]:
    # Iterate over all files on the drive with extensions .exe, .dll, and .ocx
    for dirpath, _, filenames in os.walk(drive):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in ('.exe', '.dll', '.ocx'):
                filepath = os.path.join(dirpath, filename)

                # Skip files that have already been analyzed
                file_hash = hashlib.sha256(open(filepath, 'rb').read()).hexdigest()
                if file_hash in analyzed_files:
                    continue

                # Construct the API request URL
                url = 'https://www.virustotal.com/vtapi/v2/file/report'
                params = {'apikey': API_KEY, 'resource': file_hash}

                # Send the API request and get the response
                response = requests.get(url, params=params)

                # Check if the request was successful
                if response.status_code == 204:
                    print(f'HTTP status code 204 received for {filepath}.')
                    continue
                elif response.status_code != 200:
                    print(f'HTTP error {response.status_code} received for {filepath}.')
                    continue

                # Add the file hash to the set of analyzed files
                analyzed_files.add(file_hash)

                # Parse the response JSON
                json_response = response.json()

                # Print the results
                if json_response['response_code'] == 0:
                    print(f'No results found for {filepath}.')
                    continue
                else:
                    console_output = f'Results for {filepath}:\n'
                    for antivirus, result in json_response['scans'].items():
                        console_output += f'{antivirus}: {result["result"]}\n'
                    print(console_output)

                # Write the console output to the output file
                with open(output_file, 'a') as f:
                    f.write(console_output)

                total_files_scanned += 1
                print("Total files scanned: ", total_files_scanned);
                print("Please wait while the next file is being scanned.")

                # Delay before making the next API request
                # This is to prevent the 204 error from appearing
                time.sleep(15)
