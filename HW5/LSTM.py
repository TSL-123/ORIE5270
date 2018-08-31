import torch
from torchtext import data
from torchtext import datasets
import random

SEED = 1234

torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)

TEXT = data.Field(tokenize='spacy')
LABEL = data.LabelField(tensor_type=torch.FloatTensor)

train, test = datasets.IMDB.splits(TEXT, LABEL)

train, valid = train.split(random_state=random.seed(SEED))