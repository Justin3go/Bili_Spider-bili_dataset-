from tqdm import tqdm
import shutil
import os


def get_useful_ids(filepath):
    '''
    获取有效的数据
    这里是先把空的数据给去除，
    然后获取观看次数与点赞数差不多的数据
    '''
    useful_ids = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            item = line.split()
            if(item[-1] != '$'):
                if((int)(item[1]) >= 300):
                    if((int)(item[2])/(int)(item[1]) <= 0.1):
                        useful_ids.append(item[0])
    return useful_ids


def choose_by_id(ids, src, tar):
    '''
    根据获取的id，将该数据复制到目标文件夹中
    '''
    for id in tqdm(ids):
        file_src = src + str(id) + ".txt"
        file_tar = tar + str(id) + ".txt"
        shutil.copyfile(file_src, file_tar)


def clean_again(filepath):
    '''
    再次清除第三行为空的数据
    '''
    flag = 1
    for file in tqdm(os.listdir(filepath)):
        file = "C:/My_app/code/EasyTitle/cleaned_data/" + file
        with open(file, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            try:
                if(len(lines[2]) <= 3):
                    flag = 0
            except IndexError:
                flag = 0
        if(flag == 0):
            os.remove(file)
            flag = 1


if __name__ == "__main__":
    # step1
    file1 = r"C:/My_app/code/EasyTitle/dataset1/other.txt"
    clean_ids = get_useful_ids(file1)
    # print(len(clean_ids)) 26594

    # step2
    file2 = r"C:/My_app/code/EasyTitle/dataset/"
    target = r"C:/My_app/code/EasyTitle/cleaned_data/"
    choose_by_id(clean_ids, file2, target)

    # step3
    filepath = "C:/My_app/code/EasyTitle/cleaned_data"
    clean_again(filepath)
