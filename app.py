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
    left_column, _, right_column = st.columns((2.5, 0.8, 2))
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
    with right_column:
        st.subheader("Research Statement")
        st.write(
            """
            I research how machine learning methods can be applied
            in the real world. I am passionate about using classical and
            machine-learning approaches to engineer solutions to complex problems. Currently, I work on developing high-performance,
            robust, safe solutions for autonomous robotic control.
            """
        )


with st.container():
    st.write("---")
    st.header("My Portfolio Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 4))
    # with image_column:
        # st.image(img_lottie_animation)
    st.write("Simple projects to demonstrate complex concepts")
    with text_column:
        st.write(
            """
            - Deep reinforcement learning algorithms: [GitHub >](https://github.com/BDEvan5/BaselineDRL)
            - Optimisation-based racing (raceline optimisation and MPCC): [GitHub >](https://github.com/BDEvan5/F1TenthRacetrackOptimisation)
            - State estimation with Kalman fitlers: in progress
            """
        )



with st.container():
    st.write("---")
    st.header("My Research Papers")
    st.write("##")
    st.write(f"- Safe reinforcement learning for high-speed autonomous racing. *Cognitvie Robotics, 2023*")
    st.write(f"- High-speed Autonomous Racing using Trajectory-aided Deep Reinforcement Learning. *Robotics and Automation Letters, 2023*")



