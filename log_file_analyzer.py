# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the log_file_analyzer Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# log_file_analyzer - Reads server logs (e.g. Apache/ Nginx-style logs).
#                   Extracts IPs, endpoints, response codes and statistics
#                   Skills: regex, file parsing, basic analytics
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# log_file_analyzer MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------

import re
import sys
from collections import Counter, defaultdict

# --------------------------------------------------
# regex patterns for different log formats
# --------------------------------------------------
# Could refer: https://www.w3schools.com/python/python_regex.asp
APACHE_COMMON_LOG = re.compile(
    r'(?P<ip>\S+) - - '
    r'\[(?P<time>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

APACHE_COMBINED_LOG = re.compile(
    r'(?P<ip>\S+) - - '
    r'\[(?P<time>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\S+)'
    r'"[^"]*" "[^"]*"'
)

# Nginx default access log is identical to Apache Commmon
NGINX_LOG = APACHE_COMMON_LOG

LOG_PATTERNS = [
    APACHE_COMBINED_LOG,
    APACHE_COMMON_LOG
]


# --------------------------------------------------
# log entry (data model)
# --------------------------------------------------
class LogEntry:
    def __init__(self, ip, path, status):
        self.ip = ip
        self.path = path
        self.status = status


# --------------------------------------------------
# log parser
# --------------------------------------------------
class LogParser:
    def __init__(self, patterns):
        self.patterns = patterns
    
    def parse(self, line):
        for pattern in self.patterns:
            match = pattern.search(line)
            if match:
                return LogEntry(
                    ip=match.group("ip"),
                    path=match.group("path"),
                    status=match.group("status")
                )
        return None


# --------------------------------------------------
# log analyzer
# --------------------------------------------------
class LogAnalyzer:
    def __init__(self):
        self.ip_counter = Counter()
        self.path_counter = Counter()
        self.status_counter = Counter()
        self.total_requests = 0
    
    def process(self, entry):
        self.total_requests += 1
        self.ip_counter[entry.ip] += 1
        self.path_counter[entry.path] += 1
        self.status_counter[entry.status] += 1
    
    def report(self, top_n=5):
        print("\nLog Analysis Summary")
        print("-" * 25)
        print(f"Total Requests: {self.total_requests}\n")

        print("Top IPs:")
        for ip, count in self.ip_counter.most_common(top_n):
            print(f"{ip:15} {count}")
        
        print("\nTop Endpoints:")
        for path, count in self.path_counter.most_common(top_n):
            print(f"{path:30} {count}")
        
        print("\nStatus Codes:")
        for status, count in self.status_counter.items():
            print(f"{status}: {count}")


# --------------------------------------------------
# main runner
# --------------------------------------------------
def analyze_log_file(file_path, line_based=True):
    parser = LogParser(LOG_PATTERNS)
    analyzer = LogAnalyzer()

    if line_based:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for chunk in iter(lambda: file.readlines(100_000), []):
                for line in chunk:
                    if not line.strip() or line.startswith('#'):
                        continue
                    entry = parser.parse(line)
                    if entry:
                        analyzer.process(entry)
    
    analyzer.report()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <log_file>")
        sys.exit(1)
    
    analyze_log_file(sys.argv[1])
