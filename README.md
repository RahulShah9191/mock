# mock
Mock API server for testing and prototyping

Add Mocks in the `resource.mocks` directory. Each mock should be a JSON file with the following structure:

```json
{
  "request": {
    "method": "GET",
    "urlPathPattern": "/requestCount"
  },
  "response": {
    "headers": {
      "Content-Type": "application/json"
    },
    "fixedDelayMilliseconds": 0,
    "jsonBody": {
      "requestCount": 0
    },
    "status": 200
  }
}
```
- `request.method`: The HTTP method of the request.
- `request.urlPathPattern`: The URL path pattern of the request.
- `response.headers`: The headers of the response.
- `response.fixedDelayMilliseconds`: The delay in milliseconds before the response is sent.
- `response.jsonBody`: The JSON body of the response, this will be supply the static response.
- `response.status`: The HTTP status code of the response.

To generate the dynamic response, you can use the following placeholders in the `response.transformers` 
```json
{
  "request": {
    "method": "POST",
    "urlPathPattern": "/api/kyc"
  },
  "response": {
    "headers": {
      "Content-Type": "application/json"
    },
    "transformer": "VerifyKYCTransformer",
    "fixedDelayMilliseconds": "5",
    "status": 201
  }
}
```
- `response.transformer`: The name of the transformer class that will generate the dynamic response. User has to implement the transformer class in the `src.transformers` directory.

To run the server, execute the following command:
```bash
    bash start.sh
