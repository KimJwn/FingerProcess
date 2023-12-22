# Fingerprint Image Datasets Pre-Processing

This repository is for the pre-processing fingerprint data.

## Get Started
### Environment

**Python3.n**

**Packages**
- ipywidgets
- opencv
- numpy

## Data preparation
1. Download the [**FVC dataset**]
2. Construct the data structure as follows:
```
|-- FVC Root
    |-- raw - 이미지를 불러 읽을 경로
        |-- FVC2000 (DB2,4 포함 - a, b 전부)
        |-- FVC2002 (DB1,3,4 포함 - a, b 전부)
        |-- FVC2004 (DB2,4 포함 - a, b 전부)
    |-- seg - 자동으로 이미지 저장될 예정
        |-- FVC2000 (빈폴더)
        |-- FVC2002 (빈폴더)
        |-- FVC2004 (빈폴더)
```


