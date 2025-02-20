# db
host="localhost"
database="imdb"
user="lgn"
password="li6545991360"
db_conn_str = f'host={host} dbname={database} user={user} password={password}'

# dataset 
querypath = 'data/damon/sql.txt'  # JOB query
tablenamedir = 'data/damon/jobtablename'  # tablename involved in the query statement
shorttolongpath = 'data/damon/shorttolong'  # Mapping of table abbreviations to full names

predicatesEncodeDictpath = 'data/damon/predicatesEncodedDict'   
queryEncodeDictpath = 'data/damon/queryEncodedDict' 

# OVN 
OVN_input_dim = 8*8 + 19 # len(tables)**2 + len(predicatesEncode)
OVN_train_file_path = 'data/damon/ovn_train_file.txt'
test_file_path = ''
OVN_model_path = 'saved_models/ovn_supervised.pt'
OVN_save_dir = 'saved_models/'
OVN_result_path = 'data/damon/ova_result.txt'

# ADN
ADN_train_file_path = ''
ADN_model_path = 'saved_models/adn_supervised.pt'
ADN_save_dir = 'saved_models/'

result_path = 'data/damon/result.txt'