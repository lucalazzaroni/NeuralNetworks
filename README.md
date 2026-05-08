# Reti Neurali: dall'idea al dispositivo

Materiale didattico per un'introduzione alle **reti neurali artificiali** tramite un problema di riconoscimento di attività fisiche.

Gli studenti vestono i panni del team di ingegneria di WristMind, una startup che deve costruire un braccialetto intelligente capace di riconoscere cosa stai facendo (camminare, correre, riposare) direttamente sul chip al polso, senza connessione internet. Partendo da un singolo neurone artificiale, si arriva in quattro tappe a costruire una rete neurale completa e a effettuare il deployment su un microcontrollore reale.

## Struttura del minicorso

| # | Notebook | Tema |
|---|---|---|
| 1 | `01-il_neurone.ipynb` | Il percettrone: dal neurone biologico all'artificiale, funzioni di attivazione, classificazione binaria (riposo vs. movimento) con Keras |
| 2 | `02-la_rete_si_fa_profonda.ipynb` | Multi-Layer Perceptron: strati nascosti, backpropagation, classificazione multiclasse (6 attività), matrice di confusione, softmax |
| 3 | `03-sfida_tra_modelli.ipynb` | Regressione con reti neurali, confronto NN vs. k-NN vs. modello lineare, overfitting nelle reti grandi, Dropout |
| 4 | `04-dal_laboratorio_al_dispositivo.ipynb` | Deployment su dispositivi embedded: TensorFlow Lite, quantizzazione int8, deployment STM32, Edge AI |

## Obiettivi di apprendimento

Al termine della lezione lo studente sarà in grado di:

- conoscere il percettrone come generalizzazione del modello lineare con funzione di attivazione;
- spiegare intuitivamente come funziona l'addestramento di una rete neurale;
- leggere le curve di apprendimento e riconoscere i segnali di overfitting;
- conoscere il processo di deployment su dispositivi embedded.

## Dataset

I notebook usano il **UCI Human Activity Recognition Dataset** ([OpenML id 1478](https://www.openml.org/d/1478)), caricato automaticamente via `sklearn.datasets.fetch_openml`. Il dataset contiene i segnali di accelerometro e giroscopio di 30 volontari che hanno svolto 6 attività diverse (camminare, salire/scendere le scale, seduto, in piedi, sdraiato). Da ogni finestra di 2 secondi sono state estratte 561 feature statistiche.

## Concetti matematici introdotti

- Percettrone: combinazione lineare + funzione di attivazione
- Funzioni di attivazione: sigmoide, ReLU, tangente iperbolica
- Softmax per classificazione multiclasse
- Cross-entropy categoriale come funzione costo
- Backpropagation e regola della catena (intuizione)
- Dropout come regolarizzazione
- Quantizzazione float32 → int8
- Deployment su microcontrollore: STM32Cube.AI

## Prerequisiti

**Per gli studenti**: aver seguito le lezioni 01 (classificazione k-NN) e 02 (regressione lineare). Non è necessario ricordare tutti i dettagli, ma è utile avere familiarità con i concetti di feature, target, funzione costo, discesa del gradiente e overfitting.

**Setup**: serve un browser e un account Google per Colab (oppure un ambiente Python locale con le librerie sotto). Alla prima esecuzione il dataset viene scaricato automaticamente.