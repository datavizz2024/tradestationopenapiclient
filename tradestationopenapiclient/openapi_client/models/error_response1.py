# coding: utf-8

"""
    

    # Authentication For more information on authorization and gaining an access/refresh token, please visit: [Authentication](/docs/fundamentals/authentication/auth-overview). <SecurityDefinitions /> 

    The version of the OpenAPI document: 
    Contact: ClientServices@tradestation.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class ErrorResponse1(BaseModel):
    """
    Contains error details.
    """
    error: Optional[StrictStr] = Field(None, alias="Error", description="Error Title, can be any of `BadRequest`, `Unauthorized`, `NotFound`, `Forbidden`, `TooManyRequests`, `InternalServerError`, `NotImplemented`, `ServiceUnavailable`, or `GatewayTimeout`.")
    message: Optional[StrictStr] = Field(None, alias="Message", description="The description of the error.")
    __properties = ["Error", "Message"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ErrorResponse1:
        """Create an instance of ErrorResponse1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorResponse1:
        """Create an instance of ErrorResponse1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorResponse1.parse_obj(obj)

        _obj = ErrorResponse1.parse_obj({
            "error": obj.get("Error"),
            "message": obj.get("Message")
        })
        return _obj


