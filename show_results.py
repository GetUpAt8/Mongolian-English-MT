import os
import re
import json
import matplotlib.pyplot as plt

result_dir = './results/'
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

draw_whats = ['loss', 'bleu', 'ppl']


# 打开txt文件并读取内容
with open('./nohup.out', 'r', encoding='utf8') as file:
    file_content = file.read()

# 使用正则表达式来匹配满足特定格式的行
pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \| INFO \| valid \| epoch \d+ \| valid on \'valid\' subset \| loss [\d.]+ \| nll_loss [\d.]+ \| ppl [\d.]+ \| bleu [\d.]+ \| wps [\d.]+ \| wpb [\d.]+ \| bsz [\d.]+ \| num_updates (\d+|\d+\.\d+e[+-]\d+) \| best_bleu [\d.]+)'

matches = re.findall(pattern, file_content)

with open(result_dir + 'epochs.txt', 'w', encoding='utf8') as f:
    
    # 打印匹配到的行
    for match in matches:
        # print(match)
        f.write(match[0] + '\n')

# 打开txt文件并读取内容
with open(result_dir + 'epochs.txt', 'r', encoding='utf8') as file:
    file_content1 = file.read()
# 使用正则表达式来匹配并提取指标
pattern1 = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| INFO \| valid \| epoch (\d+) \| valid on \'valid\' subset \| loss ([\d.]+) \| nll_loss ([\d.]+) \| ppl ([\d.]+) \| bleu ([\d.]+) \| wps ([\d.]+) \| wpb ([\d.]+) \| bsz ([\d.]+) \| num_updates (\d+|\d+\.\d+e[+-]\d+) \| best_bleu ([\d.]+)'

matches1 = re.findall(pattern1, file_content1)

# 创建一个字典，用于存储各项指标的值
metrics_data = {
    'timestamp': [],
    'epoch': [],
    'loss': [],
    'nll_loss': [],
    'ppl': [],
    'bleu': [],
    'wpb': [],
    'wps': [],
    'bsz': [],
    'num_updates': [],
    'best_bleu': []

}

# 遍历匹配结果，整理数据
for match in matches1:
    # print(match)
    timestamp, epoch, loss, nll_loss, ppl, bleu, wps, wpb, bsz, num_updates, best_bleu = match  
    
    epoch = int(epoch)
    loss = float(loss)
    nll_loss = float(nll_loss)
    ppl = float(ppl)
    bleu = float(bleu)
    wps = float(wps)
    wpb = float(wpb)
    bsz = float(bsz)
    num_updates = float(num_updates)
    best_bleu = float(best_bleu)

    # metrics_data['timestamp'].append(timestamp)
    metrics_data['epoch'].append(epoch)
    metrics_data['loss'].append(loss)
    metrics_data['nll_loss'].append(nll_loss)
    metrics_data['ppl'].append(ppl)
    metrics_data['bleu'].append(bleu)
    metrics_data['wps'].append(wps)
    metrics_data['wpb'].append(wpb)
    metrics_data['bsz'].append(bsz)
    metrics_data['num_updates'].append(num_updates)
    metrics_data['best_bleu'].append(best_bleu)

# print(len(metrics_data['bleu']),len(metrics_data['best_bleu']))

# 保存整理后的数据为JSON文件
with open(result_dir + 'metrics.json', 'w', encoding='utf8') as json_file:
    json.dump(metrics_data, json_file, indent=4)

print("Data has been saved to " + result_dir + "metrics.json.")

# 从JSON文件中加载数据
with open(result_dir + 'metrics.json', 'r', encoding='utf8') as json_file:
    data = json.load(json_file)


for obj in draw_whats:
    # 提取Bleu项对应的999个值并将其转换为浮点数
    draw_what = obj
    convert_draw_what = draw_what.upper()

    bleu_values = data[draw_what]
    # print(bleu_values)
    # 生成X轴坐标
    epochs = list(range(1, len(bleu_values) + 1))

    # 增加图像分辨率
    plt.figure(dpi=1000)

    # 绘制图表
    plt.plot(epochs, bleu_values, marker='o', linestyle='-', color='b')
    plt.title(convert_draw_what + ' Scores Over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel(convert_draw_what)
    plt.grid(True)
    plt.savefig(result_dir + draw_what + ".png")
    # plt.show()
    plt.close()

print("Pics has been saved to " + result_dir + ".")