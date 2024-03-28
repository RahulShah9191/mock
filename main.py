import falcon

from wsgiref.simple_server import make_server

import uvicorn

from src.service.mock import Mock
from src.service.route import Route

app = falcon.App()
class Healthcheck:

   def on_get(self, req, resp):
      """Handles GET requests"""
      resp.status = falcon.HTTP_200
      resp.content_type = falcon.MEDIA_TEXT
      resp.text = (
         'Mockserver is Running..'
      )

hello = Healthcheck()

app.add_route('/healthcheck', hello)

# if __name__ == '__main__':
#     # Running the Falcon application with Uvicorn server
#     uvicorn.run("falconUvicorn:app", host='0.0.0.0', port=8000, reload=True, workers=5)

if __name__ == '__main__':
    m = Mock()
    r = Route(m)
    app = r.add_route_to_app(app)
    with make_server('0.0.0.0', 8000, app) as httpd:
       print('Serving on port 8000...')
       httpd.serve_forever()
