# Reti Neurali: dall'idea al dispositivo

Materiale didattico per un'introduzione alle **reti neurali artificiali** tramite un problema di riconoscimento di attività fisiche. Pensata per studenti delle scuole superiori che hanno già seguito le lezioni introduttive sul machine learning (classificazione e regressione).

Il filo conduttore è una **storia**: gli studenti vestono i panni del team di ingegneria di WristMind, una startup che deve costruire un braccialetto intelligente capace di riconoscere cosa stai facendo — camminare, correre, riposare — direttamente sul chip al polso, senza connessione internet. Partendo da un singolo neurone artificiale, arrivano in quattro tappe a costruire una rete neurale completa e a prepararla per il deployment su un microcontrollore reale.

## Struttura della lezione

Quattro notebook progressivi. Ogni notebook è autonomo: carica il dataset, applica il preprocessing necessario e introduce i concetti richiesti. La narrazione è continua, ogni notebook chiude con un cliffhanger ripreso dal successivo.

| # | Notebook | Tema |
|---|---|---|
| 1 | `01_il_risveglio_del_neurone.ipynb` | Il percettrone: dal neurone biologico all'artificiale, funzioni di attivazione, classificazione binaria (riposo vs. movimento) con Keras |
| 2 | `02_la_rete_si_fa_profonda.ipynb` | Multi-Layer Perceptron: strati nascosti, backpropagation, classificazione multiclasse (6 attività), matrice di confusione, softmax |
| 3 | `03_sfida_tra_modelli.ipynb` | Regressione con reti neurali, confronto NN vs. k-NN vs. modello lineare, overfitting nelle reti grandi, Dropout |
| 4 | `04_dal_laboratorio_al_dispositivo.ipynb` | Deployment su dispositivi embedded: TensorFlow Lite, quantizzazione int8, firmware Arduino, Edge AI |

## Obiettivi di apprendimento

Al termine della lezione lo studente sarà in grado di:

- descrivere il percettrone come generalizzazione del modello lineare con funzione di attivazione;
- spiegare intuitivamente come funziona la backpropagation;
- costruire e addestrare una rete neurale densa con Keras per classificazione e regressione;
- leggere le curve di apprendimento e riconoscere i segnali di overfitting;
- confrontare reti neurali con k-NN e modelli lineari e scegliere il modello appropriato al problema;
- descrivere il processo di deployment su dispositivi embedded e il ruolo di TFLite.

## Approccio didattico

Stesso schema della lezione di regressione: prima di ogni cella di codice c'è una **cella di testo** che spiega cosa stiamo per fare e perché, ricollegandolo alla storia. Il codice è generosamente commentato. Le **sezioni di teoria matematica** sono raccolte in blocchi dedicati che il docente può approfondire o saltare a seconda del livello della classe.

Ogni notebook si chiude con:
- **Cosa dovremmo aver capito** — sintesi dei concetti del notebook appena concluso
- **Cosa faremo adesso** — ponte narrativo verso il notebook successivo (tranne l'ultimo)

## Dataset

I notebook usano il **UCI Human Activity Recognition Dataset** ([OpenML id 1478](https://www.openml.org/d/1478)), caricato automaticamente via `sklearn.datasets.fetch_openml`. Il dataset contiene i segnali di accelerometro e giroscopio di 30 volontari che hanno svolto 6 attività diverse (camminare, salire/scendere le scale, seduto, in piedi, sdraiato). Da ogni finestra di 2 secondi sono state estratte 561 feature statistiche.

Nessuna registrazione o account richiesti: il dataset è pubblico e viene scaricato automaticamente da OpenML alla prima esecuzione (circa 25 MB, poi in cache locale).

## Concetti matematici introdotti

- Percettrone: combinazione lineare + funzione di attivazione
- Funzioni di attivazione: sigmoide, ReLU, tangente iperbolica
- Softmax per classificazione multiclasse
- Cross-entropy categoriale come funzione costo
- Backpropagation e regola della catena (intuizione)
- Dropout come regolarizzazione
- Quantizzazione float32 → int8

## Prerequisiti

**Per gli studenti**: aver seguito le lezioni 01 (classificazione k-NN) e 02 (regressione lineare). Non è necessario ricordare tutti i dettagli, ma è utile avere familiarità con i concetti di feature, target, funzione costo, discesa del gradiente e overfitting.

**Setup**: serve un browser e un account Google per Colab (oppure un ambiente Python locale con le librerie sotto). Alla prima esecuzione il dataset viene scaricato automaticamente.

## Esecuzione locale

```bash
pip install numpy pandas matplotlib scikit-learn tensorflow
```

Poi avviare Jupyter e aprire i notebook nell'ordine numerato.

## Note per il docente

- Il notebook 4 (deployment) richiede TensorFlow ≥ 2.9 per la conversione TFLite. In Colab è soddisfatto automaticamente.
- I tempi di training nei notebook 2 e 3 possono variare da 1 a 5 minuti su CPU. Con GPU (Colab gratuito: Runtime → Cambia tipo di runtime → T4 GPU) scendono a pochi secondi.
- Il confronto di velocità nel notebook 3 (`time.time()`) può dare risultati variabili su Colab condiviso: è normale e può essere usato come spunto di discussione.
- Il firmware Arduino nel notebook 4 è pseudocodice didattico: mostra i concetti senza richiedere hardware fisico. Chi vuole, può eseguire il firmware reale su un Arduino Nano 33 BLE Sense usando la libreria [TFLite Micro](https://github.com/tensorflow/tflite-micro).
