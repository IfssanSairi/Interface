import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

st.header("Evolution de la concentration des entités chimiques dans un cycle autocatalytique ", divider="gray")

class Reaction(object):
    

    def __init__(self, reactifs, produits, E_a, deltaG):
        self.reactifs=reactifs
        self.produits=produits
        self.E_a=E_a
        self.deltaG=deltaG
    
    def constante(self, isForward):
      if (self.deltaG <= 0 and isForward) or (self.deltaG >= 0 and not isForward) : 
         k=np.exp(-self.E_a/(8.314*290))
      else :  
         k=np.exp((-self.E_a - abs(self.deltaG))/(8.314*290))  
      return(k)
    
    def vitesse(self, y, idx): 
      vp=self.constante(isForward=True)
      for e,n in self.reactifs.items():
        vp*=y[idx[e]]**n

      vm=self.constante(isForward=False)
      for e,n in self.produits.items():
         vm*=y[idx[e]]**n
      
      return(vp-vm)
        
#Ea_LH=0
#Ea_LC=80e3 
#DeltaG_LH = 5e3
#DeltaG_LC = 50e3 

def M(reactions, entites, idx):
    M = np.zeros((len(reactions), len(entites)))
    for i, r in enumerate(reactions):
        for e, n in r.reactifs.items(): 
            M[i, idx[e]] = M[i, idx[e]] - n  
        for e, n in r.produits.items():
            M[i, idx[e]] = M[i, idx[e]] + n  
    return M


def simulation_AB_seul(E_a, entree, sortie, Tmax):
    entites = ["A", "AB", "B", "ABA", "ABAB_h", "ABAB_c"]
    idx = {e: i for i, e in enumerate(entites)}

    y0 = np.zeros(len(entites))
    y0[idx["A"]] = 1
    y0[idx["B"]] = 1
    y0[idx["AB"]] = 0.001


    reactions = [Reaction({"A":1, "AB":1}, {"ABA":1}, E_a=0, deltaG=0), 
             Reaction({"B":1, "ABA":1}, {"ABAB_h":1}, E_a=0, deltaG=0),
             Reaction({"ABAB_h":1}, {"ABAB_c":1}, E_a=E_a, deltaG=-50e3), 
             Reaction({"ABAB_c":1}, {"AB":2}, E_a=0, deltaG=2*0)] 

    Matrice = M(reactions, entites, idx) 

    def cycle(y,t):
        V = np.array([r.vitesse(y,idx) for r in reactions])
        W=np.dot(V, Matrice)

        W[idx["A"]] += entree - sortie * y[idx["A"]]
        W[idx["B"]] += entree - sortie * y[idx["B"]]
      
        return(W)

    dt=0.1
    t = np.arange(0,Tmax,dt)
    sol = odeint(cycle,y0,t)
    return (t, sol)

