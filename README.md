#dataset
## 1.VOC2007 dataset

- VOCdevkit
  - VOC2007
    - Annotations #标注数据xml
    - ImageSets
      - Main
        - test.txt #图片序号
        - train.txt
        - trainval.txt
        - val.txt
    - JPEGImages #存放图片
    - create_pascal_tf_record.py

## 2.data for tfrecord

- dataset
  - data #存放csv和tfrecord文件
  - test #存放图片和标注文件
  - train
  - val
  - xml_to_csv.py
  - generate_tfrecord.py# dataset
