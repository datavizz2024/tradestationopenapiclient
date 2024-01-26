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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.historical_order import HistoricalOrder
from openapi_client.models.order_error import OrderError

class HistoricalOrders(BaseModel):
    """
    Orders contains a collection of recent or historical orders for the requested account.
    """
    orders: Optional[conlist(HistoricalOrder)] = Field(None, alias="Orders")
    errors: Optional[conlist(OrderError)] = Field(None, alias="Errors")
    next_token: Optional[StrictStr] = Field(None, alias="NextToken", description="A token returned with paginated orders which can be used in a subsequent request to retrieve the next page.")
    __properties = ["Orders", "Errors", "NextToken"]

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
    def from_json(cls, json_str: str) -> HistoricalOrders:
        """Create an instance of HistoricalOrders from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in orders (list)
        _items = []
        if self.orders:
            for _item in self.orders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Orders'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HistoricalOrders:
        """Create an instance of HistoricalOrders from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HistoricalOrders.parse_obj(obj)

        _obj = HistoricalOrders.parse_obj({
            "orders": [HistoricalOrder.from_dict(_item) for _item in obj.get("Orders")] if obj.get("Orders") is not None else None,
            "errors": [OrderError.from_dict(_item) for _item in obj.get("Errors")] if obj.get("Errors") is not None else None,
            "next_token": obj.get("NextToken")
        })
        return _obj


