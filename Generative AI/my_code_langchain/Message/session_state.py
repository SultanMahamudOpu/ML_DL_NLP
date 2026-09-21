import streamlit as st

st.header('Session State Demo')

# যদি session_state এর মধ্যে count না থাকে, মানে শুধু প্রথম বারই count = 0 হবে। তারপর থেকে আর এটা 0 হবে না। মানে এর value update হতে থাকবে
if 'count' not in st.session_state:
    st.session_state.count = 0
    
    
st.write(f'Current count {st.session_state.count}')

if st.button('Increase'):
    st.session_state.count += 1
if st.button('Decrease'):
    st.session_state.count -= 1
if st.button('Reset'):
    st.session_state.count = 0
    
st.write(f'Updated count {st.session_state.count}')
st.write(f'Printing session state {st.session_state}')