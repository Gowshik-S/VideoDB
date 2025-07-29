import streamlit as st

from ..auth import sign_in


def main():
    st.title("🔐 Login")
    st.write("Welcome back! Please enter your credentials.")

    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", type="primary"):
        if not email or not password:
            st.warning("Please provide both email and password.")
            st.stop()
        try:
            user = sign_in(email, password)
            st.session_state["id_token"] = user["idToken"]
            st.session_state["user"] = user
            st.success("Successfully logged in! 🚀")
            st.experimental_set_query_params()  # Clear URL params
            st.experimental_rerun()
        except Exception as exc:
            st.error(f"Login failed: {exc}")

    st.info("Don't have an account? Choose the **Sign Up** page from the sidebar.")


if __name__ == "__main__":
    main()