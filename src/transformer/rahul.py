from falcon import Request
from src.transformer.transformer import BaseTransformer


class RahulTransformer(BaseTransformer):

    def __init__(self, req: Request):
        self.req = req

    def transform(self, req, resp):
        # TODO write your own logic to generate the dynamic response
        return str({"RahulTransformer": "generate_dynamic_response" })
