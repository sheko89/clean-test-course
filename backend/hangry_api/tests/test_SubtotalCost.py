from types import SimpleNamespace

from api.controllers import Subtotal


def order_item(quantity, price):
  return SimpleNamespace(quantity=quantity, item=SimpleNamespace(price=price))


def test_SimpleCost():
  #Arrange
  order = [
    order_item(5, 1.0),
    order_item(5, 1.0),
    order_item(5, 1.0),
  ]
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 15



def test_ComplexCost():
  #Arrange
  order = [
    order_item(2, 3.5),
    order_item(1, 4.5),
  ]
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 11.5
