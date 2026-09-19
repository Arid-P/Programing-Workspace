import streamlit as st
import pandas as pd
from school_models import student, teacher

# --- Page Configuration ---
st.set_page_config(page_title="School Management 3.0", layout="wide")

st.title("🏫 School Management System 3.0")
st.markdown("---")

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigation", ["Students", "Teachers"])

# --- Helper Function to Refresh Data ---
def get_student_df():
    data = student.view_students()
    return pd.DataFrame([{"ID": s.id, "Name": s.name, "Phone": s.phone_number, "Grade": s.grade} for s in data])

def get_teacher_df():
    data = teacher.view_teacher()
    return pd.DataFrame([{"ID": t.id, "Name": t.name, "Phone": t.phone_number, "Subject": t.subject} for t in data])

# --- Student Management Section ---
if menu == "Students":
    st.header("👨‍🎓 Student Management")
    
    # View and Search
    df = get_student_df()
    search = st.text_input("Search Student by Name", "")
    if search:
        df = df[df['Name'].str.contains(search, case=False)]
    
    st.dataframe(df, use_container_width=True)

    # Actions: Add, Update, Delete
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Add Student")
        with st.form("add_student"):
            name = st.text_input("Full Name")
            phone = st.text_input("Phone Number")
            grade = st.selectbox("Grade", [f"{i}-{s}" for i in range(1,13) for s in "ABCD"])
            if st.form_submit_button("Submit"):
                if student.add_student(name, phone, grade):
                    st.success(f"Added {name}")
                    st.rerun()

    with col2:
        st.subheader("Update Record")
        if not df.empty:
            target_id = st.selectbox("Select ID to Update", df['ID'])
            field = st.selectbox("Field", ["Name", "Phone", "Grade"])
            new_val = st.text_input("New Value")
            field_map = {"Name": 1, "Phone": 2, "Grade": 3}
            if st.button("Update Student"):
                if student.update_student(target_id, field_map[field], new_val):
                    st.success("Updated!")
                    st.rerun()

    with col3:
        st.subheader("Delete Record")
        if not df.empty:
            del_id = st.selectbox("Select ID to Delete", df['ID'], key="del_stu")
            if st.button("Confirm Delete", type="primary"):
                if student.delete_student(del_id):
                    st.warning("Deleted!")
                    st.rerun()

# --- Teacher Management Section ---
elif menu == "Teachers":
    st.header("👩‍🏫 Teacher Management")
    
    df = get_teacher_df()
    st.dataframe(df, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Add Teacher")
        with st.form("add_teacher"):
            name = st.text_input("Full Name")
            phone = st.text_input("Phone Number")
            subject = st.text_input("Subject")
            if st.form_submit_button("Submit"):
                if teacher.add_teacher(name, phone, subject):
                    st.success(f"Added {name}")
                    st.rerun()

    with col2:
        st.subheader("Update Record")
        if not df.empty:
            target_id = st.selectbox("Select ID to Update", df['ID'])
            field = st.selectbox("Field", ["Name", "Phone", "Subject"])
            new_val = st.text_input("New Value")
            field_map = {"Name": 1, "Phone": 2, "Subject": 3}
            if st.button("Update Teacher"):
                if teacher.update_teacher(target_id, field_map[field], new_val):
                    st.success("Updated!")
                    st.rerun()

    with col3:
        st.subheader("Delete Record")
        if not df.empty:
            del_id = st.selectbox("Select ID to Delete", df['ID'], key="del_tea")
            if st.button("Confirm Delete", type="primary"):
                if teacher.delete_teacher(del_id):
                    st.warning("Deleted!")
                    st.rerun()