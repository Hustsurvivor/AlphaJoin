import config 

with open('data/damon/sql.txt')as f:
    sql_lines = f.readlines()
    qid2sql = { line.split('#####')[0]: line.split('#####')[1].strip() for line in sql_lines}

with open('data/damon/seq.txt')as f:
    seq_lines = f.readlines()
    qid2seq = { line.split('#####')[0]: line.split('#####')[1].strip() for line in seq_lines}

with open('data/damon/time.txt')as f:
    time_lines = f.readlines()
    qid2time = { line.split('#####')[0]: line.strip().split('#####')[1:] for line in time_lines}

new_lines = []
for qid in qid2time:
    sql = qid2sql[qid]
    seq = qid2seq[qid]
    # 存pg的time
    time = qid2seq[qid][1]
    new_lines.append(qid + ',' + seq + ',' + time + '\n')

with open(config.OVN_train_file_path, 'w')as f:
    f.writelines(new_lines)    