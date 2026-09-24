import pandas as pd
def main(): 
    data = { 
        "Месяц": ["Январь", "Февраль", "Март"], 
        "Выручка": [120000, 150000, 135000], 
        } 
    df = pd.DataFrame(data) 
    print(df) 
    
    print("Средняя выручка:", df["Выручка"].mean()) 

def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100
if __name__ == "__main__": main()