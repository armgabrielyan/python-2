from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

	def draw(self):
		return 'I can draw a circle'


class Square(Shape):

	def draw(self):
		return 'I can draw a square'


class Triangle(Shape):

	def draw(self):
		return 'I can draw a triangle'


class ShapeFactory:
	SHAPES = {
		'circle': Circle,
		'square': Square,
		'triangle': Triangle,
	}


	@staticmethod
	def build(shape):
		return ShapeFactory.SHAPES[shape]()


class Client:

	@staticmethod
	def draw(shape):
		factory = ShapeFactory().build(shape)

		return factory.draw()


client = Client()
print(client.draw('square'))
