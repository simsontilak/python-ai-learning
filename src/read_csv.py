import csv
import pandas as pd

def read_rows():
    with open("data/student.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            

def read_rows_dict():
    with open("data/student.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"],"=>",row["score"])
            
def write_rows_dict():
    students = [
        {"Name":"AKil","Age":44,"Score":56.2},
        {"Name":"Sandy","Age":54,"Score":51.2},
        {"Name":"Raj","Age":64,"Score":52.2}
    ]
    with open("data/new_student.csv","w") as file:
        field_names = ["Name","Age","Score"]
        writer = csv.DictWriter(file,fieldnames=field_names)
        writer.writeheader()
        writer.writerows(students)

def read_using_pandas():
    data = pd.read_csv("data/new_student.csv")
    print(data)
    print(data["Name"])
    print(data.describe())
        
            
def main():
    read_rows()
    read_rows_dict()
    write_rows_dict()
    read_using_pandas()

if __name__ == "__main__":
    main()
