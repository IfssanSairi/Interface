import streamlit as st
from pathlib import Path
from st_flexible_callout_elements import flexible_callout

st.header("Théorie : chimie des cycles autocatalytiques", divider="gray")

IMG_DIR = Path(__file__).parent

st.markdown("## Introduction")

st.markdown("### Catalyse ")

col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.image(IMG_DIR / "Catalyse.png", caption="Figure 3 : Réaction de **catalyse**. L'entité primaire $A$ est consommée dans la première réaction et produite dans la dernière, son **bilan chimique** est **nul**. C'est le **catalyseur**.", width=450)


st.markdown(""" L'idée est que la réaction chimique $A + B \\rightarrow AB$ **ne peut pas se réaliser** d'un point de vue **cinétique** (freinée par une barrière d'activation trop élevée). 
            En revanche, d'autres réactions peuvent elles se réaliser car plus **favorables cinétiquement** (barrières d'activation plus basses) et produire l'entité $AB$. Elles font intervenir d'autres entités, notamment un **catalyseur**. 
            """)

st.markdown("### Autocatalyse")

col1, col2, col3 = st.columns([1, 2, 1])  
with col2:
    st.image(IMG_DIR / "Cycle.drawio.png", caption="Figure 4 : Schéma d'un cycle autocatalytique minimal. $\mathrm{AB}$, $\mathrm{(AB)A}$ et $\mathrm{(AB)(AB)}$ représentent les espèces coeurs du motif, $\mathrm{AB}$ est l'espèce autocatalytique. $\mathrm{A}$ et $\mathrm{B}$ servent de nourriture.", width=500)

st.markdown(
    """
    Le principe pour l'**autocatalyse** est le même que celui de la **catalyse**, en revanche cette fois le **catalyseur** est aussi un **produit de la réaction catalysée**.
    Ainsi, une composante unique de l'autocatalyse est qu'elle a nécessairement lieu en présence de produits. La suite de réactions peut donc être représentée au sein d'un cycle, d'où le terme de **cycle autocatalytique**.
""")

st.markdown("## Equations de réactions")

st.markdown('''
<style>
.katex-html {
    text-align: center;
}
</style>''',
unsafe_allow_html=True
)

st.markdown(""" 
            Prenons d'abord un exemple simple avec le **cycle autocatalytique du formose**, considéré comme le **cycle autocatalytique le plus simple** [2].  
            La réaction qui ne peut pas se faire est la suivante :  
""")
st.latex(r'''C + C \xrightleftharpoons[k_{-1}]{k_1} C_{2}''')

st.markdown("""
            L'ensemble des réactions qui peuvent se faire et qui composent le **cycle autocatalytique** sont les suivantes : 
""")

st.latex(r'''C_{2} + C \xrightleftharpoons[k_{-2}]{k_2} C_{3}''')
st.latex(r'''C_{3} + C \xrightleftharpoons[k_{-3}]{k_3} C_{4}''')
st.latex(r'''C_{4} \xrightleftharpoons[k_{-4}]{k_4} C_{2} + C_{2}''')

st.markdown(""" 
            Par la suite, nous nous intéresserons à un cas **plus complexe** de ces **cycles autocatalytiques**, sur lesquels, **contrairement** au **cycle du formose**, 
            nous pourrions créer des **mutants**. Pour cela, nous allons détailler les réactions de ce cycle plus complexe en se focalisant davantage 
            sur les **liaisons hydrogène** et **covalentes** qui y interviennent : 
""")

st.write(f"a.) **Liaison** **hydrogène** entre A et AB (où les 2 A se lient ensemble):")

col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.latex(r'''AB + A \xrightleftharpoons[k_{-1}]{k_1} (AB)A''')
    st.image(IMG_DIR / "Reaction_1.drawio.png", caption="Figure 5 : Réaction 1 d'un cycle autocatalytique minimal.", width=400)

st.write(f"b.) **Liaison** **hydrogène** entre B et (AB)A (où les 2 B se lient ensemble) : ")

col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.latex(r'''(AB)A + B \xrightleftharpoons[k_{-2}]{k_2} AB(A+B)''')
    st.image(IMG_DIR / "Reaction_2.drawio.png", caption="Figure 6 : Réaction 2 d'un cycle autocatalytique minimal.", width=400)

st.write(f"c.) **Liaison** **covalente** entre A et B : ")

col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.latex(r'''AB(A+B) \xrightleftharpoons[k_{-3}]{k_3} (AB)(AB)''')
    st.image(IMG_DIR / "Reaction_3.drawio.png", caption="Figure 7 : Réaction 3 d'un cycle autocatalytique minimal.", width=400)

st.write(f"d.) **Rupture** des liaisons hydrogènes : ")

col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.latex(r'''(AB)(AB) \xrightleftharpoons[k_{-4}]{k_4} 2 AB''')
    st.image(IMG_DIR / "Reaction_4.drawio.png", caption="Figure 8 : Réaction 4 d'un cycle autocatalytique minimal.", width=400)


st.markdown(""" 
    Cette représentation permet également de mieux comprendre le **rôle** des **liaisons covalentes** et des **liaisons faibles**  
    (comme les liaisons hydrogènes), comme on connaît bien leur rôle important chez les **acides nucléiques**. 
    
    Pour en revenir à la formation du **mutant**, supposons dans le milieu une entité $A'$ : si $AB$ réagit avec un $A'$ au lieu d'un $A$, puis 
    réagit avec un $B$, *in fine* nous aurions bien la formation de $AB$ et $A'B$ qui correspond bien au **mutant**. 
             
""")

