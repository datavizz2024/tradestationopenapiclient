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
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from openapi_client.models.advanced_options_definition import AdvancedOptionsDefinition
from openapi_client.models.order_confirm_request_definition_legs_inner import OrderConfirmRequestDefinitionLegsInner

class OrderRequestDefinition(BaseModel):
    """
    OrderRequestDefinition
    """
    account_key: StrictStr = Field(..., alias="AccountKey", description="Must be a valid Account Key for that user and Asset Type ")
    advanced_options: Optional[AdvancedOptionsDefinition] = Field(None, alias="AdvancedOptions")
    asset_type: StrictStr = Field(..., alias="AssetType")
    duration: StrictStr = Field(..., alias="Duration", description="Allowed durations vary by Asset Type * DAY - Day, valid until the end of the regular trading session. * DYP - Day Plus; valid until the end of the extended trading session * GTC - Good till canceled * GCP - Good till canceled plus * GTD - Good through date * GDP - Good through date plus * OPG - At the opening; only valid for listed stocks at the opening session Price * CLO - On Close; orders that target the closing session of an exchange. * IOC - Immediate or Cancel; filled immediately or canceled, partial fills are accepted * FOK - Fill or Kill; orders are filled entirely or canceled, partial fills are not accepted * 1 or 1 MIN - 1 minute; expires after the 1 minute * 3 or 3 MIN - 3 minutes; expires after the 3 minutes * 5 or 5 MIN - 5 minutes; expires after the 5 minutes ")
    gtd_date: Optional[constr(strict=True, max_length=10)] = Field(None, alias="GTDDate", description="Date that Order is valid through. Input Format: MM/DD/YYYY Required for orders with Duration = GTD. ")
    limit_price: Optional[StrictStr] = Field(None, alias="LimitPrice")
    stop_price: Optional[StrictStr] = Field(None, alias="StopPrice")
    order_confirm_id: Optional[constr(strict=True, max_length=25)] = Field(None, alias="OrderConfirmId", description="A unique identifier regarding an order used to prevent duplicates.  Must be unique per API key, per order, per user. ")
    order_type: StrictStr = Field(..., alias="OrderType")
    quantity: StrictStr = Field(..., alias="Quantity")
    route: Optional[StrictStr] = Field(None, alias="Route", description="The route of the order. For Stocks and Options, Route value will default to `Intelligent` if no value is set. Must be UPPERCASE. Routes can be obtained from [Retrieve Available Exchanges](#operation/getExchanges). ")
    symbol: StrictStr = Field(..., alias="Symbol", description="Must be UPPERCASE")
    trade_action: StrictStr = Field(..., alias="TradeAction", description="Conveys the intent of the trade * BUY - `equities` and `futures` * SELL - `equities` and `futures` * BUYTOCOVER - `equities` * SELLSHORT - `equities` * BUYTOOPEN - `options` * BUYTOCLOSE - `options` * SELLTOOPEN - `options` * SELLTOCLOSE - `options` ")
    osos: Optional[conlist(OrderRequestDefinitionOSOsInner, min_items=1, unique_items=True)] = Field(None, alias="OSOs")
    legs: Optional[conlist(OrderConfirmRequestDefinitionLegsInner, min_items=1, unique_items=True)] = Field(None, alias="Legs")
    __properties = ["AccountKey", "AdvancedOptions", "AssetType", "Duration", "GTDDate", "LimitPrice", "StopPrice", "OrderConfirmId", "OrderType", "Quantity", "Route", "Symbol", "TradeAction", "OSOs", "Legs"]

    @validator('asset_type')
    def asset_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('EQ', 'FU', 'OP'):
            raise ValueError("must be one of enum values ('EQ', 'FU', 'OP')")
        return value

    @validator('duration')
    def duration_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DAY', 'DYP', 'GTC', 'GCP', 'GTD', 'GDP', 'OPG', 'CLO', 'IOC', 'FOK', '1', '1 MIN', '3', '3 MIN', '5', '5 MIN'):
            raise ValueError("must be one of enum values ('DAY', 'DYP', 'GTC', 'GCP', 'GTD', 'GDP', 'OPG', 'CLO', 'IOC', 'FOK', '1', '1 MIN', '3', '3 MIN', '5', '5 MIN')")
        return value

    @validator('order_type')
    def order_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Limit', 'Market', 'StopLimit', 'StopMarket'):
            raise ValueError("must be one of enum values ('Limit', 'Market', 'StopLimit', 'StopMarket')")
        return value

    @validator('trade_action')
    def trade_action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('BUY', 'SELL', 'BUYTOCOVER', 'SELLSHORT', 'BUYTOOPEN', 'BUYTOCLOSE', 'SELLTOOPEN', 'SELLTOCLOSE'):
            raise ValueError("must be one of enum values ('BUY', 'SELL', 'BUYTOCOVER', 'SELLSHORT', 'BUYTOOPEN', 'BUYTOCLOSE', 'SELLTOOPEN', 'SELLTOCLOSE')")
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
    def from_json(cls, json_str: str) -> OrderRequestDefinition:
        """Create an instance of OrderRequestDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of advanced_options
        if self.advanced_options:
            _dict['AdvancedOptions'] = self.advanced_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in osos (list)
        _items = []
        if self.osos:
            for _item in self.osos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['OSOs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in legs (list)
        _items = []
        if self.legs:
            for _item in self.legs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Legs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderRequestDefinition:
        """Create an instance of OrderRequestDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderRequestDefinition.parse_obj(obj)

        _obj = OrderRequestDefinition.parse_obj({
            "account_key": obj.get("AccountKey"),
            "advanced_options": AdvancedOptionsDefinition.from_dict(obj.get("AdvancedOptions")) if obj.get("AdvancedOptions") is not None else None,
            "asset_type": obj.get("AssetType"),
            "duration": obj.get("Duration"),
            "gtd_date": obj.get("GTDDate"),
            "limit_price": obj.get("LimitPrice"),
            "stop_price": obj.get("StopPrice"),
            "order_confirm_id": obj.get("OrderConfirmId"),
            "order_type": obj.get("OrderType"),
            "quantity": obj.get("Quantity"),
            "route": obj.get("Route"),
            "symbol": obj.get("Symbol"),
            "trade_action": obj.get("TradeAction"),
            "osos": [OrderRequestDefinitionOSOsInner.from_dict(_item) for _item in obj.get("OSOs")] if obj.get("OSOs") is not None else None,
            "legs": [OrderConfirmRequestDefinitionLegsInner.from_dict(_item) for _item in obj.get("Legs")] if obj.get("Legs") is not None else None
        })
        return _obj

from openapi_client.models.order_request_definition_osos_inner import OrderRequestDefinitionOSOsInner
OrderRequestDefinition.update_forward_refs()

