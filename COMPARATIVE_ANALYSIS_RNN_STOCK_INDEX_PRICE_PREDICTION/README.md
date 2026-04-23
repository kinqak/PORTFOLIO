# Forecasting Stock Market Indices Using RNN, LSTM and GRU Networks

This repository contains the implementation and results of a research project focused on forecasting stock market index values using recurrent neural network architectures: RNN, LSTM, and GRU.

The primary objectives of this project are to:

- Evaluate the effectiveness of RNN-based models in time series forecasting of financial indices,  
- Compare predictive performance across developed and emerging markets,  
- Analyze model robustness across three distinct macroeconomic periods.

## Data Description

The dataset consists of daily closing prices from:

- **MSCI World Index** – representing developed markets,  
- **MSCI Emerging Markets Index** – representing emerging markets.

The data is segmented into three economic periods:

1. **Stable period** – before the COVID-19 pandemic (2018–2019),  
2. **Pandemic period** – during the global COVID-19 shock (2020–2021),  
3. **War period** – reflecting the impact of the Russian invasion of Ukraine (2022).

## Implemented Models

- SimpleRNN (vanilla recurrent neural network)  
- Long Short-Term Memory (LSTM)  
- Gated Recurrent Unit (GRU)

## REPOSITORY STRUCTURE

- `DATA/` – input time series (MSCI World, Emerging; Stable, Pandemic, War).  
- `MODELS/` – training scripts for SimpleRNN, LSTM, GRU.  
- `RESULTS/` – simulation outputs: model type, hyperparameters, evaluation metrics (MAE, RMSE, etc.).
- `Kinga_Kolodziej_415255.pdf` – full bachelor's thesis

