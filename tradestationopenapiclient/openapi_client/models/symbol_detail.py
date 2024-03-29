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
from openapi_client.models.asset_type import AssetType
from openapi_client.models.price_format import PriceFormat
from openapi_client.models.quantity_format import QuantityFormat

class SymbolDetail(BaseModel):
    """
    SymbolDetail
    """
    asset_type: Optional[AssetType] = Field(None, alias="AssetType")
    country: Optional[StrictStr] = Field(None, alias="Country", description="The country of the exchange where the symbol is listed.")
    currency: Optional[StrictStr] = Field(None, alias="Currency", description="Displays the type of base currency for the selected symbol.")
    description: Optional[StrictStr] = Field(None, alias="Description", description="Displays the full name of the symbol, special characters may be formatted in unicode.")
    exchange: Optional[StrictStr] = Field(None, alias="Exchange", description="Name of exchange where this symbol is traded.")
    expiration_date: Optional[StrictStr] = Field(None, alias="ExpirationDate", description="The UTC formatted expiration date of a future or option symbol, in the country the contract is traded in. The time portion of the value should be ignored.")
    future_type: Optional[StrictStr] = Field(None, alias="FutureType", description="Displays the type of future contract the symbol represents, futures only.")
    option_type: Optional[StrictStr] = Field(None, alias="OptionType", description="Defines whether an option is a call or a put. Valid values are `CALL` and `PUT`.")
    price_format: Optional[PriceFormat] = Field(None, alias="PriceFormat")
    quantity_format: Optional[QuantityFormat] = Field(None, alias="QuantityFormat")
    root: Optional[StrictStr] = Field(None, alias="Root", description="Displays the symbol root, e.g. `ES` for Futures symbol `@ESH21`, `OEX` for IndexOption `OEX 210129C1750`, and `AAPL` for StockOption `AAPL 210129C137`.")
    strike_price: Optional[StrictStr] = Field(None, alias="StrikePrice", description="For an Option symbol, the Strike Price for the Put or Call.")
    symbol: Optional[StrictStr] = Field(None, alias="Symbol", description="The Symbol name or abbreviation.")
    underlying: Optional[StrictStr] = Field(None, alias="Underlying", description="The financial instrument on which an Options contract is based or derived. Can also apply to some Futures symbols, like continuous Futures contracts, e.g. `ESH21` for `@ES`.")
    __properties = ["AssetType", "Country", "Currency", "Description", "Exchange", "ExpirationDate", "FutureType", "OptionType", "PriceFormat", "QuantityFormat", "Root", "StrikePrice", "Symbol", "Underlying"]

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
    def from_json(cls, json_str: str) -> SymbolDetail:
        """Create an instance of SymbolDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of price_format
        if self.price_format:
            _dict['PriceFormat'] = self.price_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quantity_format
        if self.quantity_format:
            _dict['QuantityFormat'] = self.quantity_format.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SymbolDetail:
        """Create an instance of SymbolDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SymbolDetail.parse_obj(obj)

        _obj = SymbolDetail.parse_obj({
            "asset_type": obj.get("AssetType"),
            "country": obj.get("Country"),
            "currency": obj.get("Currency"),
            "description": obj.get("Description"),
            "exchange": obj.get("Exchange"),
            "expiration_date": obj.get("ExpirationDate"),
            "future_type": obj.get("FutureType"),
            "option_type": obj.get("OptionType"),
            "price_format": PriceFormat.from_dict(obj.get("PriceFormat")) if obj.get("PriceFormat") is not None else None,
            "quantity_format": QuantityFormat.from_dict(obj.get("QuantityFormat")) if obj.get("QuantityFormat") is not None else None,
            "root": obj.get("Root"),
            "strike_price": obj.get("StrikePrice"),
            "symbol": obj.get("Symbol"),
            "underlying": obj.get("Underlying")
        })
        return _obj


