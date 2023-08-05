import streamlit as st
import pandas as pd
my_dict = {"date":[],"name":[]};
import datetime

# using now() to get current time
import hashlib
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username):
    current_time = datetime.datetime.now()
    my_dict["date"].append(current_time)
    my_dict["name"].append(username)

def login_user(username):
    
    return my_dict


def view_all_users():
    return (my_dict)



def main():
    """Simple Login App"""

    st.title("Simple Login App")

    menu = ["Home","Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
        # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:

                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics")
                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")





    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")

        if st.button("Signup"):
            date = datetime.datetime.now()
            #create_usertable()
            add_userdata(new_user)
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
            username = st.sidebar.text_input("User Name")

            result = login_user(username)
            if result:

                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics")
                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns=["Username"])
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")



if __name__ == '__main__':
    main()