def simulation_mutant(E_a_residant,E_a_mutant, concentration_mut, Tmax, entree, sortie):
    entites=["A", "AB", "B",  "A'", "A'B", "ABA", "ABAB_h", "ABAB_c","A'BA'", "A'BA'B_h", "A'BA'B_c"]
    idx = {e: i for i, e in enumerate(entites)}

    y0 = np.zeros(len(entites))
    y0[idx["A"]] = 1
    y0[idx["B"]] = 1
    y0[idx["AB"]] = 0.001
    y0[idx["A'"]] = concentration_mut


    reactions= [
             Reaction({"A":1, "AB":1}, {"ABA":1}, E_a=0, deltaG=0), 
             Reaction({"B":1, "ABA":1}, {"ABAB_h":1}, E_a=0, deltaG=0), 
             Reaction({"ABAB_h":1}, {"ABAB_c":1}, E_a=E_a_residant, deltaG=-50e3), 
             Reaction({"ABAB_c":1}, {"AB":2}, E_a=0, deltaG=2*0), 
             Reaction({"A'B":1, "A'":1}, {"A'BA'":1}, E_a=0, deltaG=0),
             Reaction({"A'BA'":1, "B":1}, {"A'BA'B_h":1}, E_a=0, deltaG=0),
             Reaction({"A'BA'B_h":1}, {"A'BA'B_c":1}, E_a=E_a_mutant, deltaG=-50e3),
             Reaction({"A'BA'B_c":1}, {"A'B":2}, E_a=0, deltaG=2*0)] 

    Matrice = M(reactions, entites, idx) 

    def cycle(y,t):
        V = np.array([r.vitesse(y,idx) for r in reactions])
        W=np.dot(V,Matrice)

        W[idx["A"]] += entree - sortie * y[idx["A"]]
        W[idx["B"]] += entree - sortie * y[idx["B"]]
        W[idx["A'"]] += entree - sortie * y[idx["A'"]]

        return (W)
    
    dt=0.1
    t=np.arange(0,Tmax,dt) 

    y = y0.copy()
    sol = np.zeros((len(t), len(entites)))
    sol[0] = y

    tableau = []
    mutation = False

    t_mut = 100
    k_mut = int(t_mut/dt)

    for k in range(1, len(t)):
       y = odeint(cycle, y, [t[k-1], t[k]])[-1] 
      
       if not mutation and k >= k_mut :

          mutation = True       
          tableau.append(t[k])
          concentration = 0.001   
          y[idx["AB"]]  = max(y[idx["AB"]] - concentration, 0)
          y[idx["A'B"]] += concentration 
          
          #p = 10*y[idx["AB"]] *y[idx["A'"]]*dt #jouer sur valeurs du facteur
          #p=min(p,1)
          
          #if np.random.rand() < p:
             

       sol[k] = y

    return (t, sol, tableau)

#AFFICHAGE
st.markdown("### Scénario n°1 : Cycle AB seul autocatalyseur", unsafe_allow_html=True)

st.markdown(""" 
            Dans ce scénario, nous nous attendons à observer **l'auto-amplification** de l'entité **autocatalytique** $AB$.  

            Pour simuler au mieux les conditions nécessaires au **vivant**, nous nous plaçons dans un **système ouvert**, ainsi nous pourrons choisir des 
            valeurs de **taux d'entrée** et de **sortie** non nulles. 
            
            Nous pouvons nous rendre compte que dans un système **fermé**, la grandeur cinétique $E_{a}$ est un facteur multiplicateur
            qui joue un rôle sur la vitesse. Dans un système **ouvert**, le rôle de $E_{a}$ est plus complexe en réalité, cependant lorsque 
            cette **barrière d'activation augmente**, nous pouvons toujours observer un **ralentissement** de la réaction. 
            
            """)


values = np.linspace(0,10000) 
temps=np.linspace(200,1000)
valeurs = np.linspace(0,1)
taux = np.linspace(0,0.005)

col_graph, col_ctrl = st.columns([3, 1]) 

with col_ctrl:
    st.markdown("#### Paramètre cinétique")
    E_a = st.select_slider('$Ea_{LC} (J/mol)$', options=values, value=0, key="E_a_global")
    st.markdown("#### Autres paramètres")
    Tmax = st.select_slider(
        'Temps maximal pour la simulation',
        options=temps,
        value=200,
        key="Tmax"
    )
    entree = st.select_slider(
        'Taux entrée élémentaire',
        options=taux,
        value=0,
        key="entree"
    )
    sortie = st.select_slider(
        'Taux sortie élémentaire',
        options=taux,
        value=0,
        key="sortie"
    )
   
t, sol = simulation_AB_seul(E_a,entree, sortie, Tmax)

fig, ax = plt.subplots(figsize=(4,3))

color = ["#457B9D", "#A8DADC", "#8EB1AA"]
for i, lettre in enumerate(["A", "AB", "B"]):
   ax.plot(t, sol[:, i], label=lettre, color=color[i])

ax.set_xlabel('t')
ax.set_ylabel('Concentration des entités')
ax.legend()
with col_graph:
   st.pyplot(fig, use_container_width=False)

   
#AFFICHAGE DU 2EME PLOT 
st.markdown("### Scénario n°2 : Cycle avec mutant", unsafe_allow_html=True)

