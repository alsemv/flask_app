import urllib

DEBUG = True
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect={}".format(urllib.parse.quote_plus('DRIVER={ODBC Driver 11 for SQL Server};SERVER=DFM15\SQLEXPRESS;DATABASE=cantine;UID=sa;PWD=dfm_2017!;'))
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY="secretkey"
