"""Module API for Task Manager"""
from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from jamaah.tasks.jamaah_tasks import JamaahTasks


class ReportTaskStatus(MethodView):
    """Class View to handle get task status"""
    @jwt_required
    def get(self, task_id):
        """Method to handle request get detail task by task_id"""
        report_task = JamaahTasks().AsyncResult(task_id)
        status = "pending"
        current = 0
        if report_task.state == 'PENDING':
            status = "pending"
        elif report_task.state == 'FAILURE':
            status = "failure"
        else:
            status = report_task.info
            current = 1
        return jsonify({
            "task_id": task_id,
            'state': report_task.state,
            "meta": {
                'current': current,
                'total': 1,
                'status': status  # this is the exception raised
            }
        })
