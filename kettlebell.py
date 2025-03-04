import streamlit as st
#import plotly.express as px

st.image("logo.png", width=200)

def calculate_series_volume(weights, doubles, repetitions):
    return [w * (2 if d else 1) * r for w, d, r in zip(weights, doubles, repetitions)]

def main():
    st.title("Kettlebell Sport - Kalkulator Objętości Treningowej")
    
    # Wybór ilości serii
    series = st.selectbox("Wybierz ilość serii:", list(range(1, 21)))
    
    weights = []
    doubles = []
    repetitions = []
    
    # Użytkownik wybiera ciężar, ilość powtórzeń i czy używa dwóch odważników
    for i in range(series):
        st.subheader(f"Seria {i+1}")
        weight = st.selectbox(f"Wybierz wagę odważnika (Seria {i+1}):", list(range(4, 50, 2)), key=f'weight_{i}')
        double = st.checkbox(f"Dwa odważniki? (Seria {i+1})", key=f'double_{i}')
        repetition = st.number_input(f"Ilość powtórzeń (Seria {i+1}):", min_value=1, max_value=500, key=f'repetition_{i}')
        
        weights.append(weight)
        doubles.append(double)
        repetitions.append(repetition)
    
    if st.button("Oblicz objętość"):
        series_volumes = calculate_series_volume(weights, doubles, repetitions)
        total_volume = sum(series_volumes)
        
        # Wyświetlenie wyniku
        st.success(f"Całkowita objętość treningowa: {total_volume} kg")
        
        # Tworzenie wykresu
        fig = st.plotly_chart(x=list(range(1, series + 1)), y=series_volumes, labels={'x': 'Seria', 'y': 'Objętość (kg)'},
                     title="Objętość treningowa dla każdej serii", text=series_volumes)
        fig.update_traces(textposition="outside")
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
