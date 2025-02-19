# AlphaJoin
AlphaJoin: Join Order Selection à la AlphaGo

### AlphaJoin 1.0 
#### 1. get resource
将查询query放在```resource/jobquery```目录下。
执行```AlphaJoin1.0/getQueryEncode.py```文件，生成目录```resource/jobtablename```和文件```shorttolong```。其中，```resource/jobtablename```目录下存放每个查询中涉及的表；```shorttolong```存放表别名到全名的映射。
``` python
python AlphaJoin1.0/getResource.py
```

#### 2. get queryencoding
运行```AlphaJoin1.0/getQueryEncode.py```文件，生成query编码和predicate编码。
``` python 
python AlphaJoin1.0/getQueryEncode.py
```

#### 3. pretreatment
运行```AlphaJoin1.0/pretreatment.py```文件，进行预处理。包括划分训练集和验证集。
``` python
python AlphaJoin1.0/pretreatment.py
```
> ```pretreatment.py```输入的文件内容的形式为： ```queryName + "," + hintCore + "," + "timeout,-," + df.format(new Date());```

#### 4. train network
运行```AlphaJoin1.0/train_network.py```文件，进行网络训练。用预处理时划分的训练集和验证集进行模型训练。
``` python
python AlphaJoin1.0/train_network.py
```

#### 5. find best plan 
运行```AlphaJoin1.0/findBestPlan.py```文件，对训练好的模型进行测试。
``` python
python AlphaJoin1.0/findBestPlan.py
```

### AlphaJoin 2.0

在AlphaJoin 1.0的基础上增加自适应决策网络。
``` python 
python AdaptiveDecisionNet/crossvalidation.py
```
其中pretreatment输入的文件的格式为``` queryName + "," + PGtime + "," + hinttime + "," + label ```

### 训练流程
先用训练集训练AlphaJoin1.0得到训练好的OVN(order value network)网络。
再用AlphaJoin1.0对训练集进行测试，得到预测的hint，由hint得到plan运行的时间hinttime。
用训练集的PGtime和hinttime训练AlphaJoin2.0的ADN(adaptive decision network)网络。
最终联合OVN与ADN对测试集进行测试。