st.markdown("""
            Pour appréhender le concept d'**évolution** sur ces **objets prébiotiques**, nous décidons dans cette partie de simuler l'apparition
            d'un **mutant** dans le système, à savoir ici $A'B$ qui ne peut apparaître que si $AB$, le **résidant**, est **abondant**.

            Cette condition d'abondance sur l'entité $AB$ n'est pas vraiment respectée ici dans la simulation car nous avons décidé 
            de représenter cet évènement mutationnel de manière **déterministe** en le forçant à apparaître à un instant donné dès que la **concentration de $A'$** (une **entité primaire** dans le système au même titre que $A$ et $B$) est **non nulle**. 

            Nous pouvons afficher sur le graphique le 1er et seul moment où le **mutant $A'B$** apparaît, c'est
            ce à quoi correspond la **ligne verticale grise en pointillée**. Ce moment marque l'**introduction du mutant**. 
            Dans cette simulation, une fois qu'il apparaît **il ne peut plus réappaître**, il s'agit donc d'un **évènement mutationnel fortuit et rare**.

            De la même manière, la réaction $A' + B \\rightarrow A'B$ est très **défavorable** cinétiquement. En revanche, si l'entité $A'B$ est amenée à réagir avec les entités $A'$ et $B$, nous pourrions imaginer une série de réactions 
            qui formeraient aussi un **cycle autocatalytique pour le mutant**.  
            
            """)


col_graph, col_ctrl = st.columns([3, 1]) 

col1, col2 = st.columns(2)

with col_ctrl:
    st.markdown("#### Paramètres cinétiques")
    E_a_residant= st.select_slider('$Ea_{LC}\,\mathrm{résidant}\,(J/mol)$', options=values, value=0, key="E_a_residant") 
    E_a_mutant= st.select_slider('$Ea_{LC}\,\mathrm{mutant}\,(J/mol)$', options=values, value=0, key="E_a_mutant")
    E_a = st.select_slider('$Ea_{LC} (J/mol)$', options=values, value=0, key="E_a")
    st.markdown("#### Autres paramètres")
    entree=st.select_slider('Taux entrée entités élémentaires', options=taux, value=0, key="entree_col2")
    sortie=st.select_slider('Taux sortie entités élémentaires', options=taux, value=0, key="sortie_col3")
    
with col1 : 
   Tmax=st.select_slider('Temps maximal pour la simulation',options=temps, value=200, key="Tmax_col3")

with col2 : 
   concentration_mut=st.select_slider(r''' Concentration de A' ''', options=valeurs, value=0)


t_2, sol_2, tableau = simulation_mutant(E_a_residant,E_a_mutant, concentration_mut,Tmax, entree, sortie)

fig_2, ax_2 = plt.subplots(figsize=(4,3))

color = ["#457B9D", "#A8DADC", "#8EB1AA","#F5D5F2", "#DEB865" ]
for i, lettre in enumerate(["A", "AB", "B", "A'", "A'B"]):
   ax_2.plot(t_2, sol_2[:, i], label=lettre, color=color[i])

if len(tableau)!= 0 and concentration_mut !=0 : 
   ax_2.plot([tableau[0],tableau[0]], [0, 1], color="grey", lw=1, linestyle="--")

ax_2.set_xlabel('t')
ax_2.set_ylabel('Concentration des entités')
ax_2.legend()
with col_graph:
   st.pyplot(fig_2, use_container_width=False)

st.markdown("""

            Grâce à cette simulation, nous pouvons toucher du doigt l'idée d'une **intéraction** entre ces **2 cycles autocatalytiques** : 
            nous nous apercevons que cette dynamique repose fortement sur la grandeur $Ea_{LC}$ qui lorsqu'elle est plus grande 
            pour le cycle résidant semble favoriser cinétiquement l'apparition du mutant $A'B$.

            **Remarque** : une manière plus réaliste de le faire aurait été de modéliser une **probabilité** d'apparition de **mutant**, proportionnelle à la concentration de $A'$ choisie et de $AB$. 

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


