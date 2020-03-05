# DESCRIPTION
    Scrapes canyon outlet to let you know when new bike is added

# USAGE
    Periodically run script with following arguments:
    * --email                      // Your email address 
    * --locale                     // Your region locale: de, en, gb, us... (default=hr)
    * --type                       // Bike outlet type: road, mountain, urban, fitness, pro (default=road)
    * --size                       // Bike size: 3XS, 2XS, XS, S, M, L, XL, 2XL, 3XL
    * --model                      // Bike model (possible multiple comma separated models)
    * --gender                     // Bike gender: Unisex, WMN (default=Unisex)

    First run will send all bikes from outlet matching the given filter criteria. Every subsequent run will send bikes that are newly added, if any.
    
# EXAMPLE
    `python canyonscrape.py --email my@email.com --locale hr --type road --size L --model Speedmax,Aeroad --gender Unisex`



