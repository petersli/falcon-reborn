from PIL import Image
import torch, json
from torchvision import transforms, utils
import numpy as np

model = torch.load('model.pt')
model.eval()

def run(model, input):
    result = model(input)

    result_img = Image.fromarray(result)
    result_img.save('result.png', format='PNG')
    
run(model, input)