import streamlit as st

from ..auth import sign_up


def main():
    st.title("🆕 Sign Up")
    st.write("Create a new VidCraftAI account.")

    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")
    confirm = st.text_input("Confirm Password", type="password", key="signup_confirm")

    if st.button("Create Account", type="primary"):
        if not email or not password:
            st.warning("Please provide both email and password.")
            st.stop()
        if password != confirm:
            st.warning("Passwords do not match.")
            st.stop()
        try:
            user = sign_up(email, password)
            st.success("Account created successfully! You can now log in from the sidebar.")
            st.balloons()
        except Exception as exc:
            st.error(f"Sign-up failed: {exc}")

    st.info("Already have an account? Go to the **Login** page from the sidebar.")


if __name__ == "__main__":
    main()