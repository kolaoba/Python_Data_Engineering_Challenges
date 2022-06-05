import requests
import os
import zipfile

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

# Define folder creation function
def create_downloads_folder():
    # Create downloads directory if not exists
    global folderPath
    folderPath = "./downloads"

    if not os.path.exists(folderPath):
        print("Folder does not exist\nCreating downloads folder...")
        os.makedirs(folderPath)


# define synchronous file download function
def download_files_synchronously():
    # Download files from uris
    for url in download_uris:
        print("Fetching url: " + url)
        req = requests.get(url)
        if not req.status_code == 200:
            print('Issue downloading from %s\nReturned status code %s' % (url, req.status_code))
            continue


        # Extract filename
        fileName = url.split('/')[-1]
        filePath = folderPath + "/" + fileName

        # Save file
        file = open(filePath, "wb") # write in binary mode
        file.write(req.content)
        file.close()
        print('%s saved successfully to %s' % (fileName, filePath) )

        # Unzip file using context manager
        with zipfile.ZipFile(filePath, 'r') as zipObj:
            zipObj.extractall(folderPath)
        
        # Remove zip files
        os.remove(filePath)



def main():
    # your code here
    create_downloads_folder()
    download_files_synchronously()


if __name__ == '__main__':
    main()
