reference = {}
sources = {}

# SST
x = {}
x['name'] = 'sst'
x['target'] = 'sst_raw'
x['url'] = 'https://nlp.stanford.edu/sentiment/trainDevTestTrees_PTB.zip'
x['unpack'] = 'unzip trainDevTestTrees_PTB.zip -d sst_raw'
x['cleanup'] = 'rm trainDevTestTrees_PTB.zip'
sources[x['name']] = x

reference['sources'] = sources