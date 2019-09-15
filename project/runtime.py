from PIL import Image
import torch, json
import torchvision
from torchvision import transforms, utils
import numpy as np
import os


'''
model = torch.load('model.pt')
model.eval()

def run(input_id):
    input_dir = os.path.join(os.getcwd(),'static', 'input', input_id)
    input = Image.open(input_dir)
    result = model(input)

    result_img = Image.fromarray(result)
    result_img.save(os.path.join(os.getcwd(), 'static', 'output', input_id), format='PNG')
    

'''

def run(input_id):
    model = torch.hub.load('mateuszbuda/brain-segmentation-pytorch', 'unet',
        in_channels=3, out_channels=1, init_features=32, pretrained=False)

    model.load_state_dict(torch.load("model.pt"))

    input_dir = os.path.join(os.getcwd(),'static', 'input', input_id + '.png')
    input_image = Image.open(input_dir)

    m, s = np.mean(input_image, axis=(0, 1)), np.std(input_image, axis=(0, 1))
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=m, std=s),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)
    print(input_batch)

    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model = model.to('cuda')

    with torch.no_grad():
        output = model(input_batch)

    torchvision.utils.save_image(torch.round(output[0]), os.path.join(os.getcwd(), 'static', 'output', input_id + '.png'))

run('med')