## WebScraping and File Downloading with Python.

This folder contains code used to scrape www.ncei.noaa.gov website for files sitting at the following location

https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/

The specific file was `Last Modified` on ``2022-02-07 14:03`.

After finding this file, the code builds a url for the file, downloads it and loads it into pandas to print out the record with the highest `HourlyDryBulbTemperature` to the terminal.



#### Setup
1. cd to  `Exercises/2-Webscraping_File_Downloading` folder.
   
2. Run `docker build --tag=exercise-2 .` to build the `Docker` image.
   
3. Run `docker-compose up run` to run program.

