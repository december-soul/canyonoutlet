# DESCRIPTION
Scrapes canyon outlet to let you know when new bike is added

# USAGE
Periodically run script with arguments from table below.
    
Argument | Description              | Values                                | Default
-------- | ------------------------ | ------------------------------------- | ------------
--email  | Your email address       |                                       | **required**
--locale | Your region locale       | de, en, gb, us...                     | hr
--type   | Bike outlet type         | road, mountain, urban, fitness, pro   | road
--size   | Bike size                | 3XS, 2XS, XS, S, M, L, XL, 2XL, 3XL   | **required**
--model  | Bike model(s)            |                                       | **required**
--gender | Bike gender              | Unisex, WMN                           | Unisex
--group  | Bike Groupset            | Ultegra, 105, Dura Ace, ..            | Ultegra
--price  | Max Bike price           |                                       | Unlimited

First run will send all bikes from outlet matching the given filter criteria. 
Every subsequent run will send bikes that are newly added, if any.
    
# EXAMPLE
```python canyonscrape.py --email my@email.com --locale en --type road --size L --model Speedmax,Aeroad```



