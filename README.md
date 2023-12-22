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
|-- FVC (Root)
    |-- raw (이미지를 불러 읽을 경로)
        |-- FVC2000 (DB2,4 포함 - a, b 전부)
        |-- FVC2002 (DB1,3,4 포함 - a, b 전부)
        |-- FVC2004 (DB2,4 포함 - a, b 전부)
    |-- seg (자동으로 전처리된 이미지 저장될 예정)
        |-- FVC2000 (빈폴더)
        |-- FVC2002 (빈폴더)
        |-- FVC2004 (빈폴더)
```

## Data loading
1. Set the Root directory
  - **INPUT 1** || Your Pre-processing Root Dir (ex: /../../FVC/raw/): 
2. Choose the exact sub-set from the full FVC dataset.
  - **INPUT 2** || DIR Year:
  - **INPUT 3** || DIR Subset:
3. Pick/Change the index of the fingerprint image. (the indexs are sorted in the list)
  - **Image Index : (insert number or increase/decrease the number of index)**
4. Now you can control the filter types and sizes to nomarlize the dirty raw fingerprints.
  - ** First filer :
    - Integer Slider  
    
    | None | Gaussian | Bilateral | Median |
    | ------ | ------ | ------ | ------ |
    | - | Gaussian blur |  Bilateral blur | Median blur |
    | - | Recommand to use |  - | - |
 - ** Filst filter's size : [blur filter size]
 - ** [angle] : **Negative** - turn to **left** angle || **Positive** - turn to **right** angle  (
   - Real number Slider
5.  Fix the parameters to equalize the image.
  - ** bulk size : [equalize Bulk]
    - Integer Slider     
    - filter size
  - ** 차감 상수 : [equalize C]
    - Integer Slider
    - the **smaller**, the **weaker** the flattening the histogram.
    - I recommend to let it low for the highly pressured the fingerprint images.
6.  Select whether generate the margin for imgae, and how much to increase the margin.
  - ** [Paddig size] :
      - Integer Slider
      - if you do not want extra margin, set this value as **0**
      - I recommend to use the 20 pixels margin for the cleaner segmentation.
6.  Control the segmentation mask.
  - ** [USE : Simple blur mask] :
      - CheckBox
      - check the box when you use simple blurring mask, rather to use default sobel computational mask
  - ** [mask blur] :
      - Integer Slider
      - make it bigger for the disconnections are appeared in the fingerprint a lot.
  - ** [dilate blur] :
      - Integer Slider
      - It fuctions as the segmentation masking wider-larger or as fill the holes in the mask.
  - ** [erod  blur] :
      - Integer Slider
      - It fuctions as the segmentation masking smaller.
      - Be carefull not to increase the holes in the mask.
      
