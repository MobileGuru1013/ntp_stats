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


class IssueTokenRequestMetadataRulesFeesItems(object):
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
        'address': 'str',
        'token_id': 'str',
        'value': 'str'
    }

    attribute_map = {
        'address': 'address',
        'token_id': 'tokenId',
        'value': 'value'
    }

    def __init__(self, address=None, token_id=None, value=None):  # noqa: E501
        """IssueTokenRequestMetadataRulesFeesItems - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._token_id = None
        self._value = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if token_id is not None:
            self.token_id = token_id
        if value is not None:
            self.value = value

    @property
    def address(self):
        """Gets the address of this IssueTokenRequestMetadataRulesFeesItems.  # noqa: E501

        Address fee is auto sent to  # noqa: E501

        :return: The address of this IssueTokenRequestMetadataRulesFeesItems.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IssueTokenRequestMetadataRulesFeesItems.

        Address fee is auto sent to  # noqa: E501

        :param address: The address of this IssueTokenRequestMetadataRulesFeesItems.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def token_id(self):
        """Gets the token_id of this IssueTokenRequestMetadataRulesFeesItems.  # noqa: E501

        How fee should be paid, either with a tokenId, or with NEBL if null  # noqa: E501

        :return: The token_id of this IssueTokenRequestMetadataRulesFeesItems.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this IssueTokenRequestMetadataRulesFeesItems.

        How fee should be paid, either with a tokenId, or with NEBL if null  # noqa: E501

        :param token_id: The token_id of this IssueTokenRequestMetadataRulesFeesItems.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    @property
    def value(self):
        """Gets the value of this IssueTokenRequestMetadataRulesFeesItems.  # noqa: E501

        Amount of NTP1 token, or NEBL (in satoshi) to pay as fee  # noqa: E501

        :return: The value of this IssueTokenRequestMetadataRulesFeesItems.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IssueTokenRequestMetadataRulesFeesItems.

        Amount of NTP1 token, or NEBL (in satoshi) to pay as fee  # noqa: E501

        :param value: The value of this IssueTokenRequestMetadataRulesFeesItems.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, IssueTokenRequestMetadataRulesFeesItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
