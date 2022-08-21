from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote.webelement import WebElement
from ui_test.ui_utils.action_mouse import ActionMouse
from typing import Literal
from functools import partial


class DragAndDrop(ActionMouse):
	def __init__(self, driver: webdriver):
		super().__init__(driver)
		self.url_page = "https://the-internet.herokuapp.com/drag_and_drop"

		self._block_a_id = "id=column-a"
		self._block_b_id = "id=column-b"

	def drag_and_drop_element(self, revers: bool = False, indent_px: int = 1,
							  block_deviation: Literal['LEFT', 'RIGHT', 'TOP', 'BOTTOM'] = None) -> bool:
		blocks_old = self._get_block_a_and_block_b(revers=revers)
		draggable_old, droppable_old = blocks_old

		drag_and_drop = partial(
			self.drag_and_drop, draggable_element=draggable_old, droppable_element=droppable_old
		)
		if block_deviation == "LEFT":
			# self.drag_and_drop(
			# 	draggable_element=draggable_old, droppable_element=droppable_old, by_offset=(-indent_px, 0)
			# )
			drag_and_drop(by_offset=(-indent_px, 0))
		elif block_deviation == "RIGHT":
			width = droppable_old.get_property("width")
			# self.drag_and_drop(
			# 	draggable_element=draggable_old, droppable_element=droppable_old, by_offset=(width + indent_px, 0)
			# )
			drag_and_drop(by_offset=(width + indent_px, 0))
		elif block_deviation == "TOP":
			# self.drag_and_drop(
			# 	draggable_element=draggable_old, droppable_element=droppable_old, by_offset=(0, -indent_px)
			# )
			drag_and_drop(by_offset=(0, -indent_px))
		elif block_deviation == "BOTTOM":
			height = droppable_old.get_property("height")
			# self.drag_and_drop(
			# 	draggable_element=draggable_old, droppable_element=droppable_old, by_offset=(0, height + indent_px)
			# )
			drag_and_drop(by_offset=(0, height + indent_px))
		else:
			# self.drag_and_drop(draggable_element=draggable_old, droppable_element=droppable_old)
			drag_and_drop()

		blocks_new = self._get_block_a_and_block_b(revers=revers)
		return [block.text for block in blocks_old] != [block.text for block in blocks_new]

	def _get_block_a_and_block_b(self, revers: bool = False) -> tuple[WebElement, WebElement]:
		blocks = (
			self.validate_web_element(self._block_a_id, clickable=True),
			self.validate_web_element(self._block_a_id, clickable=True)
		)
		return blocks[::-1] if revers else blocks
