# Log File Analyzer

## Overview

**Log File Analyzer** is a Python-based command-line utility designed to read and analyze server log files such as **Apache** and **Nginx access logs**.
It extracts structured information from raw log entries and generates useful statistics including request counts, response codes, and popular endpoints.

The project demonstrates core backend skills such as **regular expressions**, **file parsing**, and **basic analytics**.

---

## Features

- Parses Apache/Nginx-style access logs
- Extracts:

  - Client IP addresses
  - Requested endpoints
  - HTTP response status codes

- Generates statistics:

  - Total request count
  - Requests per IP address
  - Most accessed endpoints
  - Status code distribution

- Efficient line-by-line file processing
- Graceful handling of malformed log entries

---

## Supported Log Format

Typical access log entry:

```
127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /api/users HTTP/1.1" 200 1234
```

### Extracted Fields

- IP address
- Timestamp
- HTTP method
- Endpoint
- Status code
- Response size (optional)

---

## Project Structure

```
log_file_analyzer/
│
├── log_file_analyzer.py
├── README.md
└── sample_logs/
    └── access.log
```

---

## Requirements

- Python 3.8 or higher
- No third-party dependencies (uses standard library only)

---

## Usage

1. Place your server log file in the project directory (or provide a path).
2. Run the analyzer from the command line:

   ```bash
   python log_file_analyzer.py <log_file_path>
   ```

3. View the generated statistics in the terminal output.

---

## Sample Output

```
Log Analysis Summary
-------------------
Total Requests: 12,543

Top IP Addresses:
192.168.1.10  - 2,450 requests
10.0.0.5      - 1,890 requests

Most Accessed Endpoints:
/api/login    - 3,210 requests
/api/users    - 2,750 requests

HTTP Status Codes:
200 - 10,234
404 - 1,450
500 - 859
```

---

## Design Highlights

- **Regex-based parsing** for flexible log format handling
- **Streaming file processing** to support large log files
- **Dictionary-based counters** for efficient analytics
- **Clear separation of concerns** (parsing, analysis, reporting)

---

## Error Handling

- Skips malformed or incomplete log lines
- Handles missing or empty log files gracefully
- Avoids loading entire files into memory

---

## Extensibility

Planned or possible enhancements:

- Time-based analytics (hourly/daily traffic)
- IP geolocation
- User-agent analysis
- Export reports to JSON or CSV
- Support for custom log formats
- Real-time log monitoring

---

## License

This project is licensed under the **GNU General Public License v3.0 or later**.
See the `LICENSE` file for details.

---

## Author

**Developer Jarvis (Pen Name)**
GitHub: [https://github.com/DeveloperJarvis](https://github.com/DeveloperJarvis)

---

## Interview Summary (One Line)

> A Python CLI tool that parses Apache/Nginx logs using regex and produces meaningful traffic and error statistics through efficient file processing.
