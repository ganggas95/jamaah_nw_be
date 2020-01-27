from flask import Flask
from jamaah.api.auth import AuthAPI
from jamaah.api.wilayah import (
    ProvinsiAPI,
    KabupatenAPI,
    KecamatanAPI,
    DesaAPI)
from jamaah.api.jamaah import (
    JamaahListAPI,
    DetailJamaahAPI,
    ReportDataAPI,
)
from jamaah.api.users import (
    UserListAPI,
    DetailUserAPI,
    ProfileChangePasswordAPI,
    ResetPasswordAPI,
    ToggleStatusAPI,
    ProfileUserAPI,
)
from jamaah.api.tasks import ReportTaskStatus
from jamaah.api.file import FileAPI


def login_url(app: Flask):
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/login",
        view_func=AuthAPI.as_view("auth_api"),
        methods=["POST"]
    )
    return app


def wilayah_url(app: Flask):
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/wilayah/provinsi",
        view_func=ProvinsiAPI.as_view("provinsi_api"), methods=["GET"])
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/wilayah/kabupaten",
        view_func=KabupatenAPI.as_view("kabupaten_api"), methods=["GET"])
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/wilayah/kecamatan/<kode_kab>",
        view_func=KecamatanAPI.as_view("kecamatan_api"), methods=["GET"])
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/wilayah/desa/<kode_kec>",
        view_func=DesaAPI.as_view("desa_api"), methods=["GET"])
    return app


def jamaah_url(app: Flask):
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/jamaah/list",
        view_func=JamaahListAPI.as_view("list_jamaah_api"),
        methods=["GET", "POST"])
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/jamaah/report",
        view_func=ReportDataAPI.as_view("report_jamaah_api"),
        methods=["GET"])
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/jamaah/<jamaah_id>/detail",
        view_func=DetailJamaahAPI.as_view("detail_jamaah_api"),
        methods=["GET", "PUT", "DELETE"])
    return app


def tasks_url(app: Flask):
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/task/<task_id>",
        view_func=ReportTaskStatus.as_view("task_status_api"),
        methods=["GET"])
    return app


def user_url(app: Flask):
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/user/list",
        view_func=UserListAPI.as_view("list_user_api"),
        methods=["GET", "POST"])

    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/user/<user_id>/detail",
        view_func=DetailUserAPI.as_view("detail_user_api"),
        methods=["GET", "PUT", "DELETE"])

    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/user/password",
        view_func=ProfileChangePasswordAPI.as_view("password_profile_api"),
        methods=["POST", "PUT"])

    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/user/profile",
        view_func=ProfileUserAPI.as_view("profile_user_api"),
        methods=["PUT"])

    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/user/<user_id>/password/reset",
        view_func=ResetPasswordAPI.as_view("reset_password_user_api"),
        methods=["GET"])

    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/user/<user_id>/status/toggle",
        view_func=ToggleStatusAPI.as_view("toggle_status_user_api"),
        methods=["GET"])
    return app


def file_url(app: Flask):
    app.add_url_rule(
        f"{app.config.get('API_ROOT')}/file/<filename>",
        view_func=FileAPI.as_view("file_api"),
        methods=["GET"]
    )
    return app
