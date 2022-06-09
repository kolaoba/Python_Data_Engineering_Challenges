# Downloading Files with Python - Synchronously

This folder contains code used to create a downloads folder, iteratively download files from a list of uris, unzip them and delete zip files.

Code is modularised and split into main.py and helper_functions.py scripts with the latter supplying utility functions to the main.py file.

Error handling is included to accomodate bad uris.

#### Setup
1. cd to  `Exercises/1a-Synchronously_Download_Files_With_Python` folder.
   
2. Run `docker build --tag=exercise-1a .` to build the `Docker` image.
   
3. Run `docker-compose up run` to run program.
