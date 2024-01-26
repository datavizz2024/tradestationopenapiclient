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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from openapi_client.models.order_confirm_response_leg import OrderConfirmResponseLeg
from openapi_client.models.order_confirm_response_time_in_force import OrderConfirmResponseTimeInForce
from openapi_client.models.trailing_stop import TrailingStop

class OrderConfirmResponse(BaseModel):
    """
    The response will also contain asset-specific fields.
    """
    account_currency: Optional[StrictStr] = Field(None, alias="AccountCurrency", description="The currency the account is traded in.")
    account_id: Optional[StrictStr] = Field(None, alias="AccountID", description="TradeStation Account ID.")
    add_liquidity: Optional[StrictBool] = Field(None, alias="AddLiquidity", description="This option allows you to place orders that will only add liquidity on the route you selected. To place an Add Liquidity order, the user must also select Book Only order type. Valid values `true` and `false`.  Valid for Equities only.")
    all_or_none: Optional[StrictBool] = Field(None, alias="AllOrNone", description="Use this advanced order feature when you do not want a partial fill. Your order will be filled in its entirety or not at all. Valid values `true` and `false`.  Valid for Equities and Options.")
    base_currency: Optional[StrictStr] = Field(None, alias="BaseCurrency", description="The base currency.")
    book_only: Optional[StrictBool] = Field(None, alias="BookOnly", description="This option restricts the destination you choose in the direct routing from re-routing your order to another destination. This type of order is useful in controlling your execution costs by avoiding fees the Exchanges can charge for rerouting your order to another market center. Valid values `true` and `false`.  Valid for Equities only.")
    counter_currency: Optional[StrictStr] = Field(None, alias="CounterCurrency", description="The counter currency.")
    currency: Optional[StrictStr] = Field(None, alias="Currency", description="The currency used in this transaction.")
    debit_credit_estimated_cost: Optional[StrictStr] = Field(None, alias="DebitCreditEstimatedCost", description="The actual cost for Market orders and orders with conditions, such as Trailing Stop or Activation Rule orders. Takes into account wheather or not the transaction will result in a debit or credit to the user.")
    discretionary_price: Optional[StrictStr] = Field(None, alias="DiscretionaryPrice", description="You can use this option to reflect a Bid/Ask at a lower/higher price than you are willing to pay using a specified price increment. Valid for `Limit` and `Stop Limit` orders only. Valid for Equities only.")
    estimated_commission: Optional[StrictStr] = Field(None, alias="EstimatedCommission", description="An estimated value that is calculated using the published TradeStation commission schedule. Equity and Futures Orders.")
    estimated_cost: Optional[StrictStr] = Field(None, alias="EstimatedCost", description="The actual cost for Market orders and orders with conditions, such as Trailing Stop or Activation Rule orders.")
    estimated_price: Optional[StrictStr] = Field(None, alias="EstimatedPrice", description="An estimated value that is calculated using current market information. The actual cost for Market orders and orders with conditions, such as Trailing Stop or Activation Rule orders, may differ significantly from this estimate.")
    initial_margin_display: Optional[StrictStr] = Field(None, alias="InitialMarginDisplay", description="Initial margin displayed for this transaction.")
    legs: Optional[conlist(OrderConfirmResponseLeg)] = Field(None, alias="Legs")
    limit_price: Optional[StrictStr] = Field(None, alias="LimitPrice", description="The limit price for Limit orders.")
    non_display: Optional[StrictBool] = Field(None, alias="NonDisplay", description="When you send a non-display order, it will not be reflected in either the Market Depth display or ECN books. Valid values `true` and `false`.  Valid for Equities only.")
    order_asset_category: Optional[StrictStr] = Field(None, alias="OrderAssetCategory", description="Indicates the category of the order.")
    order_confirm_id: Optional[StrictStr] = Field(None, alias="OrderConfirmID", description="Non-crypto orders only.  A unique identifier regarding an order used to prevent duplicates. Must be unique per API key, per order, per user.")
    peg_value: Optional[StrictStr] = Field(None, alias="PegValue", description="This order type is useful to achieve a fair price in a fast or volatile market. Valid values `BEST` and `MID`. Valid for Equities only.")
    product_currency: Optional[StrictStr] = Field(None, alias="ProductCurrency", description="The currency of the product.")
    route: Optional[StrictStr] = Field(None, alias="Route", description="The route of this transaction.")
    show_only_quantity: Optional[StrictInt] = Field(None, alias="ShowOnlyQuantity", description="Hides the true number of shares intended to be bought or sold. Valid for `Limit` and `StopLimit` order types. Not valid for all exchanges.")
    spread: Optional[StrictStr] = Field(None, alias="Spread", description="The option spread.")
    stop_price: Optional[StrictStr] = Field(None, alias="StopPrice", description="The stop price for open orders.")
    summary_message: Optional[StrictStr] = Field(None, alias="SummaryMessage", description="A summary message.")
    time_in_force: Optional[OrderConfirmResponseTimeInForce] = Field(None, alias="TimeInForce")
    trailing_stop: Optional[TrailingStop] = Field(None, alias="TrailingStop")
    underlying: Optional[StrictStr] = Field(None, alias="Underlying", description="Underlying symbol name.")
    __properties = ["AccountCurrency", "AccountID", "AddLiquidity", "AllOrNone", "BaseCurrency", "BookOnly", "CounterCurrency", "Currency", "DebitCreditEstimatedCost", "DiscretionaryPrice", "EstimatedCommission", "EstimatedCost", "EstimatedPrice", "InitialMarginDisplay", "Legs", "LimitPrice", "NonDisplay", "OrderAssetCategory", "OrderConfirmID", "PegValue", "ProductCurrency", "Route", "ShowOnlyQuantity", "Spread", "StopPrice", "SummaryMessage", "TimeInForce", "TrailingStop", "Underlying"]

    @validator('order_asset_category')
    def order_asset_category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('EQUITY', 'STOCKOPTION', 'FUTURE', 'CRYPTO'):
            raise ValueError("must be one of enum values ('EQUITY', 'STOCKOPTION', 'FUTURE', 'CRYPTO')")
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
    def from_json(cls, json_str: str) -> OrderConfirmResponse:
        """Create an instance of OrderConfirmResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in legs (list)
        _items = []
        if self.legs:
            for _item in self.legs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Legs'] = _items
        # override the default output from pydantic by calling `to_dict()` of time_in_force
        if self.time_in_force:
            _dict['TimeInForce'] = self.time_in_force.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trailing_stop
        if self.trailing_stop:
            _dict['TrailingStop'] = self.trailing_stop.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderConfirmResponse:
        """Create an instance of OrderConfirmResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderConfirmResponse.parse_obj(obj)

        _obj = OrderConfirmResponse.parse_obj({
            "account_currency": obj.get("AccountCurrency"),
            "account_id": obj.get("AccountID"),
            "add_liquidity": obj.get("AddLiquidity"),
            "all_or_none": obj.get("AllOrNone"),
            "base_currency": obj.get("BaseCurrency"),
            "book_only": obj.get("BookOnly"),
            "counter_currency": obj.get("CounterCurrency"),
            "currency": obj.get("Currency"),
            "debit_credit_estimated_cost": obj.get("DebitCreditEstimatedCost"),
            "discretionary_price": obj.get("DiscretionaryPrice"),
            "estimated_commission": obj.get("EstimatedCommission"),
            "estimated_cost": obj.get("EstimatedCost"),
            "estimated_price": obj.get("EstimatedPrice"),
            "initial_margin_display": obj.get("InitialMarginDisplay"),
            "legs": [OrderConfirmResponseLeg.from_dict(_item) for _item in obj.get("Legs")] if obj.get("Legs") is not None else None,
            "limit_price": obj.get("LimitPrice"),
            "non_display": obj.get("NonDisplay"),
            "order_asset_category": obj.get("OrderAssetCategory"),
            "order_confirm_id": obj.get("OrderConfirmID"),
            "peg_value": obj.get("PegValue"),
            "product_currency": obj.get("ProductCurrency"),
            "route": obj.get("Route"),
            "show_only_quantity": obj.get("ShowOnlyQuantity"),
            "spread": obj.get("Spread"),
            "stop_price": obj.get("StopPrice"),
            "summary_message": obj.get("SummaryMessage"),
            "time_in_force": OrderConfirmResponseTimeInForce.from_dict(obj.get("TimeInForce")) if obj.get("TimeInForce") is not None else None,
            "trailing_stop": TrailingStop.from_dict(obj.get("TrailingStop")) if obj.get("TrailingStop") is not None else None,
            "underlying": obj.get("Underlying")
        })
        return _obj


