## Este repositório serve como entrega da Sprint 1 da Challenge da Turma 3ESPA em parceria com a CarePlus, para a disciplina de Physical Computing IOT & IOB

### Feito por:

#### Beatriz Rocha 553455

#### Luis Alberto 553507

#### Isabelle Torricelli 552806

#### Rafael Nascimento 553117

## Este projeto implementa um sistema simples de reconhecimento facial utilizando OpenCV e o algoritmo LBPH (Local Binary Patterns Histograms). Ele captura imagens faciais, treina um modelo com base nelas e executa reconhecimento em tempo real via webcam.

## Estrutura do projeto

```
/
├── faces/
│   ├── pessoa1/
│   ├── pessoa2/
│   └── ...
├── face_capture.py
├── train.py
├── recognition.py
├── modelo_faces.yml
├── labels.json
└── README.md
```
## Dependências

### - opencv-python
### - opencv-contrib-python
### - numpy

## Como Executar

```
python -m pip install -r requirements.txt

python face_capture.py

python train.py

python recognition.py

```


## O uso de dados biométricos, especialmente imagens faciais, envolve riscos e responsabilidades. Ao utilizar este sistema, você deve:

### - Sempre obter consentimento explícito das pessoas cujas imagens serão coletadas
### - Informar claramente a finalidade do reconhecimento facial
### - Armazenar as imagens em ambiente seguro e protegido
### - Evitar o uso para vigilância não autorizada
### - Nunca usar reconhecimento facial para discriminar pessoas

## Pontos importantes:

### Imagens faciais são dados sensíveis — semelhante a impressões digitais

### Pessoas têm direito de solicitar exclusão de suas imagens

### Não deve ser usado em sistemas de julgamento automatizado

### Não deve ser usado para rotular comportamentos, emoções ou perfis psicológicos
