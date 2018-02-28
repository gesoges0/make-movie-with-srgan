import os
from tqdm import tqdm
from time import sleep

for i in tqdm(range(1, 6008+1)):
    #print('python srgan_main2.py --mode=evaluate --valid_lr_img={}'.format(name_file))
    print('python srgan_main2.py --mode=evaluate --valid_lr_img=image_%06d.png'%i)
    os.system('python srgan_main2.py --mode=evaluate --valid_lr_img=image_%06d.png'%i)
    
    
    #print('cp ./samples_movie/evaluate/valid_bicbic.png ./samples_movie/evaluate/valid_bicbic/valid_bicbic_{}'.format(name_file))
    os.system('cp ./samples_movie/evaluate/valid_bicubic.png ./samples_movie/evaluate/valid_bicubic/valid_bicubic_%06d.png'%i)
    #print('cp ./samples_movie/evaluate/valid_lr.png ./samples_movie/evaluate/valid_lr/valid_lr_{}'.format(name_file))
    os.system('cp ./samples_movie/evaluate/valid_lr.png ./samples_movie/evaluate/valid_lr/valid_lr_%06d.png'%i)
    #print('cp ./samples_movie/evaluate/valid_gen.png ./samples_movie/evaluate/valid_gen/valid_gen_{}'.format(name_file))
    os.system('cp ./samples_movie/evaluate/valid_gen.png ./samples_movie/evaluate/valid_gen/valid_gen_%06d.png'%i)
    #sleep(5)
    

    

