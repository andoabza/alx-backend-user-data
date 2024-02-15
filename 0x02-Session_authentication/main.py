import datetime
from datetime import timedelta
user_id_by_session_id = {
            'user_id': '456',
            'created_at': datetime.datetime.now()
        }
print('created_at' in user_id_by_session_id)