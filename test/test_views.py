import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        self.assertTrue(", ".join(SUPPORTED) in rv.data)

    def test_msg_with_output_json(self):
        rv = self.app.get('/?output=json')
        self.assertEquals('{"imie": "Adrian", "mgs": "Hello World!"}', rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        a = '<greetings><name>Adrian</name>'
        b = '<msg>Hello World!</msg></greetings>'
        self.assertEquals(a + b, rv.data)

    def test_msg_with_output_name_json(self):
        rv = self.app.get('/?name=name&output=json')
        self.assertEquals('{"imie": "name", "mgs": "Hello World!"}', rv.data)

    def test_msg_with_output_name_xml(self):
        rv = self.app.get('/?name=name&output=xml')
        a = '<greetings><name>name</name>'
        b = '<msg>Hello World!</msg></greetings>'
        self.assertEquals(a + b, rv.data)
