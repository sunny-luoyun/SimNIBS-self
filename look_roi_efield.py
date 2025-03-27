import os
import numpy as np
import simnibs

# 查看roi单位电场强度
g = ['01', '02', '03', '04', '06', '07', '09', '12', '13', '14', '15', '17', '18', '21', '22', '25', '26', '27', '28', '29', '33', '36', '38', '40', '41', '43']
for i in g:
    # 读取刺激结果，file放入刺激上一步骤刺激所生成的文件夹路径
    head_mesh = simnibs.read_msh(
        os.path.join(f'D:\\moni\\m2m_Sub0{i}\\test_tdcs1', f'Sub0{i}_TDCS_1_scalar.msh')
    )

    # 划分出灰质
    gray_matter = head_mesh.crop_mesh(simnibs.ElementTags.GM)

    # 设定要观察的ROI位置
    ernie_coords = simnibs.mni2subject_coords([22, -3, -4], f'D:\moni\m2m_Sub0{i}')
    # 以roi为中心半径10mm的小球
    r = 10.

    # 获取平均场强
    elm_centers = gray_matter.elements_baricenters()[:]
    roi = np.linalg.norm(elm_centers - ernie_coords, axis=1) < r
    elm_vols = gray_matter.elements_volumes_and_areas()[:]

    # 放置roi小球
    gray_matter.add_element_field(roi, 'roi')
    gray_matter.view(visible_fields='roi')

    # 得到小球内电场
    field_name = 'magnE'
    field = gray_matter.field[field_name][:]

    # 输出结果
    mean_magnE = np.average(field[roi], weights=elm_vols[roi])
    print(f'Sub0{i} ', mean_magnE)