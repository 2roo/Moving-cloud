import os
import requests
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = '062b2682-c6b1-4a3e-b2b0-16d65261098e'
SCOPES = ['Files.ReadWrite']
access_token = generate_access_token(APP_ID, SCOPES)

# file_list = ["./download/b.txt", "./download/윤가현-2022-07-06-aa5555.pdf", "./download/싸지방용/files.txt", "./download/문서/2021-2/#영상/디지털시스템및실험/1115-1 디시.mp4"]
file_list = ["./download/문서/2021-2/#영상/디지털시스템및실험/1115-1 디시.mp4"]
for file_path in file_list:
    file_name = os.path.basename(file_path)
    total_file_size = file_size = os.path.getsize(file_path)


    if not os.path.exists(file_path):
        raise Exception(f'{file_name} is not found.')

    # file_path = file_path[2:]

    headers = {
        'Authorization': 'Bearer ' + access_token['access_token'],
        'content-type': 'application/json; charset=UTF-8',
        'Content-Length': str(file_size),
        'Content-Range': f'bytes 0-{file_size-1}/{file_size}'
    }

    # 400MB 이하    
    request_body = {
        'description' : 'a large file',
        'fileSystemInfo': { '@odata.type': 'microsoft.graph.fileSystemInfo' },
        '@mirosoft.graph.conflictBehavior': 'rename',
        'name' : file_name
    }

    #upload session
    response_upload_session = requests.post(
        GRAPH_API_ENDPOINT + f'/me/drive/items/root:/GDrive/{file_path}:/CreateUploadSession',
        headers=headers,
        json=request_body
    )
    print(response_upload_session)

    headers2 = {
        'content-type': 'application/json; charset=UTF-8',
        'Content-Length': str(total_file_size),
        'Content-Range': f'bytes 0-{total_file_size-1}/{total_file_size}'
    }

    try:
        upload_url = response_upload_session.json()['uploadUrl']
    except Exception as e:
        raise Exception(str(e))

    with open(file_path, 'rb') as upload:
        total_file_size = os.path.getsize(file_path)
        chunk_size = 327680
        chunk_number = total_file_size // chunk_size
        chunk_leftover = total_file_size - chunk_size * chunk_number
        counter = 0
        
        while True:
            chunk_data = upload.read(chunk_size)
            
            start_index = counter * chunk_size
            end_index = start_index + chunk_size
            
            if not chunk_data:
                break
            if counter == chunk_number:
                end_index = start_index + chunk_leftover
            
            headers = {
                'Content-Type': 'application/json; charset=UTF-8',
                'Content-Length': f'{chunk_size}',
                'Content-Range': 'bytes {start_index}-{end_index-1}/{total_file_size}'
            }
            chunk_data_upload_status = requests.put(
                upload_url,
                headers=headers,
                data=chunk_data
            )
            # print('Upload Progress: {0}'.format(chunk_data_upload_status.json()['nextExpectedRanges']))
            counter += 1
            print(chunk_data_upload_status)
            print(chunk_data_upload_status.json())
            