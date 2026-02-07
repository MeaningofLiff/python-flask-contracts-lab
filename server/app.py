#!/usr/bin/env python3

#!/usr/bin/env python3

from flask import Flask, make_response
app = Flask(__name__)

# Data
contracts = [
    {
        "id": 1,
        "contract_information": "This contract is for John and building a shed"
    }
]

customers = ["bob", "bill", "john", "sarah"]


@app.get("/contract/<int:id>")
def get_contract(id):
    """
    Return contract info if found.
    200 → contract found, returns information
    404 → contract not found
    """
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract is None:
        return make_response("", 404)

    return make_response(contract["contract_information"], 200)


@app.get("/customer/<string:customer_name>")
def get_customer(customer_name):
    """
    Customer data is sensitive.
    204 → customer exists (no response body)
    404 → customer not found
    """
    if customer_name.lower() in customers:
        return ("", 204)

    return make_response("", 404)


if __name__ == "__main__":
    app.run(debug=True)
