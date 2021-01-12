
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


    return np.array(x) , relation_set,entity_set,set(entityPair_set)


def set_entity_pair(dataArry,entityPair_set):

    num_entity_pair = len(entityPair_set)
    Pair_list = []
    entiObjset = obtain_entity_obj()

    for i in range(num_entity_pair):
        # 获取关系
        rel_set = []
        head = entityPair_set[i][0]
        tail = entityPair_set[i][1]
        for t in range(len(dataArry)):
            if head == dataArry[t][0] and tail == dataArry[t][2]:
                rel_set.append(dataArry[t][1])


        #


        # 封装对象
        _entityPair_h = None
        _entityPair_t = None

        for entiobj_h in entiObjset:
            if entiobj_h.symb == head:
                _entityPair_h = entiobj_h
                break

        if _entityPair_h==None:
            _entityPair_h= Enti(_id=None,_symbal=head,_lable=None,_description=None)

        for entiobj_t in entiObjset:
            if entiobj_t.symb == tail:
                _entityPair_t = entiobj_t
                break
        # 实体集合中没有，重新创建
        if _entityPair_t==None:
            _entityPair_t= Enti(_id=None,_symbal=tail,_lable=None,_description=None)



        pair = EntiPairObj(h_EntiObj=_entityPair_h,relation_list=rel_set, t_EntiObj=_entityPair_t)
        """
        print("-------------------------------")
        print("Head  lab \n",pair.H_Enti.lable)
        print("Relations \n",pair.Relset)
        print("Tail lab \n",pair.T_Enti.lable)
        """

        Pair_list.append(pair)


    return Pair_list



def split_test_train(pair_set,train_file_path,test_file_path):




    num = len(pair_set)
    print(num)

    try:
        f_train = open(train_file_path,  'w')
        f_test = open(test_file_path,  'w')

    except IOError as err:
        print('file open error: {0}'.format(err))

    else:
        for i in range(pair_set):
            X = pair_set[i]
            if X.num_relations > 1:
                index = np.random.random_integers(0,X.num_relations - 1)

                relation_test = X.Relset.pop(index)

                f_train.writelines(['%s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb,X.H_Enti.lable, X.Relset[x], X.T_Enti.symb,X.T_Enti.lable) for x in range(len(X.num_relations))])

                f_test.writelines('%s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb,X.H_Enti.lable, relation_test, X.T_Enti.symb,X.T_Enti.lable))

            else:
                f_train.writelines(['%s \t %s \t %s \t %s \t %s\t \n'% (X.H_Enti.symb, X.H_Enti.lable, X.Relset[x], X.T_Enti.symb,X.T_Enti.lable) for x in range(len(X.num_relations))])

        f_train.close()
        f_test.close()




if  __name__=='__main__':


    all_data_file = "./FB15K/all_triples.txt"

    train_file_path = "./train.txt"
    test_file_path = "./test.txt"
    print("读取所有数据 \n")
    dataArry,relation_set,entity_set,entityPair_set = read_all_data(all_data_file)

    print(dataArry.shape)
    print("numble relation ",len(set(relation_set)))
    print("numble entity ",len(set(entity_set)))
    print("entityPair_set ",len(entityPair_set),len(set(entityPair_set)))

    print("设置 entity pair，每对实体之间有若干个关系")
    pair_set = set_entity_pair(dataArry,list(entityPair_set))

    print(len(pair_set))



    """
    for i in range(len(pair_set)):

        print("Head  lab \n",pair_set[i].H_Enti.lable)
        print("Relations \n",pair_set[i].Relset)
        print("Tail lab \n",pair_set[i].T_Enti.lable)

    """
    print("分割训练集和测试集合，将多关系实体对中的一个关系作为测试")
    split_test_train(pair_set,train_file_path,test_file_path)


    print("END !")



