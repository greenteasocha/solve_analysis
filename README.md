# solve_analysis
## ngram & Byte Pair Encoding

### 解説

[世界トップキューバーのソルブを解析してみた(はてなブログ)](https://socha77.hatenablog.com/entry/2018/08/14/002401)

make raw file (ex. data/xxx/txt) and do  
```html
python readseq.py --path=data/xxx.txt --out=data/xxx.lin # make one-line file
python ngram.py --path=data/xxx.lin # get ngram  
python BPE.py --path=data/xxx.lin --out=data/xxx.bpe # get BPE dictionary and converted file 
```

## classify CFOP or Roux by Support Vector Machine

### 解説
はてなブログ(予定)  
```html
python readfeature.py --path=data/xxx.lin --out=data/xxx.json --method=CFOP # make json file
pyhon SVM.py data/xxx.json data/yyy.json ... #add all json files. training and inference 
```
