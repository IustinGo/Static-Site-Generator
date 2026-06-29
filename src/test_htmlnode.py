import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
	def test_1(self):
		node = HTMLNode(tag="p", value="hello")
		result = node.props_to_html()
		self.assertEqual(result, "")
	def test_2(self):
		node = HTMLNode(tag="a", value="this is a website", props={"href": "https://www.boot.dev"})
		result = node.props_to_html()
		self.assertEqual(result, ' href="https://www.boot.dev"')
	def test_3(self):
		node = HTMLNode(tag="b", value="bold hello")
		result = node.props_to_html()
		self.assertEqual(result, "")

	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	def test_leaf_to_html_p2(self):
                node = LeafNode("b", "Hello, world but bold!")
                self.assertEqual(node.to_html(), "<b>Hello, world but bold!</b>")
	def test_leaf_to_html_p3(self):
                node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
                self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
		parent_node.to_html(),
		"<div><span><b>grandchild</b></span></div>",
		)

if __name__ == "__main__":
        unittest.main()
