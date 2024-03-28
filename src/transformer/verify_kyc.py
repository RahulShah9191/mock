from falcon import Request


class VerifyKYCTransformer(object):

    def __init__(self, req: Request):
        self.req = req

    def generate_dynamic_response(self) -> str:
       # TODO write your own logic to generate the dynamic response
       return str({"VerifyKYCTransformer": "generate_dynamic_response" })