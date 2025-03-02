import streamlit as st
st.image("logo.png", width=200)
def calculate_volume(series, weights, doubles):
    total_volume = sum(w * (2 if d else 1) for w, d in zip(weights, doubles)) * series
    return total_volume

def main():
    st.title("Kettlebell Sport - Kalkulator Objętości Treningowej")
    
    # Wybór ilości serii
    series = st.selectbox("Wybierz ilość serii:", list(range(1, 21)))
    
    weights = []
    doubles = []
    
    # Użytkownik wybiera ciężar dla każdej serii
    for i in range(series):
        st.subheader(f"Seria {i+1}")
        weight = st.selectbox(f"Wybierz wagę odważnika (Seria {i+1}):", list(range(4, 50, 2)), key=f'weight_{i}')
        double = st.checkbox(f"Dwa odważniki? (Seria {i+1})", key=f'double_{i}')
        
        weights.append(weight)
        doubles.append(double)
    
    if st.button("Oblicz objętość"):
        total_volume = calculate_volume(series, weights, doubles)
        st.success(f"Całkowita objętość treningowa: {total_volume} kg")

if __name__ == "__main__":
    main()