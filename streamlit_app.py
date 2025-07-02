import streamlit as st

def print_left(items):
    return [f"Pick up the {i} with the left hand and drop it in the bin" for i in items]

def print_right(items):
    return [f"Pick up the {i} with the right hand and drop it in the bin" for i in items]

st.set_page_config(page_title="Mobile Pick Bridge", layout="centered")
st.title("🦾 Mobile Pick Bridge")
st.write("Enter items to generate pick instructions for both hands.")

count = st.number_input("How many items would you like to enter?", min_value=1, step=1)

items = []
with st.form("item_form"):
    for i in range(int(count)):
        item = st.text_input(f"Item #{i + 1}", key=f"item_{i}")
        items.append(item)

    submitted = st.form_submit_button("Generate Instructions")

if submitted:
    if all(item.strip() for item in items):
        st.subheader("Instructions:")
        st.text("\n".join(print_left(items)))
        st.text("\n".join(print_right(items)))
    else:
        st.error("Please fill in all item fields before generating instructions.")
