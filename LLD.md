# 📘 Low-Level Design (LLD): Log File Analyzer

## 1. System Overview

The **Log File Analyzer** is a command-line utility that reads server log files (Apache/Nginx style), parses each log entry, extracts useful fields, and generates analytical statistics such as request counts, response code distribution, and most accessed endpoints.

The system processes logs **line-by-line** using **regular expressions** to ensure efficiency with large files.

---

## 2. Supported Log Format

Typical Apache / Nginx access log format:

```
127.0.0.1 - - [10/Oct/2023:13:55:36 +0000]
"GET /api/users HTTP/1.1" 200 1234
```

### Extracted Fields

- IP Address
- Timestamp
- HTTP Method
- Endpoint (URL path)
- HTTP Status Code
- Response Size (optional)

---

## 3. Core Components

### 3.1 LogEntry (Data Model)

**Responsibility:**
Represents a parsed log entry.

**Attributes:**

- `ip_address`
- `timestamp`
- `http_method`
- `endpoint`
- `status_code`
- `response_size`

**Purpose:**

- Acts as a structured container for parsed log data.
- Simplifies analytics processing.

---

### 3.2 LogParser

**Responsibility:**
Parses raw log lines using regular expressions.

**Attributes:**

- `log_pattern` (compiled regex)

**Methods:**

- `parse_line(line)`

  - Applies regex to a log line
  - Returns a `LogEntry` object if valid
  - Returns `None` if malformed

**Regex Responsibilities:**

- Capture IP address
- Capture HTTP method
- Capture endpoint
- Capture status code
- Handle malformed or partial log lines gracefully

---

### 3.3 LogReader

**Responsibility:**
Reads log files efficiently.

**Attributes:**

- `file_path`

**Methods:**

- `read_lines()`

  - Reads the file line-by-line
  - Passes each line to `LogParser`
  - Prevents loading entire file into memory

---

### 3.4 LogAnalyzer

**Responsibility:**
Performs analytics on parsed log entries.

**Attributes:**

- `ip_counter`
- `endpoint_counter`
- `status_code_counter`
- `total_requests`

**Methods:**

- `process_entry(log_entry)`
- `get_top_ips(n)`
- `get_top_endpoints(n)`
- `get_status_code_stats()`
- `get_total_requests()`

**Analytics Performed:**

- Number of requests per IP
- Most accessed endpoints
- Distribution of HTTP status codes
- Total request count

---

### 3.5 ReportGenerator

**Responsibility:**
Formats and displays analytics results.

**Methods:**

- `print_summary()`
- `print_top_ips()`
- `print_top_endpoints()`
- `print_status_codes()`

**Output:**

- Human-readable CLI reports
- Optional export to text or JSON

---

## 4. Data Flow

```text
Log File
   ↓
LogReader
   ↓
LogParser (regex)
   ↓
LogEntry
   ↓
LogAnalyzer
   ↓
ReportGenerator
```

---

## 5. Program Flow

1. User provides log file path
2. Log file opened and read line-by-line
3. Each line parsed using regex
4. Valid log entries sent to analyzer
5. Analyzer updates counters and stats
6. Summary report printed to CLI

---

## 6. Error Handling & Edge Cases

- Malformed log lines are skipped
- Empty lines ignored
- File not found → graceful exit
- Invalid regex match → counted as failed parse
- Very large files handled via streaming

---

## 7. Performance Considerations

- Line-by-line reading avoids memory overload
- Pre-compiled regex for efficiency
- Dictionary counters for O(1) updates
- Suitable for large log files (GB-scale)

---

## 8. Extensibility

Future enhancements:

- Time-based analytics (hourly/daily traffic)
- IP geolocation lookup
- User-agent parsing
- Multiple log format support
- Export to CSV / JSON
- Real-time log monitoring

---

## 9. CLI Example Output

```
Log Analysis Summary
--------------------
Total Requests: 12543

Top IPs:
1. 192.168.1.10 - 2450 requests
2. 10.0.0.5     - 1890 requests

Top Endpoints:
/api/login      - 3210
/api/users      - 2750

Status Codes:
200: 10234
404: 1450
500: 859
```

---

## 10. Skills Demonstrated

✔ Regular Expressions
✔ File I/O and streaming
✔ Data aggregation
✔ Error handling
✔ Clean architecture
✔ Interview-ready LLD

---

### 🎯 Interview One-Line Summary

> _A Python CLI tool that efficiently parses Apache/Nginx logs using regex, extracts structured data, and generates meaningful traffic and error statistics._
