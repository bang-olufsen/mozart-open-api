# coding: utf-8

"""
Mozart platform API

API for interacting with the Mozart platform.

The version of the OpenAPI document: 0.2.0
Contact: support@bang-olufsen.dk
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import io
import re  # noqa: F401
import warnings

try:
    from pydantic.v1 import ValidationError, validate_arguments
except ImportError:
    from pydantic import ValidationError, validate_arguments

from typing import Awaitable, Optional, Union, overload

from typing_extensions import Annotated

try:
    from pydantic.v1 import Field, StrictStr
except ImportError:
    from pydantic import Field, StrictStr


from typing import Dict, Optional

from mozart_api.api_client import ApiClient
from mozart_api.api_response import ApiResponse
from mozart_api.exceptions import ApiTypeError, ApiValueError  # noqa: F401
from mozart_api.models.remote_menu_item import RemoteMenuItem
from mozart_api.models.remote_ui_key_state import RemoteUIKeyState


class RemoteApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    async def get_remote_menu(
        self,
        descendants_to: Annotated[
            Optional[StrictStr], Field(description="Get all descendants to this item")
        ] = None,
        **kwargs,
    ) -> Dict[str, RemoteMenuItem]:  # noqa: E501
        """Get all remote menu items  # noqa: E501


        :param descendants_to: Get all descendants to this item
        :type descendants_to: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Dict[str, RemoteMenuItem]
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_remote_menu_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.get_remote_menu_with_http_info(descendants_to, **kwargs)  # noqa: E501

    @validate_arguments
    async def get_remote_menu_with_http_info(
        self,
        descendants_to: Annotated[
            Optional[StrictStr], Field(description="Get all descendants to this item")
        ] = None,
        **kwargs,
    ) -> ApiResponse:  # noqa: E501
        """Get all remote menu items  # noqa: E501


        :param descendants_to: Get all descendants to this item
        :type descendants_to: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Dict[str, RemoteMenuItem], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["descendants_to"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_remote_menu" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("descendants_to") is not None:  # noqa: E501
            _query_params.append(("descendantsTo", _params["descendants_to"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            "200": "Dict[str, RemoteMenuItem]",
        }

        return await self.api_client.call_api(
            "/api/v1/remote",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    async def post_remote_key_trigger(
        self,
        id: Annotated[StrictStr, Field(..., description="Key identifier")],
        remote_ui_key_state: RemoteUIKeyState,
        **kwargs,
    ) -> None:  # noqa: E501
        """Remote input key press  # noqa: E501


        :param id: Key identifier (required)
        :type id: str
        :param remote_ui_key_state: (required)
        :type remote_ui_key_state: RemoteUIKeyState
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the post_remote_key_trigger_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.post_remote_key_trigger_with_http_info(
            id, remote_ui_key_state, **kwargs
        )  # noqa: E501

    @validate_arguments
    async def post_remote_key_trigger_with_http_info(
        self,
        id: Annotated[StrictStr, Field(..., description="Key identifier")],
        remote_ui_key_state: RemoteUIKeyState,
        **kwargs,
    ) -> ApiResponse:  # noqa: E501
        """Remote input key press  # noqa: E501


        :param id: Key identifier (required)
        :type id: str
        :param remote_ui_key_state: (required)
        :type remote_ui_key_state: RemoteUIKeyState
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = ["id", "remote_ui_key_state"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_remote_key_trigger" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["id"] is not None:
            _path_params["id"] = _params["id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["remote_ui_key_state"] is not None:
            _body_params = _params["remote_ui_key_state"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return await self.api_client.call_api(
            "/api/v1/remote/key/{id}/trigger",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    async def post_remote_trigger(
        self,
        id: Annotated[StrictStr, Field(..., description="Remote menu item ID")],
        **kwargs,
    ) -> None:  # noqa: E501
        """Trigger a remote menu item  # noqa: E501


        :param id: Remote menu item ID (required)
        :type id: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the post_remote_trigger_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.post_remote_trigger_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    async def post_remote_trigger_with_http_info(
        self,
        id: Annotated[StrictStr, Field(..., description="Remote menu item ID")],
        **kwargs,
    ) -> ApiResponse:  # noqa: E501
        """Trigger a remote menu item  # noqa: E501


        :param id: Remote menu item ID (required)
        :type id: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = ["id"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_remote_trigger" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["id"] is not None:
            _path_params["id"] = _params["id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return await self.api_client.call_api(
            "/api/v1/remote/{id}/trigger",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
