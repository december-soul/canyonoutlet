DESCRIPTION
Scrapes canyon outlet to let you know when new bike is added.

BRANCHES
Master branch is optimised for MacOS execution, pythonanywhere branch is for pythonanywhere.com hosting service.

USAGE
1. Set up gmail
    - Turn on less secure access to your gmail account: https://hotter.io/docs/email-accounts/secure-app-gmail/
    - Set emailAddress and password variables for your account in main.py

2. Obtain proper url
    - Go to canyon website
    - Navigate to road bike outlet section
    - Set desired filters and sorting options
    - Copy url parameters to urlParameters variable in main.py

3. Run locally or upload to host service
    - First run will send all bikes from outlet matching the given filter criteria
    - Every subsequent run will send bikes that are newly added, if any

