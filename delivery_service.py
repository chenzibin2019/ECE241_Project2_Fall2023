"""
UMass ECE 241 - Advanced Programming
Project 2 - Fall 2023
"""
import sys
from graph import Graph, Vertex
from priority_queue import PriorityQueue

class DeliveryService:
    def __init__(self) -> None:
        """
        Constructor of the Delivery Service class
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


    ## DO NOT MODIFY CODE BELOW!
    @staticmethod
    def nodeEdgeWeight(v):
        return sum([w for w in v.connectedTo.values()])

    @staticmethod
    def totalEdgeWeight(g):
        return sum([DeliveryService.nodeEdgeWeight(v) for v in g]) // 2

    @staticmethod
    def checkMST(g):
        for v in g:
            v.color = 'white'

        for v in g:
            if v.color == 'white' and not DeliveryService.DFS(g, v):
                return 'Your MST contains circles'
        return 'MST'

    @staticmethod
    def DFS(g, v):
        v.color = 'gray'
        for nextVertex in v.getConnections():
            if nextVertex.color == 'white':
                if not DeliveryService.DFS(g, nextVertex):
                    return False
            elif nextVertex.color == 'black':
                return False
        v.color = 'black'

        return True

# NO MORE TESTING CODE BELOW!
# TO TEST YOUR CODE, MODIFY test_delivery_service.py
