from PIL import Image
import torch, json
from torchvision import transforms, utils
import numpy as np
import os

model = torch.load('model.pt')
model.eval()

def run(input_name):
    input_dir = os.path.join(os.getcwd(),'static', input_name)
    input = Image.open(input_dir)
    result = model(input)

    result_img = Image.fromarray(result)
    result_img.save('result.png', format='PNG')
    