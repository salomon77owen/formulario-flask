from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Crear la tabla si no existe
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            edad INTEGER
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        edad = request.form["edad"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, apellido, edad) VALUES (?, ?, ?)",
                       (nombre, apellido, edad))
        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("index.html")

#if __name__ == "__main__":
 #   init_db()
  #  app.run(debug=True)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
else:
    # Esto se ejecuta en Render
    init_db()
