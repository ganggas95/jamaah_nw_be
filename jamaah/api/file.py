"""Module API for file access"""
import os
import uuid
from flask.views import View
from flask import current_app as app
from flask import send_file
from flask_jwt_extended import jwt_required


class FileAPI(View):
    """Class API For file"""

    @jwt_required
    def dispatch_request(self, filename):
        """Handle request file access"""
        fileext = str(filename).split(".")
        full_filename = os.path.join(
            os.getcwd(),
            app.config["EXPORT_DIR_DATA"],
            filename)
        return send_file(full_filename,
                         as_attachment=True,
                         attachment_filename=f"{str(uuid.uuid1())}.{fileext[1]}")
