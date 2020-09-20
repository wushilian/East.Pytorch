import time
import torch
import subprocess
import os
from models.East import EAST
from detect import detect_dataset
import shutil


def eval_model(model_name, test_img_path, submit_path, save_flag=True):
	if os.path.exists(submit_path):
		shutil.rmtree(submit_path) 
	os.mkdir(submit_path)

	device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
	model = EAST().to(device)
	model.load_state_dict(torch.load(model_name))
	model.eval()
	
	start_time = time.time()
	detect_dataset(model, device, test_img_path, submit_path)
	os.chdir(submit_path)
	res = subprocess.getoutput('zip -q submit.zip *.txt')
	res = subprocess.getoutput('mv submit.zip ../')
	os.chdir('../')
	res = subprocess.getoutput('python ./evaluate/script.py –g=./evaluate/gt.zip –s=./submit.zip')
	print(res)
	os.remove('./submit.zip')
	print('eval time is {}'.format(time.time()-start_time))	

	if not save_flag:
		shutil.rmtree(submit_path)


if __name__ == '__main__': 
	model_name = './pths/model_epoch_30.pth'
	test_img_path = os.path.abspath('/media/wsl/e4e97cf5-d097-4359-bc8c-b24e8286e52a/ustc/DataSet/English/icdar2015/detection/test/imgs')
	submit_path = './submit'
	eval_model(model_name, test_img_path, submit_path)
