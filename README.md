# Non-Invasive Polygraph

## Description

This project is a non-invasive polygraph that aims to identify lies in a statement by using a machine learning model. The model analyzes the statement and determines if it is false or not with an accuracy of 61%. The polygraph also analyzes the movements of the eyes and head posing to further determine if the person is lying or not. The machine learning models used for the eye and head movement analysis were trained on a small dataset for demo purposes.

## Features

- Uses logistic model to analyze statements and determine if they are true or false
- Analyzes eye movement and head posing to detect lies
- Utilizes Microsoft Cognitive Services for speech-to-text and sentiment analysis

## Impact

This polygraph can be used in a variety of settings, including court proceedings and job interviews, to ensure that the truth is being told. It can help prevent injustice and manipulation of evidence in legal cases, as well as make sure that hiring decisions are based on accurate information.

## Installation

To use this project, you will need to clone the repository and install the commands:

```bash
  pip install requirements.txt
  python main.py
```

## Future Work

There are several ways in which the accuracy of this polygraph could be improved:

- Increase the size of the dataset used for training the machine learning models
- Add additional variables to analyze during a statement, such as heart rate, face microexpressions, and the coherence of the statement with past statements made by the person
- Improve the machine learning algorithms used for analysis
- Installation

## Acknowledgement
Part of these code was achived thanks to the previous work of the following people:
- Agarwal, V. (2020). Proctoring AI. GitHub. https://github.com/vardanagarwal/Proctoring-AI 
- Palacios, V. (2019). Deception_Detection_Capstone. GitHub. https://github.com/Victor-Palacios/Deception_Detection_Capstone
