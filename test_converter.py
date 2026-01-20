import unittest
from converter import KrutiDevConverter

class TestKrutiDevConverter(unittest.TestCase):
    def setUp(self):
        self.converter = KrutiDevConverter()

    def test_basic_conversion_kd_to_unicode(self):
        # "Hkkjr" -> "भारत" (Bharat)
        # Hk -> भ, k -> ा, j -> र, r -> त
        kruti_text = "Hkkjr"
        expected_unicode = "भारत"
        self.assertEqual(self.converter.convert_to_unicode(kruti_text), expected_unicode)

    def test_complex_conversion_kd_to_unicode(self):
        # "lkaLÑfrd" -> "सांस्कृतिक" (Sanskritic)
        # l -> स, k -> ा, a -> ं, L -> स्, Ñ -> कृ, f -> ि (repositioned), r -> त, d -> क
        # Kruti: lka L Ñ fr d
        # Unicode: स ा ं स् कृ ति क
        kruti_text = "lkaLÑfrd" 
        expected_unicode = "सांस्कृतिक"
        self.assertEqual(self.converter.convert_to_unicode(kruti_text), expected_unicode)

    def test_basic_conversion_unicode_to_kd(self):
        unicode_text = "भारत"
        expected_kruti = "Hkkjr"
        self.assertEqual(self.converter.convert_to_krutidev(unicode_text), expected_kruti)

    def test_reph_handling(self):
        # "dk;Z" -> "कार्य"
        # d -> क, k -> ा, ; -> य, Z -> र् (reph atop)
        kruti_text = "dk;Z"
        expected_unicode = "कार्य"
        self.assertEqual(self.converter.convert_to_unicode(kruti_text), expected_unicode)

if __name__ == '__main__':
    unittest.main()
