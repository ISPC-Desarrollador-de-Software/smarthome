import mysql.connector
import logging
from  mysql.connector import  errorcode
import configparser
import pathlib

logger = logging.getLogger("mysql.connector")

logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

class DBConn:
    def __init__(self,config_file = "config.ini"):
        self.config_file = config_file
        
        if(self.config_file!=""):
            config = configparser.ConfigParser()
            config_path = pathlib.Path(__file__).parent.absolute() / config_file
            config.read(config_path)
            self.db_config = config['database']
        
    def get_data_base_name(self):
        return self.db_config.get('database')
    
    def connect_to_mysql(self):
        
        try:
            return mysql.connector.connect(
                user = self.db_config.get('user'),
                password = self.db_config.get('password'),
                host = self.db_config.get('host'),
                database = self.db_config.get('database')
            )
        except mysql.connector.Error as err :
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("usuario o contraseña incorrecta")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database no exite ")
            else:
                print(err)
        return None
    
    
    
    