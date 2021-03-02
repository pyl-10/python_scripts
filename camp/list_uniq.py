# 给列表中的重复元素去重
def duplicate_removal(e_lists):
    r_lists = []
    seen = set()
    for e_list in e_lists:
        if e_list not in seen:
            r_lists.append(e_list)
            seen.append(e_list)
    return r_lists

# 生成器写法
def dup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
