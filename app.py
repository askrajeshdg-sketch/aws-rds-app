from flask import Flask, request, jsonify
import pymysql
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to RDS
connection = pymysql.connect(
    host=os.environ["DB_HOST"], 
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"]
)

@app.get("/student")
def get_student():
    name = request.args.get("name")

    cursor = connection.cursor()
    cursor.execute("SELECT score FROM students WHERE name=%s", (name,))
    row = cursor.fetchone()

    if row:
        return jsonify({"found": True, "score": row[0]})
    else:
        return jsonify({"found": False})

app.run(host="0.0.0.0", port=5000)


