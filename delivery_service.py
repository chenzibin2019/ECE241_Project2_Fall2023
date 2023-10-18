"""
UMass ECE 241 - Advanced Programming
Project 2 - Fall 2023
"""

from graph import Graph, Vertex
from priority_queue import PriorityQueue

class DeliveryService:
    def __init__(self) -> None:
        """
        Constructor of the City class
        """
        self.city_map = None
        self.MST = None

    def buildMap(self, filename: str) -> None:
        """

        :param filename:
        :return:
        """
        pass

    def isWithinServiceRange(self, restaurant: int, user: int, threshold: int) -> bool:
        """

        :param restaurant:
        :param user:
        :param threshold:
        :return:
        """
        pass

    def buildMST(self, restaurant: int) -> bool:
        """

        :param restaurant:
        :return:
        """
        pass

    def minimalDeliveryTime(self, restaurant: int, user: int) -> int:
        """

        :param restaurant:
        :param user:
        :return:
        """
        pass

    def findDeliveryPath(self, restaurant: int, user: int) -> str:
        """

        :param restaurant:
        :param user:
        :return:
        """
        pass

    def findDeliveryPathWithDelay(self, restaurant: int, user: int, delay_info: dict[int, int]) -> str:
        """

        :param restaurant:
        :param user:
        :param delay_info:
        :return:
        """
        pass

# NO MORE TESTING CODE BELOW!
# TO TEST YOUR CODE, MODIFY test_delivery_service.py
