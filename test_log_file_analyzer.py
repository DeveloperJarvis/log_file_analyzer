import unittest
from log_file_analyzer import LogParser, LogAnalyzer, APACHE_COMMON_LOG

class TestLogParser(unittest.TestCase):

    def setUp(self):
        self.parser = LogParser([APACHE_COMMON_LOG])
    
    def test_valid_log_line(self):
        line = (
            '127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] '
            '"GET /index.html HTTP/1.1" 200 123'
        )
        entry = self.parser.parse(line)
        self.assertIsNotNone(entry)
        self.assertEqual(entry.ip, "127.0.0.1")
        self.assertEqual(entry.path, "/index.html")
        self.assertEqual(entry.status, "200")
    
    def test_invalid_log_file(self):
        line = "INVLAID LOG LINE"
        entry = self.parser.parse(line)
        self.assertIsNone(entry)


class TestLogAnalyzer(unittest.TestCase):

    def test_analytics(self):
        analyzer = LogAnalyzer()
        analyzer.process(type(
            "E", (), {"ip": "1.1.1.1", "path": "/", "status": "200"}
            ))
        analyzer.process(type(
            "E", (), {"ip": "1.1.1.1", "path": "/", "status": "200"}
            ))
        analyzer.process(type(
            "E", (), {"ip": "2.2.2.2", "path": "/login", "status": "404"}
            ))
        
        self.assertEqual(analyzer.total_requests, 3)
        self.assertEqual(analyzer.ip_counter["1.1.1.1"], 2)
        self.assertEqual(analyzer.status_counter["404"], 1)


if __name__ == "__main__":
    unittest.main()
