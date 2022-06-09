import requests
import pandas as pd
from bs4 import BeautifulSoup
from helper_functions import create_downloads_folder, save_file



def main():
    # create downloads foler
    folder_path = create_downloads_folder()

    # Declare target url and target date
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    file_date = "2022-02-07 14:03"

    # get web page
    page = requests.get(url)

    # parse web page
    soup = BeautifulSoup(page.content, "html.parser")

    # retrieve target(s)
    target_file = soup.find_all(lambda tag:tag.name=='tr' and file_date in tag.text)

    # for multiple occurences of target
    if len(target_file) > 1:
        target_file = target_file[0]
    
    # search for target filename
    file_name = target_file.find('a')['href']


    # join url with file_name for file url
    file_url = url + file_name

    # download target file
    req = requests.get(file_url)

    # error handling for missing file
    if not req.status_code == 200:
        print('Issue downloading %s from %s\nReturned status code %s' % (file_name, url, req.status_code))
    
    file_path = folder_path + "/" + file_name

    save_file(req, file_path)

    # load file into pandas 
    df = pd.read_csv(file_path)

    # find records with highest HourlyDryBulbTemperature
    max_record = df[df["HourlyDryBulbTemperature"] == df["HourlyDryBulbTemperature"].max()]

    
    # print max record
    print('Maximum temperature of %s degrees occured on %s at %s' % (max_record['HourlyDryBulbTemperature'].values[0], max_record['DATE'].values[0], max_record['NAME'].values[0]))

if __name__ == '__main__':
    main()
