import streamlit as st

st.set_page_config(
    page_title='BMI Calculator',
    page_icon='📆'
)

st.title('BMI CALCULATOR')
st.subheader(':grey[Here you can calculate your BMI]',divider='green')

height= st.number_input('Enter Your Height In cm:')
weight= st.number_input('Enter Your Weight In kg:')

if st.button('Calculate BMI'):
    if height>0 and weight>0:
        bmi= weight/height**2 *10000
        st.success(f'Your BMI is {bmi:.2f}')
        if bmi<18.5:
            st.warning('You are under-weight.')
        elif 18.5 <= bmi <25:
            st.info('you have a normal weight.')
        else:
            st.error('You are over-weight')
    else:
        st.error('Please enter valid height or weight')
