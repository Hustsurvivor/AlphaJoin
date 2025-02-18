# AlphaJoin
AlphaJoin: Join Order Selection à la AlphaGo
## run damon

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
其中pretreatment输入的文件的格式为``` queryName + "," + origintime + "," + qpoptime + "," + label ```