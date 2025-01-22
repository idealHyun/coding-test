def solution(data, ext, val_ext, sort_by):
    mapping_dict = {'code':0, 'date':1,'maximum':2,'remain':3}
    
    ext_num = mapping_dict[ext]
    sort_by_num = mapping_dict[sort_by]
    
    # ext 필터링
    filtered_data = [x for x in data if x[ext_num] < val_ext]
    
    # 정렬
    filtered_data.sort(key=lambda x: x[sort_by_num])
    
    return filtered_data