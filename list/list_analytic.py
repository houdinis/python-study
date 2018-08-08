#列表解析式

#九九乘法表
print(['{:04}.{}'.format(i,''.join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)])) for i in range(1,101)])



#'0001.xzmeglnmib'
#'0002.rakvhtajow'
#'0003.gsqjhtgobg'
#生成以上格式
print(['{:04}.{}'.format(i,''.join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)])) for i in range(1,101)])