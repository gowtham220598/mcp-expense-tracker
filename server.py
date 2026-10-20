
import sqlite3
from datetime import date
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Expense Tracker")
DB_PATH = Path(__file__).with_name("expenses.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT,
                expense_date TEXT NOT NULL
            )
        """)


@mcp.tool()
def add_expense(
    category: str,
    amount: float,
    description: str = ""
) -> str:
    """Save a new expense to the database."""
    if not category.strip():
        return "Error: Category cannot be empty."

    if not 0 < amount < float("inf"):
        return "Error: Amount must be a positive finite number."

    with get_connection() as conn:
        conn.execute(
            """INSERT INTO expenses
               (category, amount, description, expense_date)
               VALUES (?, ?, ?, ?)""",
            (category.strip(), amount, description,
             date.today().isoformat())
        )

    return f"Expense saved: {category} - Rs.{amount:.2f}"


@mcp.tool()
def monthly_total() -> str:
    """Calculate the total expenses for this month."""
    month = date.today().strftime("%Y-%m")

    with get_connection() as conn:
        total = conn.execute(
            """SELECT COALESCE(SUM(amount), 0)
               FROM expenses
               WHERE substr(expense_date, 1, 7) = ?""",
            (month,)
        ).fetchone()[0]

    return f"Total expense for {month}: Rs.{total:.2f}"


@mcp.tool()
def top_categories() -> str:
    """Show spending totals grouped by category."""
    month = date.today().strftime("%Y-%m")

    with get_connection() as conn:
        rows = conn.execute(
            """SELECT category, SUM(amount)
               FROM expenses
               WHERE substr(expense_date, 1, 7) = ?
               GROUP BY category
               ORDER BY SUM(amount) DESC""",
            (month,)
        ).fetchall()

    if not rows:
        return "No expenses found for this month."

    return "\n".join(
        f"{category}: Rs.{total:.2f}"
        for category, total in rows
    )


@mcp.resource("expenses://current-month")
def current_month_expenses() -> str:
    """Read all expenses recorded this month."""
    month = date.today().strftime("%Y-%m")

    with get_connection() as conn:
        rows = conn.execute(
            """SELECT expense_date, category, amount, description
               FROM expenses
               WHERE substr(expense_date, 1, 7) = ?
               ORDER BY id DESC""",
            (month,)
        ).fetchall()

    if not rows:
        return "No expenses this month."

    return "\n".join(
        f"{day} | {category} | Rs.{amount:.2f} | {desc}"
        for day, category, amount, desc in rows
    )


@mcp.prompt()
def budget_summary() -> str:
    """Generate instructions for a monthly budget review."""
    return (
        "Review my expenses for the current month. "
        "Use the available expense tools and resource. "
        "Explain total spending, top categories, "
        "and practical saving suggestions."
    )


if __name__ == "__main__":
    init_db()
    mcp.run()
