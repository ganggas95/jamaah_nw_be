from sqlalchemy import DateTime, Column
from sqlalchemy import func
from jamaah.factory import db


class BaseORM:
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, onupdate=func.now())
    except_fields = ["create_at", "update_at"]

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def _from_request(self, payload, except_fields=None):
        if except_fields is None:
            except_fields = []
        else:
            except_fields = except_fields + self.except_fields.copy()

        for key in payload:
            if not isinstance(payload[key], dict) and key not in except_fields:
                setattr(self, key, payload[key])
