# -*- coding: utf-8 -*-
import argparse

def model_config():
    parser = argparse.ArgumentParser()

    # Data
    data_arg = parser.add_argument_group("Data")
    data_arg.add_argument("--data_dir", type=str, default="./data/")
    data_arg.add_argument("--data_prefix", type=str, default="demo")
    data_arg.add_argument("--save_dir", type=str, default="./models/")

    # Network
    net_arg = parser.add_argument_group("Network")
    net_arg.add_argument("--embed_size", type=int, default=256)
    net_arg.add_argument("--hidden_size", type=int, default=768)
    net_arg.add_argument("--bidirectional", type=str2bool, default=True)
    net_arg.add_argument("--attn", type=str, default='dot', choices=['none', 'mlp', 'dot', 'general'])

    config = parser.parse_args()

    return config

if __name__ == '__main__':
    config = model_config()
    print('data_dir: ', config.data_dir)


# 1. import argparse    首先导入模块
# 2. parser = argparse.ArgumentParser()    创建一个解析对象
# 3. parser.add_argument()  向该对象中添加要关注的命令行参数和选项
# 4. parser.parse_args()    进行解析