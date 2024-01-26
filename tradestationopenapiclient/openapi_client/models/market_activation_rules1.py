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
from pydantic import BaseModel, Field, StrictStr, validator

class MarketActivationRules1(BaseModel):
    """
    MarketActivationRules1
    """
    rule_type: Optional[StrictStr] = Field(None, alias="RuleType", description="Type of the activation rule. Currently only supports `Price`.")
    symbol: Optional[StrictStr] = Field(None, alias="Symbol", description="Symbol that the rule is based on.")
    predicate: Optional[StrictStr] = Field(None, alias="Predicate", description="The predicate comparison for the market rule type. E.g. `Lt` (less than). - `Lt` - Less Than - `Lte` - Less Than or Equal - `Gt` - Greater Than - `Gte` - Greater Than or Equal")
    trigger_key: Optional[StrictStr] = Field(None, alias="TriggerKey", description="The ticks behavior for the activation rule. Rule descriptions can be obtained from [Get Activation Triggers](#operation/GetActivationTriggers).")
    price: Optional[StrictStr] = Field(None, alias="Price", description="Valid only for RuleType=\"Price\", the price at which the rule will trigger when the price hits ticks as specified by TriggerKey.")
    logic_operator: Optional[StrictStr] = Field(None, alias="LogicOperator", description="Relation with the previous activation rule when given a list of MarketActivationRules. Ignored for the first MarketActivationRule.")
    __properties = ["RuleType", "Symbol", "Predicate", "TriggerKey", "Price", "LogicOperator"]

    @validator('trigger_key')
    def trigger_key_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('STT', 'STTN', 'SBA', 'SAB', 'DTT', 'DTTN', 'DBA', 'DAB', 'TTT', 'TTTN', 'TBA', 'TAB'):
            raise ValueError("must be one of enum values ('STT', 'STTN', 'SBA', 'SAB', 'DTT', 'DTTN', 'DBA', 'DAB', 'TTT', 'TTTN', 'TBA', 'TAB')")
        return value

    @validator('logic_operator')
    def logic_operator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('And', 'Or'):
            raise ValueError("must be one of enum values ('And', 'Or')")
        return value

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
    def from_json(cls, json_str: str) -> MarketActivationRules1:
        """Create an instance of MarketActivationRules1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MarketActivationRules1:
        """Create an instance of MarketActivationRules1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MarketActivationRules1.parse_obj(obj)

        _obj = MarketActivationRules1.parse_obj({
            "rule_type": obj.get("RuleType"),
            "symbol": obj.get("Symbol"),
            "predicate": obj.get("Predicate"),
            "trigger_key": obj.get("TriggerKey"),
            "price": obj.get("Price"),
            "logic_operator": obj.get("LogicOperator")
        })
        return _obj


