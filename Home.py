from dependencies import *


def app():
    db = Database()
    st.session_state.sent = ""
    updates = fetch_log()
    center_title(70, "#0C2637", "Notes for CSE-Cybersecurity <br>Batch 2022-2026")

    center_title(30, "black", "This page is made for downloading the notes for the 4th Semester for the following subjects <br>")

    st.header(":red[Recently Added notes]👇")
    st.markdown("###")
    with st.container(height=250, border=False):

        for i in reversed(updates):
            st.success(i, icon="✅")
    """with st.sidebar:
        st.markdown("---")
        center_title(35, "black", "Get Notified 🔔")
        email = st.text_input(label="E-Mail", key="email")
        name = st.text_input(label="Name", key="name")

        if email and name != "":
            email_b = st.button("Verify Email", use_container_width=True)
            if email_b:
                global comp_otp
                comp_otp = db.send_mail(To=email)
                st.success(f"6 Digit OTP has been sent to {email[:5]}***{email[-13:]}")
                st.session_state.sent = "sent"

            otp = st.text_input(label="One Time Password")

            if st.button("Subscribe", use_container_width=True):
                if otp == comp_otp:

                    db.email(email, name)
                else:
                    st.error("Error Verifying OTP")"""
