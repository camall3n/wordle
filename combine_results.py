import glob
import json
from tqdm import tqdm

all_results = {}
file_pattern = 'results/*'
filepaths = sorted(glob.glob(file_pattern))
len(filepaths)
for filepath in tqdm(filepaths):
    with open(filepath, 'r') as fp:
        results = json.load(fp)
    all_results.update(results)

bestWord = min(all_results, key=all_results.get)
bestWord, all_results[bestWord]

# json.dumps(all_results)
