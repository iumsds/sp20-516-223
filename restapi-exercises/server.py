from flask import jsonify
import connexion

#Create a application instance
app = connexion.App(__name__, specification_dir="./")
#Read Yaml file to configure endpoints.
app.add_api("cpu.yaml")

#create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Its working!!!"}
    return jsonify(msg)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
