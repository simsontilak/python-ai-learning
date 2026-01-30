import csv
import json
from datetime import datetime

def log_metrics(filename, accuracy, loss):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(),accuracy,loss])
        print("Metrics logged successfully.")

def save_config(config_filename, model_params):
    with open(config_filename, "w") as file:
        json.dump(model_params, file,indent=4)
    print("Config saved successfully")

def main():
    log_metrics("../data/training_log.csv",0.95,0.07)
    save_config("../data/model_config.json", 
        {"layers":[64,32,10],
         "optimizer": "adam",
         "epochs:":20})
    
if __name__ == "__main__":
    main()