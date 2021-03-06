# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EstimatedTime(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, longitud_inicial: float=None, latitud_inicial: float=None, longitud_final: float=None, latitud_final: float=None):  # noqa: E501
        """EstimatedTime - a model defined in Swagger

        :param longitud_inicial: The longitud_inicial of this EstimatedTime.  # noqa: E501
        :type longitud_inicial: int
        :param latitud_inicial: The latitud_inicial of this EstimatedTime.  # noqa: E501
        :type latitud_inicial: int
        :param longitud_final: The longitud_final of this EstimatedTime.  # noqa: E501
        :type longitud_final: int
        :param latitud_final: The latitud_final of this EstimatedTime.  # noqa: E501
        :type latitud_final: int
        """
        self.swagger_types = {
            'longitud_inicial': float,
            'latitud_inicial': float,
            'longitud_final': float,
            'latitud_final': float
        }

        self.attribute_map = {
            'longitud_inicial': 'longitud_inicial',
            'latitud_inicial': 'latitud_inicial',
            'longitud_final': 'longitud_final',
            'latitud_final': 'latitud_final'
        }

        self._longitud_inicial = longitud_inicial
        self._latitud_inicial = latitud_inicial
        self._longitud_final = longitud_final
        self._latitud_final = latitud_final

    @classmethod
    def from_dict(cls, dikt) -> 'EstimatedTime':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The estimated_time of this EstimatedTime.  # noqa: E501
        :rtype: EstimatedTime
        """
        return util.deserialize_model(dikt, cls)

    @property
    def longitud_inicial(self) -> float:
        """Gets the longitud_inicial of this EstimatedTime.


        :return: The longitud_inicial of this EstimatedTime.
        :rtype: int
        """
        return self._longitud_inicial

    @longitud_inicial.setter
    def longitud_inicial(self, longitud_inicial: float):
        """Sets the longitud_inicial of this EstimatedTime.


        :param longitud_inicial: The longitud_inicial of this EstimatedTime.
        :type longitud_inicial: int
        """

        self._longitud_inicial = longitud_inicial

    @property
    def latitud_inicial(self) -> float:
        """Gets the latitud_inicial of this EstimatedTime.


        :return: The latitud_inicial of this EstimatedTime.
        :rtype: int
        """
        return self._latitud_inicial

    @latitud_inicial.setter
    def latitud_inicial(self, latitud_inicial: float):
        """Sets the latitud_inicial of this EstimatedTime.


        :param latitud_inicial: The latitud_inicial of this EstimatedTime.
        :type latitud_inicial: int
        """

        self._latitud_inicial = latitud_inicial

    @property
    def longitud_final(self) -> float:
        """Gets the longitud_final of this EstimatedTime.


        :return: The longitud_final of this EstimatedTime.
        :rtype: int
        """
        return self._longitud_final

    @longitud_final.setter
    def longitud_final(self, longitud_final: float):
        """Sets the longitud_final of this EstimatedTime.


        :param longitud_final: The longitud_final of this EstimatedTime.
        :type longitud_final: int
        """

        self._longitud_final = longitud_final

    @property
    def latitud_final(self) -> float:
        """Gets the latitud_final of this EstimatedTime.


        :return: The latitud_final of this EstimatedTime.
        :rtype: int
        """
        return self._latitud_final

    @latitud_final.setter
    def latitud_final(self, latitud_final: float):
        """Sets the latitud_final of this EstimatedTime.


        :param latitud_final: The latitud_final of this EstimatedTime.
        :type latitud_final: int
        """

        self._latitud_final = latitud_final
