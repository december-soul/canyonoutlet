DESCRIPTION: 
    Scrapes canyon outlet to let you know when new bike is added

USAGE: 
    Periodically run script with following arguments:
    1. --email                      // Your email address 
    2. --locale                     // Your region locale: de, en, gb, us... (default=hr)
    3. --type                       // Bike outlet type: road, mountain, urban, fitness, pro (default=road)
    4. --size                       // Bike size: 3XS, 2XS, XS, S, M, L, XL, 2XL, 3XL
    5. --model                      // Bike model (possible multiple comma separated models)
    6. --gender                     // Bike gender: Unisex, WMN (default=Unisex)

    First run will send all bikes from outlet matching the given filter criteria. Every subsequent run will send bikes that are newly added, if any.
    
EXAMPLE:
    python canyonscrape.py --email my@email.com --locale hr --type road --size L --model Speedmax,Aeroad --gender Unisex



