import streamlit as st

def coinGame(x:int, y:int) -> int:
    if x>2 and y==0:
        return 0
    if y==1 and x>3:
        return 1
    elif y%2!=0:
        if 3*y-x==0:
            return 1
        elif 3*y>x:
            if (x//3)%2==0:
                return 0
            else:
                return 1  
        elif 3*y<x:
            return 1
    elif y%2==0:
        if 3*y-x==0:
            return 0
        elif 3*y>x:
            if (x//3)%2==0:
                return 0
            else:
                return 1
        elif 3*y<x:
            return 0
res=coinGame(1235644 ,345322)
print(res)
st.title("Coin Game Solver")

# User Input
x = st.number_input("Enter value for x", min_value=0, step=1, value=0)
y = st.number_input("Enter value for y", min_value=0, step=1, value=0)

# Calculate Result
if st.button("Calculate Result"):
    result = coinGame(x, y)
    st.write(f"The result is: {result}")
