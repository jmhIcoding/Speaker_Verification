#coding:utf-8
__author__ = 'jmh081701'
import  os
#--train_path 训练数据保存路径
#--noise_path 噪声数据保存路径
#--test_path 测试书籍保存路径
#--tdsv false 文本独立
#--restore false 不从模型载入
#--model_path 模型参数保存路径
#--train true   训练
#--optim    adam
#--lr 1e-3  学习速率
#--iteration     迭代次数

preprocess_cmd="python data_preprocess.py " \
          "--train_path=./train_path " \
          "--noise_path=./noise_path " \
          "--test_path=./test_path " \
          "--tdsv=no " \
          "--restore=no " \
          "--model_path=./tisv_model " \
          "--train=yes " \
          "--N=4 " \
          "--M=5 " \
          "--optim=adam " \
          "--lr=1e-3 " \
          "--iteration=100"
#数据预处理,提取原始语音文件的特性向量，并把数据保存到train_path,noise_path和test_path供训练测试使用
#os.system(preprocess_cmd)
train_cmd="python main.py " \
          "--train_path=./train_path " \
          "--noise_path=./noise_path " \
          "--test_path=./test_path " \
          "--tdsv=no " \
          "--restore=no " \
          "--model_path=./tisv_model " \
          "--train=yes " \
          "--N=4 " \
          "--M=5 " \
          "--optim=adam " \
          "--lr=1e-3 " \
          "--iteration=10000"

#训练
#os.system(train_cmd)


inference_cmd="python main.py " \
          "--train_path=./train_path " \
          "--noise_path=./noise_path " \
          "--test_path=./test_path " \
          "--tdsv=no " \
          "--restore=yes " \
          "--model_path=.\\tisv_model " \
          "--model_num=0"

#预测
os.system(inference_cmd)