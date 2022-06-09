import requests
import os
import aiohttp
import asyncio
from helper_package.helper_functions import *

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

# define synchronous file download function
async def download_files_asynchronously(folderPath):
    # Download files from uris
    for url in download_uris:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:

                print("Fetching url: " + url)

                # Error handling for unsuccessful downloads
                if not response.status_code == 200:
                    print('Issue downloading from %s\nReturned status code %s' % (url, response.status_code))
                    continue

                fileName, filePath = extract_filename(url, folderPath)

                save_file_asynchronously(response, filePath)

                print('%s saved successfully to %s' % (fileName, filePath))

                unzip_file(filePath, folderPath)

                # Remove zip files
                os.remove(filePath)

def main():
    # your code here
    folderPath = create_downloads_folder()
    # download_files_asynchronously(folderPath)
    dl_run = asyncio.get_event_loop()
    dl_run.run_until_complete(download_files_asynchronously(folderPath))

if __name__ == '__main__':
    main()
