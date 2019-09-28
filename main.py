# a script that generates business models

import random

def get_industry_list():
    file = open('industry.txt', 'r')
    list = [x.strip() for x in file.readlines()]
    return list

def get_business_model_list():
    file = open('business_model.txt', 'r')
    list = [x.strip() for x in file.readlines()]
    return list


def get_product_list():
    file = open('product_description.txt', 'r')
    list = [x.strip() for x in file.readlines()]
    return list

def run():
    b_list = get_business_model_list()
    i_list = get_industry_list()
    p_list = get_product_list()
    master_list = []
    for i in i_list:
        for j in b_list:
            for k in p_list:
                idea = '{0},  {1}, {2}'.format(i, j, k)
                master_list.append(idea)
    random.shuffle(master_list, random.random)
    with open('ideas.txt', 'w') as f:
        for item in master_list:
            f.write("%s\n"% item)
    return master_list

if __name__ == "__main__":
    run()