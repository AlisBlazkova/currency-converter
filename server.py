# Flask application extension
import connexion

# instance of the Flask application
app = connexion.App(__name__, specification_dir="./")

# creating the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
