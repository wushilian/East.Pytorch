import os
from tqdm import tqdm
def convert_3d():
    sdirs='/media/wsl/e4e97cf5-d097-4359-bc8c-b24e8286e52a/ustc/DataSet/English/Synth3D-10K/label'
    tdirs='/media/wsl/e4e97cf5-d097-4359-bc8c-b24e8286e52a/ustc/DataSet/English/Synth3D-10K/gt'
    files=os.listdir(sdirs)
    for file in tqdm(files):
        temp=''
        with open(os.path.join(sdirs,file),'r') as f:
            lines=f.read()
            lines=lines.strip().split('\n')
            length=len(lines)
            for i in range(0,length,5):

                xy0=lines[i]
                xy3=lines[i+1]
                xy2=lines[i+2]
                xy1=lines[i+3]
                flag=lines[i+4]

                temp+=xy0+','+xy1+','+xy2+','+xy3+','
                if flag=='1':
                    temp+='###'
                else:
                    temp+='hahaha'
                temp+='\n'
        with open(os.path.join(tdirs,file),'w') as f:
            f.write(temp)
            #break


if __name__=='__main__':
    convert_3d()