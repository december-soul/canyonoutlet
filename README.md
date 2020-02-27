DESCRIPTION: 
Scrapes canyon outlet to let you know when new bike is added.

USAGE: 

1. Obtain proper URL
    - Go to outlet section of canyon website using web browser of your choice
    - Set desired filters and sorting options on the website
    - Copy complete URL to url variable in main.py

2. Set email address on which to receive outlet updates
    - Set emailAddress variable in main.py

3. Run locally or upload to any host service
    - First run will send all bikes from outlet matching the given filter criteria
    - Every subsequent run will send bikes that are newly added, if any
    - Set trigger to run code in desired intervals

