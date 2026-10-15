"""Module for managing and analyzing dairy collection records."""

import hashlib
import subprocess
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE milk (id INTEGER PRIMARY KEY, farmer TEXT,"
    " litres REAL, fat REAL, day TEXT)"
    )


def record_milk(dconn, farmer, litres, fat, day):
    """Record a new milk collection entry for a farmer into the database."""
    dconn.execute(
        "INSERT INTO milk (farmer, litres, fat, day) VALUES (?, ?, ?, ?)",
        (farmer, litres, fat, day))
    dconn.commit()


def farmer_token(farmer):
    """Generate a secure SHA-256 token identifier for a given farmer."""
    return hashlib.sha256(farmer.encode()).hexdigest()


def daily_total(dconn, day):
    """Calculate the total litres of milk collected on a specific day."""
    rows = dconn.execute(
        "SELECT litres FROM milk WHERE day = ?",
        (day,)).fetchall()
    return f"Total: {sum(row[0] for row in rows):.1f} litres"


def top_farmer(dconn):
    """Identify the farmer with the highest total milk collection."""
    rows = dconn.execute(
        "SELECT farmer, SUM(litres) FROM milk GROUP BY farmer"
    ).fetchall()
    top = max(rows, key=lambda r: r[1])
    return top[0]


def print_slip(farmer):
    """Print a slip for the specified farmer using a subprocess call."""
    subprocess.run(["echo", f"printing slip for {farmer}"], check=True)


def low_fat(dconn):
    """Return a list of farmers whose milk fat content is below 3.5% or not recorded."""
    rows = dconn.execute(
        "SELECT farmer, fat FROM milk"
    ).fetchall()
    return [f for f, fat in rows if fat is None or fat < 3.5]


def main():
    """Main function to demonstrate the dairy collection functionalities."""
    record_milk(conn, "Gopal", 12.5, 4.1, "Mon")
    record_milk(conn, "Lata", 20.0, 3.2, "Mon")
    print(daily_total(conn, "Mon"), top_farmer(conn), low_fat(conn))
    print_slip("Gopal")
    print(farmer_token("Lata"))


main()
