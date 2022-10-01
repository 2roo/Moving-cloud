import os
import requests
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = '062b2682-c6b1-4a3e-b2b0-16d65261098e'
SCOPES = ['Files.ReadWrite']
# SCOPES = ['Sites.ReadWrite.All']
access_token = generate_access_token(APP_ID, SCOPES)

file_list = ["./download/a/2021-2/c/d/e.mp4"]
for file_path in file_list:
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)


    if not os.path.exists(file_path):
        raise Exception(f'{file_name} is not found.')
    with open(file_path, 'rb') as upload:
        file_path = file_path[2:]
        chunk_size = 327680
        chunk_number = file_size // chunk_size
        chunk_leftover = file_size - (chunk_size * chunk_number)
        counter = 0
        count = 0
        request_body = {
            # 'description' : 'a large file',
            # 'fileSystemInfo': { '@odata.type': 'microsoft.graph.fileSystemInfo' },
            'fileSystemInfo': { '@odata.type': 'microsoft.graph.driveItemUploadableProperties' },
            '@mirosoft.graph.conflictBehavior': 'rename',
            'name' : file_name
        }
        while True:
            chunk_data = upload.read(chunk_size)

            start_index = counter * chunk_size
            end_index = start_index + chunk_size

            if not chunk_data:
                break
            if counter == chunk_number:
                end_index = start_index + chunk_leftover
                chunk_size = chunk_leftover
            print(start_index, end_index, counter, chunk_number)
            
            if count == 0:
                headers2 = {
                    'Authorization': 'Bearer ' + access_token['access_token'],
                    # 'Content-Type': 'application/json; charset=UTF-8',
                    'Content-Length': f'{chunk_size}',
                    'Content-Range': f'bytes {start_index}-{end_index-1}/{file_size}'
                }
                # counter -= 1
                count += 1
                # upload.seek(0)
            else:
                headers2 = {
                    'Authorization': 'Bearer ' + access_token['access_token'],
                    # 'Content-Type': 'application/json; charset=UTF-8',
                    'Content-Length': f'{chunk_size}',
                    'Content-Range': f'bytes {start_index}-{end_index-1}/{file_size}'
                }
                
            # headers2 = {
            #     'Authorization': 'Bearer ' + access_token['access_token'],
            #     'Content-Type': 'application/json; charset=UTF-8',
            #     'Content-Length': f'{chunk_size}',
            #     'Content-Range': f'bytes {nextrange}/{file_size}'
            # }
            #upload session
            response_upload_session = requests.post(
                GRAPH_API_ENDPOINT + f'/me/drive/items/root:/GDrive/{file_path}:/createUploadSession',
                headers=headers2,
                json=request_body
            )
            response_upload_session = requests.post(
                GRAPH_API_ENDPOINT + f'/me/drive/items/root:/GDrive/{file_path}:/createUploadSession',
                headers=headers2,
                json=request_body
            )
            print(response_upload_session.json())
            input("")
            try:
                upload_url = response_upload_session.json()['uploadUrl']
                print(f'File: {file_path}')
                # print(f'{file_path} 업로드 완료')

            except Exception as e:
                print(e, 'error')
                # print(f'{file_path} 업로드 실패')
                break
            chunk_data_upload_status = requests.put(
                upload_url,
                headers=headers2,
                data=chunk_data
            )
            try:
                print('Upload Progress: {0}'.format(chunk_data_upload_status.json()['nextExpectedRanges']))
                # nextrange = chunk_data_upload_status.json()['nextExpectedRanges'][0]
            except:
                print(chunk_data_upload_status.json())
                input("2")
                
            counter += 1
            # print("uploading")