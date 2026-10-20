
import sqlite3

import pytest
import server


@pytest.fixture
def test_database(tmp_path, monkeypatch):
    # ஒவ்வொரு test-க்கும் தனி temporary database
    db_path = tmp_path / "test_expenses.db"

    monkeypatch.setattr(server, "DB_PATH", db_path)
    server.init_db()

    return db_path


def test_add_expense(test_database):
    result = server.add_expense(
        category="Food",
        amount=150,
        description="Lunch"
    )

    assert "Expense saved" in result

    with sqlite3.connect(test_database) as conn:
        count = conn.execute(
            "SELECT COUNT(*) FROM expenses"
        ).fetchone()[0]

    assert count == 1


def test_negative_amount(test_database):
    result = server.add_expense(
        category="Food",
        amount=-100
    )

    assert "Error" in result

    with sqlite3.connect(test_database) as conn:
        count = conn.execute(
            "SELECT COUNT(*) FROM expenses"
        ).fetchone()[0]

    assert count == 0


def test_empty_category(test_database):
    result = server.add_expense(
        category="",
        amount=100
    )

    assert "Error" in result


def test_monthly_total(test_database):
    server.add_expense("Food", 150)
    server.add_expense("Travel", 200)

    result = server.monthly_total()

    assert "350.00" in result


def test_top_categories(test_database):
    server.add_expense("Food", 150)
    server.add_expense("Travel", 200)

    result = server.top_categories()

    assert "Food" in result
    assert "Travel" in result
