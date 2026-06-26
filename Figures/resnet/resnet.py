import torch
import torchvision.models as models
from torchviz import make_dot

model = models.resnet50()
x = torch.randn(1, 3, 224, 224)
y = model(x)
dot = make_dot(y, params=dict(model.named_parameters()))
dot.format = 'png'
dot.render('resnet50_graph')
print("Saved: resnet50_graph.png")