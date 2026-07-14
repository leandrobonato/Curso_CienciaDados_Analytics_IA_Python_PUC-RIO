from pyspark.sql import HiveContext
>>> hiveContext = HiveContext(sc)
>>> hiveQuery = "SELECT SentimentText FROM TWEETS WHERE UPPER(SENTIMENT)='POS';"
>>> dfPos = df = hiveContext.sql(hiveQuery)
>>> rddPos = dfPos.rdd
>>> stopWords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you','your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do','does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as','until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once','here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few','more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'don', 't', 's', 'should', 'now']
>>> contadorPalavras = rddPos.map(lambda x:x.SentimentText.replace(',','').replace('.', ' ').replace('-','').lower()) \
... .flatMap(lambda x: x.split()) \
... .filter(lambda x: x not in stopWords) \
... .map(lambda x: (x,1)) \
... .reduceByKey(lambda x,y:x+y) \
... .map(lambda x:(x[1],x[0])) \
... .sortByKey(False)
>>>
>>>
>>>
>>> contadorPalavras.take(10)