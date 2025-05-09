# app.py
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS employees")
    c.execute(
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, password TEXT)"
    )
    c.executemany(
        "INSERT INTO employees (id, name, password) VALUES (?, ?, ?)",
        [(1, "Antonio", "1234"), (2, "Bruna", "admin"), (3, "Carlos", "letmein")],
    )
    conn.commit()
    conn.close()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    employee_id = request.form.get("employee_id", "")
    try:
        id_value = employee_id.split()[0]  # Simula o explode do PHP
        query = f"SELECT name FROM employees WHERE id = CAST({id_value} AS INT)"
        conn = sqlite3.connect("employees.db")
        c = conn.cursor()
        c.execute(query)
        result = c.fetchone()
        conn.close()
        name = result[0] if result else "Not found"
    except Exception as e:
        query = "Erro ao gerar a query"
        name = str(e)
    return render_template("index.html", result=name, query=query)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
