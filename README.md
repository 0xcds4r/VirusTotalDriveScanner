# VirusTotalDriveScanner

This tool will allow you to check your PC for malicious files/programs.


To do this, the VirusTotal API is used to guarantee the quality of verification, 
however, this may take some time if we proceed from the limitations of API requests.

Python version is 3.10.5


How to check python version?
```
python --version
```

How to run?
```
python VTDS.py
```

Before launching, we strongly recommend registering an account on the site: 
```
https://www.virustotal.com/
```

And get the API key, more detailed instructions are described at this link: 
```
https://developers.virustotal.com/reference/getting-started
```

Before using the utility, you should edit its code (Open VTDS.py in text editor), find the following line in it:
```
API_KEY = 'ENTER_HERE_YOUR_API_KEY'
```

Instead of ENTER_HERE_YOUR_API_KEY, you should insert your API key, this is necessary for the utility to work.
