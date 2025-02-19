# db
host="localhost",
database="imdb",
user="zpf",
password="wsnk59ej"
db_conn_str = f"host={host} dbname={database} user={user} password={password}"

# dataset 
querydir = 'resource/jobquery'  # JOB query
tablenamedir = 'resource/jobtablename'  # tablename involved in the query statement
shorttolongpath = 'resource/shorttolong'  # Mapping of table abbreviations to full names
predicatesEncodeDictpath = 'resource/predicatesEncodedDict'   
queryEncodeDictpath = 'resource/queryEncodedDict' 

# OVN 
OVN_train_file_path = ''
test_file_path = ''
OVN_model_path = 'saved_models/ovn_supervised.pt'
OVN_save_dir = 'saved_models/'

# ADN
ADN_train_file_path = ''
ADN_model_path = 'saved_models/adn_supervised.pt'
ADN_save_dir = 'saved_models/'

result_path = ''