import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
	def test_eq2(self):
		node = TextNode("A text node", TextType.LINK, "https://www.boot.dev")
		node2 = TextNode("A text node", TextType.LINK, "https://www.youtube.com")
		self.assertNotEqual(node, node2)
	def test_eq3(self):
		node = TextNode("This is a text node", TextType.TEXT)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)
	def test_eq4(self):
		node = TextNode("A text node", TextType.LINK, "https://www.youtube.com")
		node2 = TextNode("A text node", TextType.LINK, "https://www.youtube.com")
		self.assertEqual(node, node2)
	def test_eq5(self):
		node = TextNode("This is a text node, but fancy", TextType.ITALIC)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)
	def test_eq6(self):
		node = TextNode("A text node", TextType.LINK, "https://www.boot.dev")
		node2 = TextNode("A text node", TextType.LINK, "https://www.boot.dev")
		self.assertEqual(node, node2)
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
	unittest.main()
