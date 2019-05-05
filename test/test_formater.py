from hello_world.formater import plain_text_upper_case
from hello_world.formater import plain_text_lower_case
from hello_world.formater import plain_text
from hello_world.formater import format_to_json
from hello_world.formater import format_to_xml
from hello_world.formater import get_formatted
import unittest


class TestFormater(unittest.TestCase):
    def setup(self):
        pass

    def test_get_formatted_1(self):
        r = get_formatted("msg", "imie", "plain")
        self.assertEqual(r, "imie msg")

    def test_get_formatted_2(self):
        r = get_formatted("msg", "imie", "plain_uppercase")
        self.assertEqual(r, "IMIE MSG")

    def test_get_formatted_3(self):
        r = get_formatted("MSG", "IMIE", "plain_lowercase")
        self.assertEqual(r, "imie msg")

    def test_get_formatted_4(self):
        r = get_formatted("msg", "imie", "json")
        self.assertEqual(r, '{"imie": "imie", "mgs": "msg"}')

    def test_get_formatted_5(self):
        r = get_formatted("msg", "imie", "xml")
        a = '<greetings><name>imie</name>'
        b = '<msg>msg</msg></greetings>'
        self.assertEquals(r, a + b)

    def test_plain_uppercase(self):
        r = plain_text_upper_case("WWimIE", "EEmsG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_lowercase(self):
        r = plain_text_lower_case("wwWImie", "eeeMSg")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.islower())
        self.assertTrue(msg.islower())

    def test_plain_text(self):
        r = plain_text("msg", "imie")
        self.assertEqual(r, "imie msg")

    def test_format_to_json(self):
        r = format_to_json("msg", "imie")
        self.assertEqual(r, '{"imie": "imie", "mgs": "msg"}')

    def test_format_to_xml(self):
        r = format_to_xml("msg", "imie")
        a = '<greetings><name>imie</name>'
        b = '<msg>msg</msg></greetings>'
        self.assertEquals(r, a + b)
