import streamlit as st

# Function to analyze heart rate
def analyze_heart_rate(heart_rate):
    if heart_rate < 60:
        return "Low Heart Rate", "Consider consulting a doctor as this may indicate bradycardia."
    elif 60 <= heart_rate <= 100:
        return "Normal Heart Rate", "Your heart rate is within the normal range."
    elif 100 < heart_rate <= 120:
        return "Elevated Heart Rate", "Your heart rate is slightly elevated. Relax and monitor your rate."
    else:
        return "High Heart Rate", "Your heart rate is high. Consult a healthcare provider."

# Main function
def main():
    st.title("Heart Rate Monitoring System")
    
    st.header("Enter Your Heart Rate")
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=0, step=1)
    
    if st.button("Analyze Heart Rate"):
        status, advice = analyze_heart_rate(heart_rate)
        st.write(f"**Heart Rate Status**: {status}")
        st.write(f"**Health Advice**: {advice}")
        
        # Visual feedback
        if status == "Low Heart Rate":
            st.warning(advice)
        elif status == "Normal Heart Rate":
            st.success(advice)
        elif status == "Elevated Heart Rate":
            st.info(advice)
        else:
            st.error(advice)

if __name__ == "__main__":
    main()
