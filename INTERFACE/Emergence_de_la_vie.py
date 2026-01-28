import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from st_flexible_callout_elements import flexible_callout
from pathlib import Path

st.set_page_config(layout="wide")

IMG_DIR = Path(__file__).parent

st.header("Emergence de la vie : application à la chimie prébiotique.", divider="gray")

st.markdown("## Introduction : ")

def ancre(name, offset=80):
    st.markdown(
        f"""
        <div id="{name}" style="
            position: relative;
            top: -{offset}px;
            visibility: hidden;
        "></div>
        """,
        unsafe_allow_html=True
    )

ancre("origine-de-la-vie")
st.markdown("## Origine de la vie : ")

st.markdown("""
            L'origine de la vie est une **question fascinante** par la part de **mystère** qu'elle englobe et la multitude de **processus complexes** qu'elle implique.
            Dans cette **"soupe prébiotique"** que l'on s'imagine, l’émergence de la vie peut être perçue comme une **transition** entre un **régime d’entités primaires hors équilibre** et un **régime d’entités composites**, 
            dont la stabilité et l'organisation seraient constraintes par des **mécanismes physiques et chimiques**. 
""")

col1, col2, col3 = st.columns([1, 2, 1]) 
with col1:
    st.image(IMG_DIR / "desordre_ordre.png", caption = "Figure 1 : Soupe prébiotique. Passage d'un régime d'entités primaires hors équilibre à un régime d'entités composites contraint par la thermodynamique. ", width = 600)

st.markdown(""" 

            Le vivant peut être justement caractérisé par son **organisation structurée et dynamique**, 
            sa capacité à se **reproduire**, mais **surtout** sa capacité à **évoluer**. A partir de ces éléments constitutifs du vivant plusieurs **théories** ont été formalisées, ayant pour but d'expliquer en partie l'émergence de la vie, dont la théorie sur les **cycles autocatalytiques**. \n\n  

            """)

ancre("cycles-autocatalytiques")
st.markdown("## Pourquoi les cycles autocatalytiques ? ")


st.markdown("""
            
            La propriété du vivant à **se maintenir lui-même** et à **se reproduire** est en effet reprise par la **théorie des cycles autocatalytiques**.
            La vie est en effet d'abord faite de **cycles**, qui se répètent indéfiniment. La reproduction, constitutive du vivant, est en elle même un cycle, 
            par exemple l'oeuf donne naissance à la poule qui pond un nouvel œuf et ainsi de suite. 
            Dans l'**autocatalyse**, une molécule catalyse sa **propre production**, ainsi la reproduction est bien une **forme élaborée** de l'autocatalyse.

""")

col1, col2, col3 = st.columns([1, 2, 1])  
with col1:
    st.image(IMG_DIR / "figure1.png", caption="Figure 2 : Parallèle entre un cycle autocatalytique à gauche et un cycle de vie simplifié, chez la poule, à droite. L'image de gauche est extraite d'une présentation de Denis Kuperberg : Complexity of detecting autocatalysis in chemical reaction networks (2025)", width=600)


st.markdown("""

            L'**autocatalyse** peut être considérée comme un **acteur clé** des dynamiques prébiotiques, notamment du fait de son caractère **auto-amplifiant**. 
            Celui-ci est **fondamental**, car il fournit un mécanisme par lequel des systèmes chimiques peuvent **se maintenir**, **croître** et, éventuellement, 
            **tendre** vers des structures de plus en plus complexes. 

            De plus, au sein d'organismes actuels, des **vestiges** de ces **cycles autocatalytiques** ont pu être découverts [1], 
            ce qui souligne à nouveau le fait qu'ils ont pu jouer un rôle très important dans le monde prébiotique. 

            Les **cycles autocatalytiques** étant des systèmes, nous pourrions aussi nous demander si nous pouvons les assimiler à des **espèces** et imaginer des **relations écologiques** entre
            ces cycles via leur environnement. Par exemple, puisqu'un cycle peut **modifier son environnement** en **consommant une ressource**, est-ce qu'il peut interagir avec un autre cycle
            qui utiliserait ou produirait cette ressource ? Est-ce que nous pourrions voir émerger des concepts empruntés à l'écologie 
            comme la **compétition** ou la **coexistence** chez les **cycles autocatalytiques** ? 
            
            Mais pour tenter de comprendre en partie l'**émergence de la vie**, nous nous demanderons en particulier ici si ces **cycles autocatalytiques** peuvent **évoluer**. 
            Autrement dit, si ces cycles peuvent présenter des **variations, des mutations** héritables. 
            Pour cela, nous pourrions par la suite imaginer et **modéliser** une **entité mutante** construite à partir d'une **entité résidante autocatalytique**
            et observer le comportement de ce mutant au sein du cycle autocatalytique, il pourrait par exemple à son tour s'auto-amplifier par l'intermédiaire 
            d'un autre cycle autocatalytique mutant.
            
            Nous aborderons en détail la mutation des cycles dans la partie **Simulations**. 

""")





def sidebar_button(label, anchor, bg="#A8DADC", color="#457B9D"):
    st.sidebar.markdown(
        f"""
        <a href="#{anchor}" style="text-decoration:none;">
            <div style="
                background-color:{bg};
                color:{color};
                padding:12px;
                margin-bottom:8px;
                border-radius:25px;
                font-weight:600;
                text-align:left;
                cursor:pointer;
            ">
                 {label}
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

sidebar_button("Origine de la vie", "origine-de-la-vie")
sidebar_button("Pourquoi les cycles autocatalytiques ?","cycles-autocatalytiques")

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
        <hr>
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
