
from datetime import datetime

# Funciones varias que se repiten en el proyecto
def get_datetime_today():
    now_utc = datetime.utcnow()
    now_string = now_utc.strftime('%Y-%m-%d %H:%M:%S')
    return now_string
