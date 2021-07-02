import pyodbc
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

cnxn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER=DESKTOP-FE1RJ78\SQLEXPRESS;DATABASE=UserDB"
)

app = Flask(__name__)
CORS(app)

# Root URL
@app.route("/", methods=["GET", "POST"])
def index():
    return jsonify({"Effat": "is Farting!!"})


@app.route("/api/getUserList", methods=["GET"])
def getUsers():
    data = []
    SQL = "select * from [User]"
    cursor = cnxn.cursor()
    cursor.execute(SQL)
    row = cursor.fetchall()
    print(row)
    for r in row:
        x = {
            "username": r[0],
            "email": r[1],
            "password": r[2],
            "gender": r[3],
            "dob": r[4],
        }
        data.append(x)

    # for r in row:
    #     data.append([x for x in r])  # or simply data.append(list(row))
    return jsonify(data)


@app.route("/api/getVotka", methods=["GET"])
def getVotka():
    data = []
    SQL = "select email, password from [User]"
    cursor = cnxn.cursor()
    cursor.execute(SQL)
    row = cursor.fetchall()
    for r in row:
        x = {
            "email": r[0],
            "password": r[1],
        }
        data.append(x)
    return jsonify(data)


@app.route("/api/postdata", methods=["POST"])
def dataPost():
    jsonData = request.get_json()
    print(jsonData)

    SQL = (
        "insert into [User] values ('"
        + jsonData["username"]
        + "', '"
        + jsonData["email"]
        + "', '"
        + jsonData["password"]
        + "', '"
        + jsonData["gender"]
        + "', '"
        + jsonData["dob"]
        + "');"
    )
    print(SQL)
    cursor = cnxn.cursor()
    cursor.execute(SQL)
    cnxn.commit()
    # for r in row:
    #     print(r)
    # print(row)
    return jsonify({"SUCCESS": "Data inserted"}, 200)


if __name__ == "__main__":
    app.run(debug=True)
