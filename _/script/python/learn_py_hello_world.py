
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node import Node

@gdclass
class learn_py_hello_world(Node):

	# define properties like this
	test_int: int = 5
	test_float: float = 5.2
	test_bool: bool = True
	test_vector: Vector3 = Vector3.new3(1,2,3)
	test_node_to_rotate: Node = None

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		
		print("Hello World")
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:

		if self.test_node_to_rotate:
			self.test_node_to_rotate.rotate_y(delta)


		pass
		# put dynamic code here

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
