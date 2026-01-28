import streamlit as st


st.header("Bibliographie", divider="gray")

st.markdown(""" 

            * [1] Xavier, J. C., Hordijk, W., Kauffman, S., Steel, M. et Martin, W. F. (2020). Autocatalytic chemical networks at the origin of metabolism. Proceedings of the Royal
            Society B : Biological Sciences, 287(1922):20192377.

            * [2] T. Kosc, D. Kuperberg, E. Rajon, S. Charlat, Thermodynamic consistency of autocatalytic 
            cycles. Proc. Natl. Acad. Sci. U.S.A. 122 (2025). 

""")

st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"] > div:first-child {
        display: flex;
        flex-direction: column;
        height: 100vh;
    }

    .sidebar-content {
        flex: 1;
    }

    .sidebar-footer {
        font-size: 0.85em;
        color: #666;
        text-align: center;
        padding-bottom: 20px;
    }
    </style>

    <div class="sidebar-content"></div>

    <div class="sidebar-footer">
        <strong>Interface développée par :</strong><br>
        Ifssan SAIRI<br>
        <em>M2 MODE</em><br>
        <em>Année universitaire 2025–2026</em>
        <hr>
        <strong>Projet encadré par :</strong> 
        <span class="encadrants">Sylvain CHARLAT, Etienne RAJON, Denis KUPERBERG</span>
    </div>
    """,
    unsafe_allow_html=True
)
