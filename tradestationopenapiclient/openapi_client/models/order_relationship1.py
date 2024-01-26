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

class OrderRelationship1(BaseModel):
    """
    Describes the relationship between linked orders in a group and this order.
    """
    order_id: Optional[StrictStr] = Field(None, alias="OrderID", description="The order ID of the linked order.")
    relationship: Optional[StrictStr] = Field(None, alias="Relationship", description="Describes the relationship of a linked order within a group order to the current returned order. Valid Values are: `BRK`, `OSP` (linked parent), `OSO` (linked child), and `OCO`.")
    __properties = ["OrderID", "Relationship"]

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
    def from_json(cls, json_str: str) -> OrderRelationship1:
        """Create an instance of OrderRelationship1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderRelationship1:
        """Create an instance of OrderRelationship1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderRelationship1.parse_obj(obj)

        _obj = OrderRelationship1.parse_obj({
            "order_id": obj.get("OrderID"),
            "relationship": obj.get("Relationship")
        })
        return _obj

