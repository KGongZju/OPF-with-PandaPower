import pandas as pd
import pandapower as pp
import numpy as np
from Process_ieee_txt_data import *
import pandapower.plotting as plot
#新建网络
net=pp.create_empty_network()
#节点与线路信息导入
Bus_118, Line_118, Gen_118=ieee_get_data()
#节点编号导入net
def getopf():
    #建造118节点信息
    for i in range(119):
        if i==0:
            pp.create_bus(net,vn_kv=380,max_vm_pu=1.05,min_vm_pu=0.95)
        else:
            pp.create_bus(net,vn_kv=110,max_vm_pu=1.05,min_vm_pu=0.95)
    #外来电节点设置为0号节点，其余节点与118节点编号对应
    pp.create_ext_grid(net,bus=0,min_p_mw=-10, max_p_mw=10, min_q_mvar=-10, max_q_mvar=10)
    #线路信息导入net
    for index,row in Line_118.iterrows():
        pp.create_line_from_parameters(net,from_bus=int(row['from']),to_bus=int(row['to']),length_km=1,r_ohm_per_km=float(row['rohm']),x_ohm_per_km=float(row['xohm']),c_nf_per_km=0,max_i_ka=float(row['maxi']))
    #节点负荷信息导入net
    for index,row in Bus_118.iterrows():
        pp.create_load(net,bus=int(row['BusNo']),p_mw=float(row['P'])/1.13,q_mvar=float(row['Q'])/1.13)
    #变压器节点信息导入net
    pp.create_transformer_from_parameters(net,hv_bus=0,lv_bus=1,sn_mva=6000.0,vn_hv_kv=380.0,vn_lv_kv=110.0,vk_percent=12.2,vkr_percent=0.25,pfe_kw=60.0,vscr_percent=0.25,i0_percent=0.06)
    #发电机信息导入net
    pp.create_poly_cost(net,0,'ext_grid', cp1_eur_per_mw=0)
    for index,row in Gen_118.iterrows():
        #发电机的技术参数
        pp.create_gen(net,bus=int(row['BusNo']),p_mw=float(row['Pg']),max_p_mw=float(row['Pmax']),min_p_mw=float(row['Pmin']),max_q_mvar=float(row['Qmax']),min_q_mvar=float(row['Qmin']),vm_pu=float(row['vm']),controllable=True)
        #发电机运行成本，由于是从txt中读取并导入，如果要更改，可能需要对txt进行读写操作
        pp.create_poly_cost(net,int(row['No']), 'gen', cp1_eur_per_mw=float(row['gencost']))


    #进行OPF优化verbose=True
    pp.runopp(net, verbose=True, delta=1e-16)
    #绘制节点关联图
    #plot.simple_plot(net)
    #pp.runpp(net)
    #print('net.res_bus:', net.res_bus);
    #print('net.res_line:', net.res_line);
    #print('net.res_gen:', net.res_gen)
    #print('net.res_cost:', net.res_cost)
    return net.res_gen.p_mw

A=getopf()
print(A)
