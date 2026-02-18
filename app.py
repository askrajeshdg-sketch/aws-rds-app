from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to RDS
connection = pymysql.connect(
    host="database-1.czcwsme46up0.ap-southeast-1.rds.amazonaws.com",
    user="admin",
    password="rdsakil20078",
    database="school"
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
