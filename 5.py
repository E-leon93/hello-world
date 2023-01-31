#coding=utf-8

s_dict={1:'zhangsan',2:'lisi',3:'wangwu'}

for m in s_dict.keys():
    print('id:'+str(m))

for n in s_dict.values():
    print('name:'+str(n))

for s_id, s_name in s_dict.items():
    print('id:{0}   name:{1}'.format(s_id,s_name))
