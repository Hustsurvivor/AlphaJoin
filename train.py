import config 
from AlphaJoin1_0.arguments import get_args
from AlphaJoin1_0.getResource import mygetResource
from AlphaJoin1_0.getQueryEncode import mygetQueryAttributions, mygetQueryEncode
import AlphaJoin1_0.supervised
from AlphaJoin1_0.findBestPlan import prepare, findBestPlan
import AdaptiveDecisionNet.supervised

if __name__ == '__main__':
    # acquire tablename and shorttolong file 
    if False:
        mygetResource(config.querypath, config.tablenamedir, config.shorttolongpath, config.db_conn_str)
    
    # acquire predicate Encoding and query Encoding 
    if True:
        attrNames = mygetQueryAttributions(config.querypath)
        mygetQueryEncode(attrNames, config.querypath, config.shorttolongpath, config.predicatesEncodeDictpath, config.queryEncodeDictpath)
    
    ovn_trainer = AlphaJoin1_0.supervised.supervised(config.OVN_save_dir, config.shorttolongpath, config.predicatesEncodeDictpath)

    # pretreatment: process data and split train dataset and valid dataset 
    ovn_trainer.pretreatment(config.OVN_train_file_path)
    
    # train OVN network : alphajoin1.0

    ovn_trainer.supervised()
    
    # test network on valid dataset 
    ovn_trainer.test_network()
    
    # # do test on test dataset 
    # totalNumberOfTables, queryEncodeDict, predicatesEncodeDict, intToTable = prepare(config.queryEncodeDictpath, config.predicatesEncodeDictpath, config.shorttolongpath)        
    # findBestPlan(config.OVN_model_path, config.tablenamedir, totalNumberOfTables, queryEncodeDict, predicatesEncodeDict, intToTable, config.result_path)
    
    # train ADN network : alphajoin2.0
    adn_trainer = AdaptiveDecisionNet.supervised.supervised(config.ADN_save_dir, config.shorttolongpath, config.predicatesEncodeDictpath)
    adn_trainer.pretreatment(config.ADN_train_file_path)

    for i in range(adn_trainer.datasetnumber):
        adn_trainer.load_data(i)
        adn_trainer.supervised()
        adn_trainer.test_network()
        adn_trainer.trainList.clear()
        adn_trainer.testList.clear()
    
    
    

     