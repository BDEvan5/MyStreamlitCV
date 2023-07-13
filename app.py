import streamlit as st


st.set_page_config(page_title="Benjamin's CV", page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Hi, I am benjamin :wave:")
    st.title("An Automation Engineer in South Africa")
    st.write(
        "I enjoy using machine learning, control systems, and data science to solve problems. "
    )
    st.write("[Visit my Webpage >](https://bd-evans.com)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a postdoc at Stellenbosch University in South Africa, where I research:
            - Planning and control architectures for high-speed autonomous racing
            - Deep reinforcement learning for robotic control
            - Optimisation based control (LQR, MPC)
            - State estimation (Kalman filtering)
            """
        )


with st.container():
    st.write("---")
    st.header("My Portfolio Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    # with image_column:
        # st.image(img_lottie_animation)
    with text_column:
        st.subheader("I enjoy building simple projects to demonstrate complex concepts")
        st.write(
            """
            - Deep reinforcement learning algorithms: [GitHub >](https://github.com/BDEvan5/BaselineDRL)
            - Optimisation-based racing (raceline optimisation and MPCC): [GitHub >](https://github.com/BDEvan5/F1TenthRacetrackOptimisation)
            - State estimation with Kalman fitlers: in progress
            """
        )



# with st.container():
#     st.write("---")
#     st.header("My Research Papers")
#     st.write("##")
    # image_column, text_column = st.columns((1, 2))
    # # with image_column:
    #     # st.image(img_lottie_animation)
    # with text_column:
    #     st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
    #     st.write(
    #         """
    #         Learn how to use Lottie Files in Streamlit!
    #         Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
    #         In this tutorial, I'll show you exactly how to do it
    #         """
    #     )


