SECRET_KEY = 'Pebonito2'

SQLALCHEMY_DATABASE_URI = \
'{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = 'fatec',
    servidor = 'localhost',
    database = 'Clinica'
)