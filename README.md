DESCRIPTION: 
Scrapes canyon outlet to let you know when new bike is added

USAGE: 
1. Obtain canyon outlet URL
    - Go to outlet section of canyon website using web browser of your choice
    - Set desired filters and sorting options on the website
    - Select and copy to clipboard complete URL found in web browser address tab (e.g. https://www.canyon.com/en-hr/outlet/road-bikes/?cgid=outlet-road&prefn1=pc_familie&prefn2=pc_geschlecht&prefn3=pc_outlet&prefn4=pc_rahmengroesse&prefn5=pg_materialgroup&prefv1=Speedmax%7CUltimate%7CAeroad&prefv2=Unisex&prefv3=true&prefv4=L&prefv5=Complete%20bikes&srule=sort_price_ascending)

2. Periodically run script
    - Script is run with following command: python main.py --email your_email_address --url paste_url_from_clipboard_here

First run will send all bikes from outlet matching the given filter criteria. Every subsequent run will send bikes that are newly added, if any.

To delete stored data run: python main.py --delete

