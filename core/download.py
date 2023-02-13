"""版本下载"""

import requests

from core import settings
from core import tools

def download_json(path, version):
    url=tools.render_str(settings.VERSION_API,version=version,type="json")
    print(url)
