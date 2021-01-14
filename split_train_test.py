#! /usr/bin/python3
#-*-coding:utf-8-*-

from read_json import obtain_entity_obj
import numpy as np
import time


from KGObject import EntiPairObj,Enti

def read_all_data(path):


    # 手写读取数据
    f = open(path)
    x = []
    relation_set = []
    entity_set = []
    entityPair_set = []
    for d in f:
        d = d.strip()
        if d:
            d = d.split('\t')
            # 每个元素转为i
            elements = []
            for n in d:
                elements.append(n.strip())
            d = elements
            # print("一行数据",d)
            # time.sleep(3)
            x.append(d)
            relation_set.append(d[1])
            entity_set.append(d[0])
            entity_set.append(d[2])
            entityPair_set.append((d[0],d[2]))


    X = np.array(x)
    return X , relation_set,entity_set,set(entityPair_set)


global g_entityPair_set
global g_dataArry

def entity_pair_rel(g_i):


    entityPair_set = g_entityPair_set
    dataArry = g_dataArry


    entiObjset = obtain_entity_obj()
    symb_list = []
    for entiobj in entiObjset:
        symb_list.append(entiobj.symb)

    # print((symb_list))

    h_data = dataArry[:,0]
    t_data = dataArry[:,2]



    print(g_i)
    # 获取关系
    rel_set = []
    head = entityPair_set[g_i][0]
    tail = entityPair_set[g_i][1]
    """
    for t in range(len(dataArry)):
        if head == dataArry[t][0] and tail == dataArry[t][2]:
            rel_set.append(dataArry[t][1])
    """

    index_h = [i for i, x in enumerate(h_data) if x == head]
    index_t = [i for i, x in enumerate(t_data) if x == tail]

    com_index = [i for i in index_h if i in index_t]
    # print(com_index)
    for index in com_index:
        rel_set.append(dataArry[index][1])

    # print(head)
    # print(rel_set)
    # print(tail)

    # print("rel_set", rel_set)


    # 封装对象
    _entityPair_h = None
    _entityPair_t = None

    if head in symb_list:
        _entityPair_h = entiObjset[symb_list.index(head)]
    else:
        _entityPair_h= Enti(_id=None,_symbal=head,_lable=None,_description=None)

    if tail in symb_list:
        _entityPair_t = entiObjset[symb_list.index(tail)]

    else:
        _entityPair_t= Enti(_id=None,_symbal=tail,_lable=None,_description=None)



    pair = EntiPairObj(h_EntiObj=_entityPair_h,relation_list=rel_set, t_EntiObj=_entityPair_t)

    # if len(pair.Relset) >= 3:
    #
    #     print("Head lab,symb \n",pair.H_Enti.lable,pair.H_Enti.symb)
    #     print("Relations \n",pair.Relset)
    #     print("Tail lab \n",pair.T_Enti.lable,pair.T_Enti.symb)
    #     print("-------------------------------")


    return pair

