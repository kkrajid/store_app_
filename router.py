# server/router.py

import re
from views import get_products, get_product, add_product
from urllib.parse import urlparse

urlpatterns = [
    ('GET', '/products', get_products),
    ('GET', r'/product/(\d+)', get_product),
    ('POST', '/product/add', add_product),
]

def handle_request(request_handler, method):
    parsed_path = urlparse(request_handler.path)
    for pattern_method, pattern_path, view_func in urlpatterns:
        if method == pattern_method:
            if pattern_path.startswith('^'):
                match = re.match(pattern_path, parsed_path.path)
                if match:
                    setattr(request_handler, 'url_args', match.groups())
                    view_func(request_handler)
                    return
            elif parsed_path.path == pattern_path:
                view_func(request_handler)
                return
    request_handler._send_response(404, {"error": "Not found"})
