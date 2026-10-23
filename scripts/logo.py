import requests,zipfile,io
r=requests.get('https://download.moondroplab.com/6444df4c44144.zip');r.raise_for_status();z=zipfile.ZipFile(io.BytesIO(r.content));print(z.namelist());z.extractall('research/logo-kit')
