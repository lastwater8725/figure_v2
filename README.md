## Project
- 피겨스케이팅 자세 분류 및 joint 분석 v2
- 시계열성을 갖는 csv데이터를 활용하여 성능을 높이는 방법을 찾는 것이이 주 목적입니다.

## Data
- AIhub의 피겨스케이팅 데이터셋을 활용하였습니다.

## Folder 구조
```

```
## Environment
- linux에서 진행하였습니다. linux에서 실행하는 것을 권장드립니다.
- anaconda 가상환경에서 진행하였습니다. anaconda를 활용하시는 걸 권장드립니다.

## Code 
1. 가상환경이 없는 경우 다음 명령어로 가상환경을 생성해주세요

```
conda create -n <가상환경이름> python=3.10 
```
⬇️ e.g.
```
conda create -n <dl_imp> python=3.10
```

2. 가상환경 활성화 및 필요한 라이브러리를 설치해주세요
```
conda activate <가상환경 이름>
pip install -r requirements.txt
```
(다음과 비슷한 오류가 발생한다면 필요한 라이브러리 직접 설치)
```
AttributeError: module 'cv2' has no attribute 'xphoto'
```
라이브러리 설치 명령어
```
conda install <라이브러리 이름>
```
⬇️ e.g.
```
AttributeError: module 'cv2' has no attribute 'xphoto'
--> conda install opencv-contrib-python
```


## 실험 결과

- 실험 결과 
```

```
