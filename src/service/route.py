import inspect
import time
import importlib
import os
from http.client import HTTPException

import falcon

from src.dto.mockobject import MockObject
from src.service.mock import Mock
from falcon import Request, Response



class RouteResponse(object):

    def __init__(self, mock_object: MockObject):
        self.mock_object  = mock_object


    def get_classes_in_package(self, package_name):
        classes = []
        package_path = importlib.util.find_spec(package_name).submodule_search_locations[0]
        for root, _, files in os.walk(package_path):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    module_name = os.path.splitext(file)[0]
                    module = importlib.import_module(package_name + '.' + module_name)
                    for name, obj in inspect.getmembers(module):
                        if inspect.isclass(obj) and obj.__name__.endswith('Transformer'):
                            classes.append(obj)
        return classes


    def __wait_for_fixed_delay(self):
        if self.mock_object.response.fixedDelayMilliseconds and self.mock_object.response.fixedDelayMilliseconds > 0:
            time.sleep(self.mock_object.response.fixedDelayMilliseconds/1000)

    def __generate_dynamic_response(self, req: Request, mock_object: MockObject) -> str:
        transformers = self.get_classes_in_package("src.transformer")
        transformer_class = mock_object.response.transformer
        for transformer in transformers:
            if transformer.__name__ == mock_object.response.transformer:
                response = transformer(req).generate_dynamic_response()
                return response
        raise HTTPException(f"Transformer class {transformer_class} not found in the package")

    def on_get(self, req: Request, resp: Response):
        """Handles GET requests"""
        if self.mock_object.request.method != "GET":
            raise falcon.HTTPNotFound(
                title="Method not supported",
                description="GET method not supported for this route"
            )
        resp.status = self.mock_object.response.status
        resp.set_headers(self.mock_object.response.headers)
        # wait for fixed delay for the response
        self.__wait_for_fixed_delay()
        # generating response
        if self.mock_object.response.jsonBody:
            resp.text = str(self.mock_object.response.jsonBody)
        elif self.mock_object.response.transformer:
            resp.text = self.__generate_dynamic_response(req, self.mock_object)


    def on_post(self, req: Request, resp: Response):
        if self.mock_object.request.method != "POST":
            raise falcon.HTTPNotFound(
                title="Method not supported",
                description="POST method not supported for this route"
            )
        """Handles POST requests"""
        resp.status = self.mock_object.response.status
        resp.set_headers(self.mock_object.response.headers)
        # wait for fixed delay for the response
        self.__wait_for_fixed_delay()
        # generating response
        if self.mock_object.response.jsonBody:
            resp.text = str(self.mock_object.response.jsonBody)
        elif self.mock_object.response.transformer:
            resp.text = self.__generate_dynamic_response(req, self.mock_object)


    def on_delete(self, req: Request, resp: Response):
        if self.mock_object.request.method != "DELETE":
            raise falcon.HTTPNotFound(
                title="Method not supported",
                description="POST method not supported for this route"
            )
        """Handles DELETE requests"""
        resp.status = self.mock_object.response.status
        resp.set_headers(self.mock_object.response.headers)
        # wait for fixed delay for the response
        self.__wait_for_fixed_delay()
        # generating response
        if self.mock_object.response.jsonBody:
            resp.text = str(self.mock_object.response.jsonBody)
        elif self.mock_object.response.transformer:
            resp.text = self.__generate_dynamic_response(req, self.mock_object)


    def on_patch(self, req: Request, resp: Response):
        if self.mock_object.request.method != "DELETE":
            raise falcon.HTTPNotFound(
                title="Method not supported",
                description="POST method not supported for this route"
            )
        """Handles PATCH requests"""
        resp.status = self.mock_object.response.status
        resp.set_headers(self.mock_object.response.headers)
        # wait for fixed delay for the response
        self.__wait_for_fixed_delay()
        # generating response
        if self.mock_object.response.jsonBody:
            resp.text = str(self.mock_object.response.jsonBody)
        elif self.mock_object.response.transformer:
            resp.text = self.__generate_dynamic_response(req, self.mock_object)



    def on_put(self, req: Request, resp: Response):
        if self.mock_object.request.method != "DELETE":
            raise falcon.HTTPNotFound(
                title="Method not supported",
                description="POST method not supported for this route"
            )
        """Handles PUT requests"""
        resp.status = self.mock_object.response.status
        resp.set_headers(self.mock_object.response.headers)
        # wait for fixed delay for the response
        self.__wait_for_fixed_delay()
        # generating response
        if self.mock_object.response.jsonBody:
            resp.text = str(self.mock_object.response.jsonBody)
        elif self.mock_object.response.transformer:
            resp.text = self.__generate_dynamic_response(req, self.mock_object)


class Route(object):

    def __init__(self, mock: Mock):
        self.mock = mock

    def add_route_to_app(self, app):
        if self.mock:
            for obj in self.mock.mock_obj:
                route_response_obj = RouteResponse(obj)
                app.add_route(obj.request.urlPathPattern, route_response_obj)
        return app

