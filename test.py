import numpy as np
import torch
import config 
from AlphaJoin1_0.findBestPlan import prepare, findBestPlan
from AdaptiveDecisionNet.models import ValueNet

if __name__ == '__main__':
    
    totalNumberOfTables, queryEncodeDict, predicatesEncodeDict, intToTable = prepare(config.queryEncodeDictpath, config.predicatesEncodeDictpath, config.shorttolongpath)        
    findBestPlan(config.OVN_model_path, config.tablenamedir, totalNumberOfTables, queryEncodeDict, predicatesEncodeDict, intToTable, config.result_path)

    
    adn_Net = ValueNet(856, 5)
    adn_Net.load_state_dict(torch.load(config.ADN_model_path, map_location=lambda storage, loc: storage))
    adn_Net.eval()
    
    with open(config.test_file_path)as f:
        query_lines = f.readlines()
        query_name_list = [ query_lines.split('#####')[0] for line in query_lines]
    
    for query_name in query_name_list: 
        # state is queryencode
        state = queryEncodeDict[query_name]
        state_tensor = torch.tensor(state, dtype=torch.float32)
        
        predictionRuntime = adn_Net(state_tensor)
        prediction = predictionRuntime.detach().cpu().numpy()
        maxindex = np.argmax(prediction)
        
        # 0为pg 1为alphajoin
        
        with open(config.result_path, 'a')as f:
            f.write(query_name + '#####' + maxindex + '\n')