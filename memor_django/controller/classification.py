import json
import os

# object detection box size
def box_size(x):
    box = (x['topleft']['x'] - x['bottomright']['x'])**2 + (x['topleft']['y'] - x['bottomright']['y'])**2
    return box

def classifying():
    # 객체탐지 후 생성된 json 파일 목록 file_jlist에 저장
    json_path = './images/out'
    file_jlist = os.listdir(json_path)
    print('file_jlist\n',file_jlist,'\n')

    # 이미지 파일 목록 file_ilist에 불러오기
    img_path = './images'
    file_ilist = os.listdir(img_path)
    file_ilist.remove('out')
    print('file_ilist\n',file_ilist,'\n')

    # json 파일에서 대표 label 선정 후 이미지 파일 이름에 집어넣기 
    # 분류 기준 : confidence > 0.4 / box size 최대인 label
    for j in range(len(file_jlist)):
        with open('./images/out/'+file_jlist[j],'r') as json_file:
            json_data = json.load(json_file)
            fst_classification = []

            for i in json_data:
                if i["confidence"] >= 0.35:
                    fst_classification.append(i)
            print('fst_classification\n',fst_classification,'\n')

            # 이미지의 confidence < 0.35 이면 이름에 label 집어넣기 x
            try:
                size = box_size(fst_classification[0])
                best = {}
                for i in range(len(fst_classification)):
                    print(i,': ',size)
                    if size <= box_size(fst_classification[i]):
                        size = box_size(fst_classification[i])
                        best = fst_classification[i]
                print('box size: ', size, ', best: ', best, '\n')

                src = os.path.join(img_path, file_ilist[j])
                dst = best['label'] + '_' + file_ilist[j]
                dst = os.path.join(img_path, dst)
                os.rename(src, dst)
                json_file.close()
            except IndexError as e:
                print('IndexError: ', e)
                json_file.close()
                
        print('======================',j,'=========================')

# 객체 중복 제거

def deduplication():

    img_path = './images'
    file_ilist = os.listdir(img_path)
    print('file_ilist\n',file_ilist,'\n')

    joong_gan_answer=[]
    for arr in file_ilist:
        strArray = arr.split('_')
        joong_gan_answer.append(strArray[0])

    my_set = set(joong_gan_answer)
    label_list = list(my_set)
    temp = []
    temp = label_list
    for arr in label_list:
        isint = ''.join([i for i in arr if not i.isdigit()])
        if isint is '':
            temp.remove(arr)
        elif str(arr) == 'out':
            temp.remove(arr)
    label_list = temp
    return label_list











