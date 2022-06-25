import boto3
import gzip


def main():
    # your code here
    # declare bucket and object names
    BUCKET_NAME = "commoncrawl"
    OBJECT_NAME = "crawl-data/CC-MAIN-2022-05/wet.paths.gz"

    # intitialize s3 client with boto3
    s3 = boto3.client('s3')

    # retrieve object from s3 bucket
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_NAME)
    
    # extract body and decompress object
    content = obj['Body'].read()
    decompressed_obj = gzip.decompress(content).decode("utf-8")

    # read first line to extract key
    new_key = decompressed_obj.partition('\n')[0]

    # retreive new object using extracted key
    new_object = s3.get_object(Bucket=BUCKET_NAME, Key=new_key)

    # extract body and decompress new object
    new_content = new_object['Body'].read()
    decompressed_new_obj = gzip.decompress(new_content).decode("utf-8")
    
    # print to stdout

    print(decompressed_new_obj)


if __name__ == '__main__':
    main()
