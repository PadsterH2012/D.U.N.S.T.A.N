from sqlalchemy.orm import Session
from .models import Setting

def get_setting(db: Session, key: str) -> str:
    setting = db.query(Setting).filter(Setting.key == key).first()
    if setting:
        return setting.value
    return None
