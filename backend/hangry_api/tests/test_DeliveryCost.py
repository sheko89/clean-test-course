from types import SimpleNamespace

from api.controllers import Delivery


def item(quantity):
  return SimpleNamespace(quantity=quantity)


def test_LotsOfItems():
  #Arrange
  order = [
    item(5),
    item(5),
    item(5),
  ]
  delivery_distance = 6
  #Act
  cost = Delivery.calculate(order, delivery_distance)
  #Assert
  assert cost == 7.5


def test_MiddleOfTheRoadItems():
  #Arrange
  order = [
    item(2),
    item(2),
    item(2),
  ]
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order, delivery_distance)
  #Assert
  assert cost == 5


def test_LittleItems():
  #Arrange
  order = [
    item(3),
    item(1),
  ]
  del_dist = 2
  #Act
  cost = Delivery.calculate(order, del_dist)
  #Assert
  assert cost == 3.50
