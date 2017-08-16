import jieba

seg_list = jieba.cut("我在学习自然语言处理", cut_all=True)
print(seg_list)
print("Full Mode:" + "/".join(seg_list))

seg_list = jieba.cut("我在学习自然语言处理", cut_all=False)
print(seg_list)
print("Default Mode:"+ "/".join(seg_list))
# 生成用于倒排索引的分词用于建立索引
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后再哈佛大学学习")
print(",".join(seg_list))


