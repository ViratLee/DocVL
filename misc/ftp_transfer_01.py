import shutil
import urllib.request as request
from contextlib import closing
#ftp://username:password@server/path/to
with closing(request.urlopen('sftp://bsnpeid:gq/n7HC=@thadcplwcm13:22/logs/wcmapp13/SystemErr_19.07.09_23.00.00.log')) as r:
    with open('file', 'wb') as f:
        shutil.copyfileobj(r, f)