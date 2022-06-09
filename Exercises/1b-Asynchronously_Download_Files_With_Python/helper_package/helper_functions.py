import os
import zipfile
import aiofiles


# Define folder creation function
def create_downloads_folder():
    # Create downloads directory if not exists
    folderPath = "./downloads"

    if not os.path.exists(folderPath):
        print("Folder does not exist\nCreating downloads folder...")
        os.makedirs(folderPath)

    return folderPath

def extract_filename(url, folderPath):
    # Extract filename
    fileName = url.split('/')[-1]
    filePath = folderPath + "/" + fileName
    return fileName, filePath

async def save_file_asynchronously(response, filePath):
    # Save file
    file = await aiofiles.open(filePath, "wb") # write in binary mode
    await file.write(await response.content)
    await file.close()

def unzip_file(filePath, folderPath):
    # Unzip file using context manager
    with zipfile.ZipFile(filePath, 'r') as zipObj:
        zipObj.extractall(folderPath)