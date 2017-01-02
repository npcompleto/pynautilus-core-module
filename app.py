from rest import app 
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

app.run(host='0.0.0.0')
