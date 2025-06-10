from pyngrok import ngrok

# Run the app
!streamlit run app.py &

# Expose via ngrok
public_url = ngrok.connect(port=8501)
print(f"🌐 Your Streamlit app is live at: {public_url}")
