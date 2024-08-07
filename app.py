from flask import Flask, request, jsonify

app = Flask(__name__)

current_greeting = "hello"
MAX_GREETING_LENGTH = 100


@app.route("/api/greeting", methods=["GET"])
def get_greeting():
    global current_greeting
    return jsonify({"greeting": current_greeting})


@app.route("/api/greeting", methods=["POST"])
def post_greeting():
    global current_greeting
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Bad Request", "message": "Invalid JSON format"}), 400

    if (
        "greeting" in data
        and data["greeting"].strip()
        and len(data["greeting"].strip()) <= MAX_GREETING_LENGTH
    ):
        current_greeting = data["greeting"].strip()
        return jsonify({"greeting": current_greeting}), 200
    else:
        return (
            jsonify(
                {
                    "error": "Bad Request",
                    "message": "Greeting is either missing, empty, or too long",
                }
            ),
            400,
        )


@app.errorhandler(404)
def not_found(error):
    return (
        jsonify(
            {
                "error": "Not Found",
                "message": "The requested URL was not found on the server",
            }
        ),
        404,
    )


@app.errorhandler(500)
def internal_error(error):
    return (
        jsonify(
            {
                "error": "Internal Server Error",
                "message": "An unexpected error occurred on the server",
            }
        ),
        500,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
