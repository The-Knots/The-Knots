from PIL import Image
import torch
from torch import nn
from torchvision import transforms, models

resnet = models.resnet101(pretrained = True)

class WindRegressor(nn.Module):
    def __init__(self, tl_model):
        super().__init__()
        tl_model.fc = nn.Sequential(nn.Linear(2048, 100),
                                    nn.ReLU(True),
                                    nn.Linear(100, 1))
        self.model = tl_model

    def forward(self, x):
        return self.model(x)

def process(img_path):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.CenterCrop(128),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
    ])

    img = Image.open(img_path)
    img = transform(img).unsqueeze(0)
    
    model = WindRegressor(resnet)
    model.load_state_dict(torch.load('./static/model_101.pth', map_location=torch.device('cpu')))
    
    model.eval()
    return model(img)[0].item()
