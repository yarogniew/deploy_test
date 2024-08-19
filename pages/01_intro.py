import streamlit as st
import time
st.title("To jest strona Iwony Milewskiej")
col1, col2 = st.columns([1, 1])


col1.markdown("## Witam na stronie Iwonki!")
col1.markdown("Więcej o stronie: [iwonamilewska.pl](https://iwonamilewska.pl/)")

with st.expander("Code (expander)"):
    st.code('''
    @app.route('/process', methods=['POST'])
    def process_data():
        content = request.json
        if content and 'value' in content:
            processed_data = {'result': content['value'] * 2}
            return jsonify(processed_data)  # Upewnij się, że zwracasz JSON
        else:
            return jsonify({'error': 'Invalid input'}), 400  # Obsłuż błędne dane wejściowe''', language='python')