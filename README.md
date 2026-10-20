# MCP Expense Tracker

**A Python-based Expense Tracker MCP Server using FastMCP, SQLite, and Model Context Protocol (MCP).

## Project Overview

MCP Expense Tracker is a Python application that enables AI assistants to manage and analyze expense records using the Model Context Protocol.

The application stores expenses in an SQLite database and provides MCP tools for adding expenses, calculating monthly totals, and analyzing spending categories.

The MCP server is integrated with VS Code GitHub Copilot Chat and tested using MCP Inspector.

## Technologies Used

- **Python 3.11** — Backend programming
- **FastMCP** — MCP server implementation
- **MCP Python SDK 1.x** — Model Context Protocol integration
- **SQLite** — Local expense database
- **Pytest** — Automated testing
- **VS Code** — Development environment
- **GitHub Copilot Chat** — AI tool integration
- **MCP Inspector** — MCP server testing
- **Git & GitHub** — Version control

## Features

### 1. MCP Tools

**add_expense**

Adds a new expense to the SQLite database.

Inputs:
- Category
- Amount
- Description

Example:

```text
Category: Food
Amount: 150
Description: Lunch
```

Output:

```text
Expense saved: Food - Rs.150.00
```

**monthly_total**

Calculates the total expenses for the current month.

Example output:

```text
Total expense for 2026-10: Rs.350.00
```

*The amount above is an example. Actual results depend on database records.*

**top_categories**

Displays category-wise spending totals in descending order.

Example output:

```text
Shopping: Rs.500.00
Travel: Rs.200.00
Food: Rs.150.00
```

### 2. MCP Resource

**expenses://current-month**

Provides access to all expenses recorded during the current month.

### 3. MCP Prompt

**budget_summary**

Provides instructions to an AI assistant for reviewing monthly expenses and suggesting ways to save money.

## Project Structure

```text
mcp-expense-tracker/
│
├── server.py
├── test_server.py
├── requirements.txt
├── README.md
├── .gitignore
├── .vscode/
│   └── mcp.json
└── expenses.db
```

The virtual environment, database, and local MCP configuration are excluded from GitHub.

## Installation Guide

### Step 1 — Clone Repository

```bash
git clone https://github.com/gowtham220598/mcp-expense-tracker.git
cd mcp-expense-tracker
```

### Step 2 — Create Virtual Environment

```powershell
py -3.11 -m venv .venv
```

### Step 3 — Install Dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Step 4 — Verify MCP Installation

```powershell
.\.venv\Scripts\python.exe -c "from mcp.server.fastmcp import FastMCP; print('MCP SUCCESS')"
```

Expected output:

```text
MCP SUCCESS
```

## MCP Inspector Testing

Node.js and npm are required.

Run:

```powershell
npx @modelcontextprotocol/inspector .\.venv\Scripts\python.exe server.py
```

Use MCP Inspector to verify:

- Three MCP tools
- One MCP resource
- One MCP prompt
- Input validation
- Correct database operations

## VS Code AI Integration

Create a file named `.vscode/mcp.json` and configure the MCP server.

Example:

```json
{
  "servers": {
    "expense-tracker": {
      "type": "stdio",
      "command": "C:\\PATH\\TO\\mcp-expense-tracker\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\PATH\\TO\\mcp-expense-tracker\\server.py"
      ]
    }
  }
}
```

Replace the example paths with the actual paths on your computer.

Open GitHub Copilot Chat in Agent mode, enable the MCP tools, and interact with the expense tracker using natural language.

## Example AI Prompts

**Add an expense**

```text
Add Rs.150 for Food with description Lunch.
```

**Monthly expense report**

```text
Calculate my total expenses for the current month.
```

**Category analysis**

```text
Show my top spending categories.
```

**Multiple tool analysis**

```text
Use monthly_total and top_categories to analyze my expenses and suggest three ways to save money.
```

## Automated Testing

The project includes five automated tests using Pytest.

| Test Case | Result |
|---|---|
| Add a valid expense | Passed |
| Reject a negative amount | Passed |
| Reject an empty category | Passed |
| Calculate monthly total | Passed |
| Display top categories | Passed |

Run the tests:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

**Verified result: 5 tests passed.**

## Input Validation

The application validates expense data before saving it.

For example, a negative amount returns:

```text
Error: Amount must be a positive finite number.
```

An empty category returns:

```text
Error: Category cannot be empty.
```

## Database

SQLite is used for local data storage.

Each expense record contains:

- Expense ID
- Category
- Amount
- Description
- Expense date

The database file is generated locally and is not committed to GitHub.

## Future Enhancements

- Update and delete expenses
- Date-based expense filtering
- Monthly budget limits
- Expense charts and dashboards
- PDF and Excel reports
- User authentication
- Cloud database integration

## Conclusion

The MCP Expense Tracker demonstrates how Python applications can expose tools, resources, and prompts to AI assistants using the Model Context Protocol.

The project combines MCP server development, SQLite database operations, AI integration, input validation, and automated testing.

## GitHub Repository

https://github.com/gowtham220598/mcp-expense-tracker

## Author

**MCP Internship Project**

Developed using Python, FastMCP, and SQLite.