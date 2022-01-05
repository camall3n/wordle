import glob
import json
from tqdm import tqdm

worstCaseValidSetSize = {}
file_pattern = 'results/*'
filepaths = glob.glob(file_pattern)
len(filepaths)
for filepath in tqdm():
    with open(filepath, 'r') as fp:
        results = json.load(fp)
    worstCaseValidSetSize.update(results)

bestWord = min(worstCaseValidSetSize, key=worstCaseValidSetSize.get)
bestWord, worstCaseValidSetSize[bestWord]
