import os
import requests
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = '062b2682-c6b1-4a3e-b2b0-16d65261098e'
SCOPES = ['Files.ReadWrite']
access_token = generate_access_token(APP_ID, SCOPES)

file_list = ["./download/b.txt", "./download/윤가현-2022-07-06-aa5555.pdf", "./download/싸지방용/files.txt", "./download/문서/2021-2/#영상/디지털시스템및실험/1115-1 디시.mp4"]
for file_path in file_list:
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)


    if not os.path.exists(file_path):
        raise Exception(f'{file_name} is not found.')
    
    if file_size <= 400000000:
        # 400MB 이하
        with open(file_path, 'rb') as upload:
            print(1)
            media_content = upload.read()
        print(2)
        file_path = file_path[2:]

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
            'Content-Length': str(file_size),
            'Content-Range': f'bytes 0-{file_size-1}/{file_size}'
        }

        try:
            upload_url = response_upload_session.json()['uploadUrl']
            response_upload_status = requests.put(upload_url, headers=headers2, data=media_content)
            print(f'File: {file_path}')
            print(response_upload_status.reason)
            print(f'{file_path} 업로드 완료')

        except Exception as e:
            print(e, 'error')
            print(f'{file_path} 업로드 실패')

    else:
        
        # 400MB 초과
        with open(file_path, 'rb') as upload:
            file_path = file_path[2:]
            chunk_size = 327680
            chunk_number = file_size // chunk_size
            chunk_leftover = file_size - (chunk_size * chunk_number)
            counter = 0
            request_body = {
                'description' : 'a large file',
                'fileSystemInfo': { '@odata.type': 'microsoft.graph.fileSystemInfo' },
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

                headers = {
                    'Content-Type': 'application/json; charset=UTF-8',
                    'Content-Length': f'{chunk_size}',
                    'Content-Range': f'bytes {start_index}-{end_index-1}/{file_size}'
                }
                #upload session
                response_upload_session = requests.post(
                    GRAPH_API_ENDPOINT + f'/me/drive/items/root:/GDrive/{file_path}:/CreateUploadSession',
                    headers=headers,
                    json=request_body
                )
                print(response_upload_session)
                try:
                    upload_url = response_upload_session.json()['uploadUrl']
                    print(f'File: {file_path}')
                    print(f'{file_path} 업로드 완료')

                except Exception as e:
                    print(e, 'error')
                    print(f'{file_path} 업로드 실패')
                    break
                chunk_data_upload_status = requests.put(
                    upload_url,
                    headers=headers,
                    data=chunk_data
                )
                # print('Upload Progress: {0}'.format(chunk_data_upload_status.json()['nextExpectedRanges']))
                counter += 1
                print("uploading")

        # Cancel upload session
        # requests.delete(upload_url)

    
    
    # #4MB 이하
    # response = requests.put(
    #     GRAPH_API_ENDPOINT + f'/me/drive/items/root:/{file_path}:/content',
    #     headers=headers,
    #     data=media_content
    # )
    # print(response.json())