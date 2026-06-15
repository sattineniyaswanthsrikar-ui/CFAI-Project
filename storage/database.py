import os
import sqlite3


class Database:

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        self.conn = sqlite3.connect(
            "data/parking.db"
        )

        self.cursor = self.conn.cursor()

        self.create_tables()

    # -------------------------
    # Create Tables
    # -------------------------

    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicles(
                vehicle_id TEXT PRIMARY KEY,
                length REAL,
                width REAL,
                priority TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS history(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicle_id TEXT,
                slot_id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.conn.commit()

    # -------------------------
    # Add Vehicle
    # -------------------------

    def add_vehicle(
            self,
            vehicle_id,
            length,
            width,
            priority):

        try:

            self.cursor.execute("""
                INSERT INTO vehicles
                VALUES(?,?,?,?)
            """,
            (
                vehicle_id,
                length,
                width,
                priority
            ))

            self.conn.commit()

        except sqlite3.IntegrityError:

            print(
                "\nVehicle ID already exists!"
            )

    # -------------------------
    # Remove Vehicle
    # -------------------------

    def remove_vehicle(
            self,
            vehicle_id):

        self.cursor.execute("""
            DELETE FROM vehicles
            WHERE vehicle_id = ?
        """,
        (
            vehicle_id,
        ))

        self.conn.commit()

        print(
            "\nVehicle Removed Successfully"
        )

    # -------------------------
    # View Vehicles
    # -------------------------

    def view_vehicles(self):

        self.cursor.execute("""
            SELECT *
            FROM vehicles
        """)

        return self.cursor.fetchall()

    # -------------------------
    # Add History
    # -------------------------

    def add_history(
            self,
            vehicle_id,
            slot_id):

        self.cursor.execute("""
            INSERT INTO history(
                vehicle_id,
                slot_id
            )
            VALUES (?,?)
        """,
        (
            vehicle_id,
            slot_id
        ))

        self.conn.commit()

    # -------------------------
    # View History
    # -------------------------

    def view_history(self):

        self.cursor.execute("""
            SELECT *
            FROM history
        """)

        return self.cursor.fetchall()

    # -------------------------
    # Reset Database
    # -------------------------

    def reset_database(self):

        self.cursor.execute(
            "DELETE FROM vehicles"
        )

        self.cursor.execute(
            "DELETE FROM history"
        )

        self.conn.commit()

        print(
            "\nDatabase Reset Successfully"
        )