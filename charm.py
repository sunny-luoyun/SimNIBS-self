import os
# 通过charm将结构像进行分割
# 执行命令并获取输出
for i in ["43"]:
    process = os.popen(f'charm Sub0{i} Sub0{i}.nii.gz --forceqform')
    output = process.read()
    print(output)
    process.close()