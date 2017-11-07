import requests
c4c_url = 'https://my500248.c4c.saphybriscloud.cn'
custom_header = {'X-CSRF-TOKEN':'Fetch', 'Authorization':'Basic eXMxMDA5OldlbGNvbWUy'}
request_url = c4c_url+'/sap/c4c/odata/v1/c4codata/$metadata'
response = requests.get(request_url, headers = custom_header)
x_csrf_token = response.headers.get('x-csrf-token')
print(x_csrf_token)
