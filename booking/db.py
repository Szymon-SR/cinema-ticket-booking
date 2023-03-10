import sqlite3

import click
from flask import current_app, g

# TO BE USED ONLY TO GENERATE INITIAL DATABASE FILE

DATABASE_PATH = "booking/cinema_base.db"
TEST_DATABASE_PATH = "booking/test_base.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            DATABASE_PATH,
            detect_types=sqlite3.PARSE_DECLTYPES,
            connect_args={"check_same_thread": False},
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


def get_test_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            TEST_DATABASE_PATH,
            detect_types=sqlite3.PARSE_DECLTYPES,
            connect_args={"check_same_thread": False},
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def init_test_db():
    db = get_test_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
