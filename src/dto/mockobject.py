from typing import Optional
from pydantic import BaseModel

class MockRequest(BaseModel):
    method: str
    urlPathPattern: str

class MockResponse(BaseModel):
    headers: dict
    transformer: Optional[str]
    jsonBody: Optional[dict]
    fixedDelayMilliseconds: int
    status: int


class MockObject(BaseModel):
    request: MockRequest
    response: MockResponse


