
import sys
import torch
import json
from torch.utils.data import DataLoader
import pickle
if not torch.cuda.is_available():
    modelIP = torch.load('/content/drive/MyDrive/CPSC-8430-Deep-Learning-001/HW2/Model/model0.h5', map_location=lambda storage, loc: storage)
else:
    modelIP = torch.load('/content/drive/MyDrive/CPSC-8430-Deep-Learning-001/HW2/Model/model0.h5')
files_dir = '/content/drive/MyDrive/CPSC-8430-Deep-Learning-001/HW2/Data/MLDS_hw2_1_data/MLDS_hw2_1_data/testing_data/feat'
# i2w,w2i,dictonary =dictonaryFunc(4)
test_dataset = test_dataloader(files_dir)
test_dataloaderr =DataLoader(dataset = test_dataset, batch_size=1, shuffle=True, num_workers=8)
model = modelIP.cuda()
ss =testfun(test_dataloaderr, model, i2w)
with open('/content/drive/MyDrive/CPSC-8430-Deep-Learning-001/HW2/output.text', 'w') as f:
    for id, s in ss:
        f.write('{},{}\n'.format(id, s))


# Bleu Eval
test = json.load(open('/content/drive/MyDrive/CPSC-8430-Deep-Learning-001/HW2/Data/MLDS_hw2_1_data/MLDS_hw2_1_data/testing_label.json','r'))
#output = 'testing_data.txt'
output = '/content/drive/MyDrive/CPSC-8430-Deep-Learning-001/HW2/output.text'
result = {}

with open(output,'r') as f:
    for line in f:
        line = line.rstrip()
        comma = line.index(',')
        test_id = line[:comma]
        caption = line[comma+1:]
        result[test_id] = caption
#count by the method described in the paper https://aclanthology.info/pdf/P/P02/P02-1040.pdf
bleu=[]
for item in test:
    score_per_video = []
    captions = [x.rstrip('.') for x in item['caption']]
    score_per_video.append(BLEU(result[item['id']],captions,True))
    bleu.append(score_per_video[0])
average = sum(bleu) / len(bleu)
print("Average bleu score is " + str(average))