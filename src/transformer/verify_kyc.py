from falcon import Request

from src.transformer.transformer import BaseTransformer


class VerifyKYCTransformer(BaseTransformer):

    def __init__(self, req: Request):
        self.req = req

    def transform(self):
        # TODO write your own logic to generate the dynamic response
        return str({"VerifyKYCTransformer": "generate_dynamic_response"})
