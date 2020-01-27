import time
import os
import pandas as pd
from celery import Task
from flask import current_app as app
from jamaah.models.jamaah import Jamaah


class JamaahTasks(Task):
    ignore_result = False
    name = "jamaah_report_task"
    writer = None
    title = "Report Jamaah"
    filename = "report_jamaah"
    filetype = "xlsx"
    progress = 0
    columns = ["no_induk", "nama", "nik", "jenis_kelamin", "alamat",
               "provinsi", "kabupaten", "kecamatan", "desa", "dusun", "aktif",
               "tempat_lahir", "tanggal_lahir"]
    dataset = {"no_induk": [], "nama": [], "nik": [], "jenis_kelamin": [], "alamat": [],
               "provinsi": [], "kabupaten": [], "kecamatan": [], "desa": [], "dusun": [], "aktif": [],
               "tempat_lahir": [], "tanggal_lahir": [], }

    def run(self, provinsi_id=None, kabupaten_id=None, kecamatan_id=None):

        self.query_l = Jamaah.query.filter(
            Jamaah.jenis_kelamin == "Laki-Laki"
        )
        self.query_p = Jamaah.query.filter(
            Jamaah.jenis_kelamin == "Perempuan"
        )
        data_l = []
        data_p = []
        if provinsi_id and (kabupaten_id is None and kecamatan_id is None):
            data_l, data_p = self.collect_data_provinsi(provinsi_id)
        elif provinsi_id and (kabupaten_id and kecamatan_id is None):
            data_l, data_p = self.collect_data_kabupaten(kabupaten_id)
        elif kecamatan_id and kabupaten_id and provinsi_id:
            data_l, data_p = self.collect_data_kecamatan(kecamatan_id)
        else:
            data_l, data_p = self.collect_all_data()
        total = len(data_l) + len(data_p)
        self.progress = 0
        self.iter_data(data_l, total)
        self.iter_data(data_p, total)
        data_frame = self.create_dataframe()
        self.init_writer()
        self.write_excel(data_frame, self.title)
        self.save_excel()

        self.update_task_state("SUCCESS", total=total+1, status="SUCCESS")
        return {
            "filename": f"{self.filename}.{self.filetype}",
            "current": self.progress,
            "total": total,
            "status": "SUCCESS"
        }

    def save_excel(self):
        self.writer.save()

    def init_writer(self):
        filename = None
        with app.app_context():
            filename = os.path.join(
                app.config.get("EXPORT_DIR_DATA"),
                f"{self.filename}.{self.filetype}"
            )
        self.writer = pd.ExcelWriter(filename, "xlsxwriter")

    @property
    def workbook(self):
        return self.writer.book

    def worksheet(self, sheet_name):
        return self.writer.sheets[sheet_name]

    def write_excel(self, data_frame, sheet_name="Sheet1"):
        data_frame.to_excel(self.writer, sheet_name=sheet_name,
                            columns=data_frame.columns)

    def create_dataframe(self):
        data_frame = pd.DataFrame(self.dataset, columns=self.columns)
        return data_frame

    def iter_data(self, iterable_data=None, total=0):
        if iterable_data is None:
            iterable_data = []
        for data in iterable_data:
            self.update_dataset(data)
            self.progress += 1
            self.update_task_state("PROGRESS", total=total+1, status="PENDING")
            time.sleep(0.05)

    def update_dataset(self, data):
        self.dataset["no_induk"].append(data.no_induk)
        self.dataset["nama"].append(data.nama)
        self.dataset["nik"].append(data.nik)
        self.dataset["jenis_kelamin"].append(data.jenis_kelamin)
        self.dataset["alamat"].append(data.alamat)
        self.dataset["provinsi"].append(data.provinsi)
        self.dataset["kabupaten"].append(data.kabupaten)
        self.dataset["kecamatan"].append(data.kecamatan)
        self.dataset["desa"].append(data.desa)
        self.dataset["dusun"].append(data.dusun)
        self.dataset["aktif"].append("Aktif" if data.aktif else "Non Aktif")
        self.dataset["tanggal_lahir"].append(data.tanggal_lahir)
        self.dataset["tempat_lahir"].append(data.tempat_lahir)

    def collect_data_provinsi(self, provinsi_id):
        self.title = "Report Jamaah Provinsi"
        self.filename = "report_jamaah_provinsi"
        jamaah_p = self.query_p.filter(
            Jamaah.provinsi_id == provinsi_id).all()
        jamaah_l = self.query_l.filter(
            Jamaah.provinsi_id == provinsi_id).all()
        return jamaah_l, jamaah_p

    def collect_data_kabupaten(self, kabupaten_id):
        self.title = "Report Jamaah Kabupaten"
        self.filename = "report_jamaah_kabupaten"

        jamaah_p = self.query_p.filter(
            Jamaah.kabupaten_id == kabupaten_id).all()
        jamaah_l = self.query_l.filter(
            Jamaah.kabupaten_id == kabupaten_id).all()
        return jamaah_l, jamaah_p

    def collect_data_kecamatan(self, kecamatan_id):
        self.title = "Report Jamaah Kecamatan"
        self.filename = "report_jamaah_kecamatan"
        jamaah_p = self.query_p.filter(
            Jamaah.kecamatan_id == kecamatan_id).all()
        jamaah_l = self.query_l.filter(
            Jamaah.kecamatan_id == kecamatan_id).all()
        return jamaah_l, jamaah_p

    def collect_all_data(self):
        self.title = "Report Jamaah"
        self.filename = "report_jamaah"
        jamaah_p = self.query_p.all()
        jamaah_l = self.query_l.all()
        return jamaah_l, jamaah_p

    def update_task_state(self, state, total=0, status="PENDING"):
        self.update_state(
            state=state,
            meta={
                'current': self.progress,
                'total': total,
                'status': status
            })
