from app import app


@app.errorhandler(404)
def not_found_error(error):
    message = {
        "status_code": 404,
        "error_message": "Resource not found"
    }
    return message, 404


@app.errorhandler(500)
def internal_error(error):
    message = {
        "status_code": 500,
        "error_message": "Internal Error, resouce unavailable"
    }
    return message, 500
