import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Simple Scatter Plot App")
    st.write("Enter your data below and click on 'Generate Plot' to create a scatter plot.")

    data = get_user_input()

    if data is not None:
        st.subheader("Scatter Plot")
        create_scatter_plot(data)

def get_user_input():
    st.subheader("Enter Data")
    data = st.text_area("Input format: 'x1, y1\nx2, y2\n...'", height=200)
    
    if st.button("Generate Plot"):
        if data:
            data = data.strip()
            lines = data.split("\n")
            xy_data = [line.split(",") for line in lines]
            try:
                x_values = [float(item[0].strip()) for item in xy_data]
                y_values = [float(item[1].strip()) for item in xy_data]
                data = pd.DataFrame({"x": x_values, "y": y_values})
            except ValueError:
                st.error("Invalid data format. Please provide data in 'x, y' format.")
                data = None
        else:
            st.error("Please enter data in 'x, y' format.")
            data = None
    else:
        data = None

    return data

def create_scatter_plot(data):
    fig, ax = plt.subplots()
    ax.scatter(data["x"], data["y"])
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Scatter Plot")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