st.markdown("""## Thermodynamique et cinétique""")


st.markdown("""
            Pour suivre la **dynamique** du système, et donc l'**autoamplification** de l'espèce autocatalytique dans le milieu au cours du temps,
            nous avons besoin des **constantes de vitesse** qui dépendent des **grandeurs thermodynamiques et cinétiques** et des **concentrations** des entités de la réaction : \n\n

            **a. ) Grandeur thermodynamique** : 

            * Pour commencer, l'**énergie libre de Gibbs G** définie pour chaque entité  correspond à **l’énergie 
            disponible** pour effectuer un **travail utile** à température et pression constantes. On peut définir le changement de cette énergie 
            pour une réaction donnée par la relation suivante où $G_{\\text{initial}}$ est l'énergie libre des réactifs et $G_{\\text{final}}$ 
            est l'énergie libre des produits : 
            """)

st.latex(r'''\Delta G = G_{\text{final}} - G_{\text{initial}}''')

st.markdown("""
            Pour simplifier la partie **Simulations** et parce que l'impact du $\Delta G$ sur la dynamique n'est pas évident à définir,
            nous déciderons de fixer des valeurs pour ce paramètre et donc de ne pas pouvoir jouer sur celui-ci lors des simulations. 

""")

st.markdown(""" 

            **b.) Cinétique** : 

            La grandeur cinétique qui va particulièrement nous intéresser ici, notamment dans la partie simulation, est l'**énergie d'activation** $E_{a}$.
            Celle-ci correspond au niveau d'énergie atteint par la **barrière d'activation**. **Plus ce niveau d'énergie est important, 
            plus la réaction se fait lentement**. 

            Pour la partie **Simulations**, nous noterons $Ea_{LC}$, l'énergie d'activation associée à la **réaction c.)** formant la **liaison covalente** entre $A$ et $B$.

""")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(IMG_DIR / "Diagramme_reaction.png", caption="Figure 9 : Diagramme de réaction. En vert, $E_{a}$ représente la **barrière d'activation** dans le sens direct et $\Delta G$ la différence d'**énergie libre** entre réactifs et produits. " \
"", width=400)
    
st.markdown("""
            Comme évoqué précédemment, ces grandeurs interviennent dans l'expression des constantes de vitesse donnée par la loi empirique **d'Arrhenius**. \n\n

            Ainsi, pour la réaction $A + B \\rightarrow AB$, selon que $\Delta G$ soit négatif ou positif, nous pourrons définir les constantes de vitesse $k_+$ et $k_-$ respectivement dans les sens direct et indirect de la réaction. 
            Pour simplifier les notations, nous allons par la suite nous extraire de la constante préexponentielle $A$, ainsi que de la constante des gaz parfaits $R$ et de la température $T$ en Kelvin, initiallement présentes dans la loi d'Arrhenius. 

            * Si $\Delta G < 0$ :

""")


st.markdown("""Dans le sens **direct**, puisque la réaction est spontanée, nous modélisons le fait qu'il n'y a que la barrière d'énergie $E_{a}$ à franchir. 

""")

st.latex(r'''k_+ = \exp\left(-{E_{\text{a}}}\right)''')

st.markdown(""" Dans le **sens inverse**, nous mettons des **valeurs absolues** pour bien modéliser le fait que si $\Delta G < 0$, le **sens inverse**
            est **plus difficile** à franchir que le sens direct. 

""")

st.latex(r'''k_- = \exp\left(-{E_{\text{a}} + \left|\Delta G\right|}\right)''')

st.markdown(""" 
            * Inversement pour $\Delta G > 0$. 
""")


st.markdown("""
            Pour finir, les constantes de vitesse apparaîssent dans l'expression des vitesses des réactions (loi d'action de masse). 
            
            Ainsi pour la réaction $A + B \\rightarrow AB$ :

            * $v_{+} = [A][B]k_{+}$ dans le sens direct et $v_{-} = [AB]k_{-}$ dans le sens indirect. 

            * $v_{R}$ est la vitesse de la réaction $R$ avec $v_{R} = v_{+} - v_{-}$

            Et nous pouvons ainsi exprimer sous forme d'équation différentielle, l'évolution de la concentration des entités dans le cycle autocatalytique : 
            
            """)

st.latex(r'''\frac{d[A]}{dt} = \sum_{R \in \text{reactions}} v_R \cdot \mathrm{coef}(A, R)''')

st.markdown(""" 
            
            * $coef(A,R)$ représente le coefficient stoechiométrique de l'entité $A$ dans la réaction $R$, il est positif si elle est produit
            et négatif sinon.

            Ce sont ces équations différentielles que nous introduirons dans notre modèle et qui feront l'objet de la partie suivante **Simulations**. 

""")

def sidebar_button(label, anchor, bg="#D5F5E3", color="#8EB1AA"):
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

sidebar_button("Introduction", "introduction")
sidebar_button("Équations de réactions", "equations-de-reactions")
sidebar_button("Thermodynamique et cinétique", "thermodynamique-et-cinetique")

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
