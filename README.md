# East.Pytorch

## This is a PyTorch Re-Implementation of EAST
### Performance on ICDAR2015
download pretrain model [east_82](https://pan.baidu.com/s/1FRhBmugghhjvJnVh3sYidQ),password is 54ck,this model was pretraintrained by VISD 10K images,then finetuned by ICDAR15 1K images
model | precision | recall | F1
:-: | :-: | :-: | :-: 
paper(VGG16+RBOX) | 0.8046 | 0.7275 | 0.7641 | 
Our(resnet18+RBOX) | 0.835| 0.7554 | 0.7932 |
Our(VISD10K+IC15 1K) | 0.883| 0.767 | 0.821 |
### How to train this model
1.Modify image path and gt path in train.py

2.run train.py

### How to test images
1.Modify image path and model path in detect.py

2.run detect.py,the results are saved in "res" folder

### How to eval result
1.Modify image path and model path in eval.py

2.run deval.py and you will get the result

### keep update
