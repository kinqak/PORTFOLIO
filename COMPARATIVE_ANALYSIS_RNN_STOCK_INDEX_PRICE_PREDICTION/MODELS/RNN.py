import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from itertools import product
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Dropout, LSTM, GRU, SimpleRNN
from tensorflow.keras.callbacks import EarlyStopping

index_name = "MSCI_dm_pandemic" # Instancja danych do analizy

np.random.seed(123)
random.seed(123)
tf.random.set_seed(123)

# Wczytanie danych
index_data = pd.read_excel(f"Data/Pandemic/{index_name}.xlsx")
index_data["Date"] = pd.to_datetime(index_data["Date"])
index_data.set_index("Date", inplace=True)
full_range = pd.date_range(start=index_data.index.min(), end=index_data.index.max(), freq="B")
index_data = index_data.reindex(full_range)
index_data["Price"] = index_data["Price"].ffill()
index_data.index.name = "Date"

# Skalowanie
split_index = len(index_data) - 20
train_data = index_data.iloc[:split_index]
test_data = index_data.iloc[split_index:]

scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(train_data[["Price"]])

train_scaled = scaler.transform(train_data[["Price"]])
test_scaled = scaler.transform(test_data[["Price"]])

# Funkcja tworząca sekwencje
def create_sequences(data, seq_len):
    X, y = [], []
    for i in range(len(data) - seq_len):
        X.append(data[i:i+seq_len])
        y.append(data[i+seq_len])
    return np.array(X), np.array(y)

# Parametry siatki
sequence_lengths = [10, 20, 60]
neuron_options = [32, 64, 96]
num_layers_list = [1, 2, 3]
architectures = ["equal", "triangular"]
batch_sizes = [8, 16, 32]
epoch_values = [10, 30, 50]
dropout_rates = [0.0, 0.2]

results = []
all_model_configs = []
all_predictions = []
all_actuals = []

param_grid = list(product(sequence_lengths, neuron_options, num_layers_list, architectures, batch_sizes, epoch_values, dropout_rates))

# Pętla po konfiguracjach
for sequence_length, base_neurons, num_layers, arch, batch_size, epochs, dropout_rate in param_grid:

    X_train, y_train = create_sequences(train_scaled, sequence_length)
    X_test, y_test = create_sequences(test_scaled, sequence_length)
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    model = Sequential()
    model.add(Input(shape=(sequence_length, 1)))  

    for i in range(num_layers):
        return_seq = i < num_layers - 1
        units = base_neurons if arch == "equal" else max(1, base_neurons // (2**i))
        model.add(SimpleRNN(units, return_sequences=return_seq))
        if dropout_rate > 0:
            model.add(Dropout(dropout_rate))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2, verbose=0, callbacks=[early_stop], shuffle=False)

    predicted = model.predict(X_test)
    predicted_prices = scaler.inverse_transform(predicted).flatten()        
    actual_prices = scaler.inverse_transform(y_test.reshape(-1, 1)).flatten() 

    mae = mean_absolute_error(actual_prices, predicted_prices)
    mse = mean_squared_error(actual_prices, predicted_prices)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((actual_prices - predicted_prices) / actual_prices)) * 100
    r2 = r2_score(actual_prices, predicted_prices)

    results.append({
        "sequence_length": sequence_length,
        "base_neurons": base_neurons,
        "layers": num_layers,
        "architecture": arch,
        "batch_size": batch_size,
        "epochs": epochs,
        "dropout_rate": dropout_rate,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "MAPE": mape,
        "R2": r2
    })

    all_model_configs.append({
        "params": (sequence_length, base_neurons, num_layers, arch, batch_size, epochs, dropout_rate),
        "history": history.history
    })

    all_predictions.append(predicted_prices.tolist())
    all_actuals.append(actual_prices.tolist())

# Zapis wyników
pd.DataFrame(results).to_excel(f"Results_RNN_{index_name}.xlsx", index=False)

os.makedirs(f"Plots/{index_name}_RNN/loss", exist_ok=True)
os.makedirs(f"Plots/{index_name}_RNN/forecast", exist_ok=True)

combined = list(zip(results, all_model_configs, all_predictions, all_actuals))

sorted_combined = sorted(combined, key=lambda x: x[0]["RMSE"])[:10]

for i, (res, config, pred, actual) in enumerate(sorted_combined, start=1):
    history = config["history"]
    params = res

    filename_suffix = (
        f"seq{params['sequence_length']}_neu{params['base_neurons']}_lay{params['layers']}_"
        f"arch_{params['architecture']}_bs{params['batch_size']}_ep{params['epochs']}_dr{params['dropout_rate']}"
    )

    # Wykres funkcji straty 
    plt.figure(figsize=(8, 4))
    plt.plot(history['loss'], label='Strata treningowa', color='black', linewidth=2)
    plt.plot(history['val_loss'], label='Strata walidacyjna', color='darkred', linewidth=2)
    plt.title(f"RNN - Funkcja straty MSE (Model {i})")  
    plt.xlabel("Epoka")
    plt.ylabel("Strata (MSE)")
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    plt.tight_layout()
    plt.savefig(f"Plots/{index_name}_RNN/loss/loss_model_{i}_RNN_{filename_suffix}.png")  
    plt.close()

    # Wykres prognozy
    last_dates = index_data.index[-len(actual):]
    plt.figure(figsize=(10, 5))
    plt.plot(last_dates, actual, label='Wartości rzeczywiste', color='black', linewidth=2)
    plt.plot(last_dates, pred, label='Wartości prognozowane (RNN)', color='darkred', linewidth=2) 
    plt.title(f"RNN - Prognoza ceny zamknięcia (Model {i})")  
    plt.xlabel("Data")
    plt.ylabel("Cena zamknięcia")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.tight_layout()
    plt.savefig(f"Plots/{index_name}_RNN/forecast/forecast_model_{i}_RNN_{filename_suffix}.png")  
    plt.close()
