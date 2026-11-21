from flask import Flask, jsonify, request
app = Flask(__name__)

equipment = {
    101:{
        "id":101,
        "name":"Flight Control Unit",
        "type":"FCV",
        "status":"Operational"
    },
    102:{
        "id":102,
        "name":"Navigation System",
        "type":"NS",
        "status":"Operational"
    }
}

@app.get("/api/equipment/101")
def get_equipment():
    return jsonify(equipment[101]), 200
    #return jsonify(list(equipment.values())), 200

if __name__ == "__main__":
    app.run(debug=False, port=5000)