def set_entity_pair(dataArry,entityPair_set):

    num_entity_pair = len(entityPair_set)
    #
    # entiObjset = obtain_entity_obj()
    # symb_list = []
    # for entiobj in entiObjset:
    #     symb_list.append(entiobj.symb)
    #
    # # print((symb_list))
    #
    # h_data = dataArry[:,0]
    # t_data = dataArry[:,2]
    #==========================
    """
    for i in range(num_entity_pair):
        print(i)
        # 获取关系
        rel_set = []
        head = entityPair_set[i][0]
        tail = entityPair_set[i][1]
        
        # for t in range(len(dataArry)):
        #     if head == dataArry[t][0] and tail == dataArry[t][2]:
        #         rel_set.append(dataArry[t][1])
        

        index_h = [i for i, x in enumerate(h_data) if x == head]
        index_t = [i for i, x in enumerate(t_data) if x == tail]

        com_index = [i for i in index_h if i in index_t]
        # print(com_index)
        for index in com_index:
            rel_set.append(dataArry[index][1])

        # print(head)
        # print(rel_set)
        # print(tail)

        # print("rel_set", rel_set)


        # 封装对象
        _entityPair_h = None
        _entityPair_t = None

        if head in symb_list:
            _entityPair_h = entiObjset[symb_list.index(head)]
        else:
            _entityPair_h= Enti(_id=None,_symbal=head,_lable=None,_description=None)

        if tail in symb_list:
            _entityPair_t = entiObjset[symb_list.index(tail)]

        else:
            _entityPair_t= Enti(_id=None,_symbal=tail,_lable=None,_description=None)



        pair = EntiPairObj(h_EntiObj=_entityPair_h,relation_list=rel_set, t_EntiObj=_entityPair_t)

        
        # print("Head lab,symb \n",pair.H_Enti.lable,pair.H_Enti.symb)
        # print("Relations \n",pair.Relset)
        # print("Tail lab \n",pair.T_Enti.lable,pair.T_Enti.symb)
        # print("-------------------------------")
        


        Pair_list.append(pair)
    """
    global g_entityPair_set
    g_entityPair_set =  entityPair_set
    global g_dataArry
    g_dataArry = dataArry

    import multiprocessing as mp
    Pair_list = []
    pool = mp.Pool(4)
    Pair_list = pool.map(entity_pair_rel,[i for i in range(num_entity_pair)])
    #==========================


    return Pair_list



def split_test_train(pair_set,train_file_path,test_file_path):

    num = len(pair_set)
    print(num)

    try:
        f_train = open(train_file_path,  'w')
        f_test = open(test_file_path,  'w')
        f_all_entityPairs = open('./FB15K/3800_entityPairs.txt',  'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:

        for i in range(len(pair_set)):
            X = pair_set[i]

            f_all_entityPairs.writelines(['%s \t %s \t %s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb,X.H_Enti.lable,X.H_Enti.description, X.Relset[x], X.T_Enti.symb, X.T_Enti.lable,X.T_Enti.description) for x in range(len(X.Relset))])

            if X.num_relations > 1:

                index = np.random.random_integers(0,X.num_relations - 1) #随机移除一个关系，作为测试

                relation_test = X.Relset.pop(index)

                f_train.writelines(['%s \t %s \t %s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb,X.H_Enti.lable,X.H_Enti.description, X.Relset[x], X.T_Enti.symb,X.T_Enti.lable,X.T_Enti.description) for x in range(len(X.Relset))])

                f_test.writelines('%s \t %s \t %s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb,X.H_Enti.lable,X.H_Enti.description, relation_test, X.T_Enti.symb,X.T_Enti.lable,X.T_Enti.description))

            else:
                f_train.writelines(['%s \t %s \t %s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb, X.H_Enti.lable,X.H_Enti.description, X.Relset[x], X.T_Enti.symb,X.T_Enti.lable,X.T_Enti.description) for x in range(len(X.Relset))])

        f_train.close()
        f_test.close()
        f_all_entityPairs.close()


def main():

    all_data_file = "./FB15K/3800_triples.txt"

    train_file_path = "./FB15K/3800_train.txt"
    test_file_path = "./FB15K/3800_test.txt"
    print("read all data \n")
    dataArry,relation_set,entity_set,entityPair_set = read_all_data(all_data_file)

    print(dataArry.shape)
    print("numble relation ",len(set(relation_set)))
    print("numble entity ",len(set(entity_set)))
    print("entityPair_set ",len(entityPair_set),len(set(entityPair_set)))

    print("set entity pair，there are relations between entity pairs \n")
    pair_set = set_entity_pair(dataArry,list(entityPair_set))

    print(len(pair_set))



    """
    for i in range(len(pair_set)):

        print("Head  lab \n",pair_set[i].H_Enti.lable)
        print("Relations \n",pair_set[i].Relset)
        print("Tail lab \n",pair_set[i].T_Enti.lable)

    """
    print("split train and test , one of relations to be as test data \n")
    split_test_train(pair_set,train_file_path,test_file_path)


    print("END !")


from multiprocessing import Pool

if  __name__=='__main__':

    main()



