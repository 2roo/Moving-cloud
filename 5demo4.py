import os
import requests
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = '062b2682-c6b1-4a3e-b2b0-16d65261098e'
SCOPES = ['Files.ReadWrite']
# SCOPES = ['Sites.ReadWrite.All']
access_token = generate_access_token(APP_ID, SCOPES)

# file_list = ["./download/a/2021-2/c/d/e.mp4"]
file_list = ["./download/b.txt", "./download/윤가현-2022-07-06-aa5555.pdf", "./download/싸지방용/files.txt", "./download/문서/2021-2/#영상/디지털시스템및실험/1115-1디시.mp4"]
for file_path in file_list:
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    file_path = file_path[2:]

    if not os.path.exists(file_path):
        raise Exception(f'{file_name} is not found.')

    #Creating an upload session
    headers2 = {
        'Authorization': 'Bearer ' + access_token['access_token'],
        'content-type': 'application/json; charset=UTF-8',
        'Content-Length': str(file_size),
        'Content-Range': f'bytes 0-{file_size-1}/{file_size}'
    }
    request_body = {
        'description' : 'a large file',
        'fileSystemInfo': { '@odata.type': 'microsoft.graph.fileSystemInfo' },
        '@mirosoft.graph.conflictBehavior': 'rename',
        'name' : file_name
    }
    upload_session = requests.post(
        GRAPH_API_ENDPOINT + f'/me/drive/items/root:/GDrive/{file_path}:/createUploadSession',
        headers=headers2, 
        json=request_body
    ).json()
    print(1)
    print(upload_session)
    with open(file_path, 'rb') as f:
        total_file_size = os.path.getsize(file_path)
        chunk_size = 327680
        chunk_number = total_file_size//chunk_size
        chunk_leftover = total_file_size - chunk_size * chunk_number
        i = 0
        while True:
            chunk_data = f.read(chunk_size)
            start_index = i*chunk_size
            end_index = start_index + chunk_size
            #If end of file, break
            if not chunk_data:
                break
            if i == chunk_number:
                end_index = start_index + chunk_leftover
            #Setting the header with the appropriate chunk data location in the file
            headers = {'Content-Length':'{}'.format(chunk_size),'Content-Range':'bytes {}-{}/{}'.format(start_index, end_index-1, total_file_size)}
            #Upload one chunk at a time
            chunk_data_upload = requests.put(upload_session['uploadUrl'], data=chunk_data, headers=headers)
            print(chunk_data_upload)
            try:
                print(chunk_data_upload["createdBy"])
                print("complete")
                break
            except:
                try:
                    print(chunk_data_upload.json()["nextExpectedRanges"])
                except:
                    print(chunk_data_upload.json())
                    input()
            i = i + 1
