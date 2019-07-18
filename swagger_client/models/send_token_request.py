# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.issue_token_request_metadata import IssueTokenRequestMetadata  # noqa: F401,E501
from swagger_client.models.send_token_request_to import SendTokenRequestTo  # noqa: F401,E501


class SendTokenRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fee': 'float',
        '_from': 'list[str]',
        'to': 'list[SendTokenRequestTo]',
        'metadata': 'IssueTokenRequestMetadata'
    }

    attribute_map = {
        'fee': 'fee',
        '_from': 'from',
        'to': 'to',
        'metadata': 'metadata'
    }

    def __init__(self, fee=None, _from=None, to=None, metadata=None):  # noqa: E501
        """SendTokenRequest - a model defined in Swagger"""  # noqa: E501

        self._fee = None
        self.__from = None
        self._to = None
        self._metadata = None
        self.discriminator = None

        self.fee = fee
        if _from is not None:
            self._from = _from
        self.to = to
        if metadata is not None:
            self.metadata = metadata

    @property
    def fee(self):
        """Gets the fee of this SendTokenRequest.  # noqa: E501

        Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL)  # noqa: E501

        :return: The fee of this SendTokenRequest.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this SendTokenRequest.

        Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL)  # noqa: E501

        :param fee: The fee of this SendTokenRequest.  # noqa: E501
        :type: float
        """
        if fee is None:
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

    @property
    def _from(self):
        """Gets the _from of this SendTokenRequest.  # noqa: E501

        Array of addresses to send the token from  # noqa: E501

        :return: The _from of this SendTokenRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendTokenRequest.

        Array of addresses to send the token from  # noqa: E501

        :param _from: The _from of this SendTokenRequest.  # noqa: E501
        :type: list[str]
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this SendTokenRequest.  # noqa: E501


        :return: The to of this SendTokenRequest.  # noqa: E501
        :rtype: list[SendTokenRequestTo]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendTokenRequest.


        :param to: The to of this SendTokenRequest.  # noqa: E501
        :type: list[SendTokenRequestTo]
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def metadata(self):
        """Gets the metadata of this SendTokenRequest.  # noqa: E501


        :return: The metadata of this SendTokenRequest.  # noqa: E501
        :rtype: IssueTokenRequestMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SendTokenRequest.


        :param metadata: The metadata of this SendTokenRequest.  # noqa: E501
        :type: IssueTokenRequestMetadata
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other