import torch
import torch.nn as nn
import torch.utils.model_zoo as model_zoo
import torch.nn.functional as F
import math
from models.backbone.resnet import get_backbone
from models.neck.FPN import FPN


class output(nn.Module):
    def __init__(self,in_channel=256, scope=512):
        super(output, self).__init__()
        self.conv1 = nn.Conv2d(in_channel, 1, 1)
        self.sigmoid1 = nn.Sigmoid()
        self.conv2 = nn.Conv2d(in_channel, 4, 1)
        self.sigmoid2 = nn.Sigmoid()
        self.conv3 = nn.Conv2d(in_channel, 1, 1)
        self.sigmoid3 = nn.Sigmoid()
        self.scope = scope
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)

        nn.init.constant_(self.conv1.bias, -2.19)

    def forward(self, x):
        score = self.sigmoid1(self.conv1(x))
        loc = self.sigmoid2(self.conv2(x)) * self.scope
        angle = (self.sigmoid3(self.conv3(x)) - 0.5) * math.pi
        geo = torch.cat((loc, angle), 1)
        return score, geo


class EAST(nn.Module):
    def __init__(self, backbone=18, pretrained=True):
        super(EAST, self).__init__()

        self.extractor = get_backbone(backbone, pretrained)
        self.merge = FPN(self.extractor.out_channels, 256)
        self.output = output()

    def forward(self, x):
        return self.output(self.merge(self.extractor(x)))
