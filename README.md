# 학부연구생 BCI 실습

**학부연구생 BCI 실습 프로젝트** 자료를 정리하였으며, 다양한 실험 코드와 분석 노트북이 포함되어 있습니다.
- 다양한 뇌파 데이터셋 시각화 및 전처리
- 다양한 알고리즘 기반 뇌파 데이터셋 분류 및 회귀 과제 수행
- '혼자 공부하는 머신러닝' 실습

---

## 주요 실습 주제

- BCI(Brain-Computer Interface) 데이터 분석
- CSP(공간 패턴 분해) + LDA를 통한 분류
- Logistic Regression 실험
- EEGNet 기반 딥러닝 아키텍처 실습
- 실험 환경: Python, Jupyter Notebook, Scikit-learn, PyTorch 등

---

## 파일 구성 설명

| 파일명 | 내용 요약 |
|--------|-----------|
| `BCI2` | 초기 실습: MATLAB을 통한 EEG 신호 데이터 시각화 |
| `BCI3` | MOABB 프레임워크 기반 Cho2017 뇌파 데이터 사용 및 사용자 생각 분류 |
| `BCI4` | FFT를 통한 DEAP 뇌파 데이터 전처리 및 KNN 알고리즘 기반 감정 분류 |
| `BCI5` | filter bank CSP 및 LDA 알고리즘 기반 Cho2017 뇌파 데이터 이진분류 |
| `BCI6` | CSP, FFT 기반 EEG 데이터 전처리 및 딥러닝 기반 이진분류 |
| `BCI7` | EEGNet 기반 MAMEM3 뇌파 데이터 처리 |
| `self_ML` | '혼자 공부하는 머신러닝' 구현 |

---

## 사용 환경

- Python 3.8+
- 필수 라이브러리:  
  `torch`, `sklearn`, `numpy`, `matplotlib`, `pandas`, `scipy` 등

노트북은 [Google Colab](https://colab.research.google.com/) 또는 로컬 Jupyter 환경에서 실행 가능합니다.

---

## 참고

- 실습 주제 및 목적에 따라 개별 노트북의 설명 및 코드가 다릅니다.
- 일부 데이터는 개인/실험실 보안상 포함되지 않았을 수 있습니다.

---

## 작성 및 실습자

- 소속: 인하대학교 인공지능공학과  
- 학부연구생: [@hsmai](https://github.com/hsmai)  
- 실습 기간: 2025년 겨울학기
