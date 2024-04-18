import numpy as np
import sys


def parse_data(data):
    points = np.array(data, dtype=np.float32)

    # 添加一列强度值，默认设置为0.0
    intensity = np.zeros((points.shape[0], 1), dtype=np.float32)
    points_with_intensity = np.hstack((points, intensity))

    return points_with_intensity

assert len(sys.argv)>1


file_name=sys.argv[1]
with open(file_name+'.txt','r') as f:
    raw_data = f.read()
    raw_data=raw_data.strip().split('\n')
data = [list(map(float, line.split(','))) for line in raw_data]
points = parse_data(data)
print(points.shape)
# 将点数据保存到.bin文件
with open(file_name+'.bin', 'wb') as f:
    f.write(points.tobytes())

