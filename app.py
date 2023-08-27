import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# structure html de la page
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
        <link rel="stylesheet" href="./assets/styles.css">
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Styles
app.layout = html.Div(
                [
                    html.Div(
                        [
                            html.Img(src='assets\img\profil.jpg', className='profile-image'),
                            html.P('Développeur python indépendant',className ='job'),
                            html.Div(
                                [
                                    dcc.Link('Résumé', href='#resume', className='menu-item'),
                                    dcc.Link('Formations', href='#education', className='menu-item'),
                                    dcc.Link('Compétences', href='#skills', className='menu-item'),
                                    dcc.Link('Projets', href='#projects', className='menu-item'),
                                    dcc.Link('Langues', href='#languages', className='menu-item')
                                ],
                                className='menu'
                            ),
                        ],
                        className='sidebar'
                    ),

        html.Div(
            [
                html.Section(
                    [
                        html.H2( id='resume'),
                        html.H2(
                            [
                                html.Span('NICOLAS', className='fname'),
                                html.Span(' '),
                                html.Span('ANIORT', className='name'),
                            ] 
                            ,className='nameTitle'   
                        ),
                        html.P('Développeur python indépendant – Grâce à mon accompagnement, je facilite la conception et la création de votre site web '),
                        html.Ul(
                            [    
                            html.Li(
                            [
                                html.I(className='fa fa-address-card icon-space'),  # Utilisez la classe d'icône correcte
                                '45 ans'
                            ],
                            className='list-item'
                            ),    
                            html.Li(
                                [
                                html.I(className='fa fa-map-location-dot icon-space'),  # Utilisez la classe d'icône correcte
                                '81100 CASTRES'
                            ],
                            className='list-item'
                            ),
                            html.Li(
                                [
                                html.I(className='fa fa-envelope icon-space'),  # Utilisez la classe d'icône correcte
                                'nicolas.aniort@gmail.com'
                            ],
                            className='list-item'
                            ) 
                            ],
                         className='listeInformation'
                         )                       
                    ],
                    className='content-section'
                ),
                html.Section(
                    [
                        html.H2([
                            html.I(className='fa fa-graduation-cap'),  # Ajoutez l'icône ici
                            ' Formations'
                        ], id='education'),
                        html.P('DEVELOPPEUR D\'APPLICATION PYTHON - OPENCLASSROOMS - 2023'),
                        html.P('ANALYSTE-DEVELOPPEUR J2EE - IPST- CNAM-TOULOUSE - 2008'),
                        html.P('BTS TV option PC - EPLFPA MONTAUBAN - 2003'),
                        html.P('BACCALAUREAT SCIENTIFIQUE, Option BIOLOGIE - ECOLOGIE - ENVIRONNEMENT - 1999')
                    ],
                    className='content-section'
                ),
                html.Section(
                    [
                        html.H2([
                            html.I(className='fa fa-list-check'),  # Ajoutez l'icône ici
                            ' Compétences'
                        ], id='skills'),
                             html.Table(
                                [
                                    html.Thead(
                                        html.Tr(
                                            [
                                                html.Th(colSpan=2, children=[
                                                    html.I(className='fas fa-code'),
                                                    ' Langages'
                                                ]),
                                                html.Th(colSpan=2, children=[
                                                    html.I(className='fas fa-laptop-code'),
                                                    ' Frameworks'
                                                ]),
                                                html.Th(colSpan=2, children=[
                                                    html.I(className='fas fa-tools'),
                                                    ' Outils de développement'
                                                ]),
                                                html.Th(colSpan=2, children=[
                                                    html.I(className='fas fa-cog'),
                                                    ' Autres'
                                                ])
                                            ],
                                            className='header-row'
                                        )
                                    ),
                                    html.Tbody(
                                        [
                                            html.Tr(
                                                [
                                                    html.Td([
                                                        html.I(className='fab fa-python'),
                                                        ' Python'
                                                    ]),
                                                    html.Td('Développement Python'),
                                                    html.Td([
                                                        html.I(className='fab fa-django'),
                                                        ' Django'
                                                    ]),
                                                    html.Td('Framework web Django'),
                                                    html.Td([
                                                        html.I(className='fab fa-git'),
                                                        ' Git'
                                                    ]),
                                                    html.Td('Gestion de versions Git'),
                                                    html.Td([
                                                        html.I(className='fas fa-server'),
                                                        ' Serveurs'
                                                    ]),
                                                    html.Td('Déploiement de serveurs')
                                                ]
                                            ),
                                            # Ajoutez d'autres lignes de compétences ici
                                        ]
                                    )
                                ]
                            )
                    
                    ],
                    className='content-section'
                ),
                #SECTION PROJET------------------------
                html.Section(
                    [
                        html.H2([
                                html.I(className='fa fa-diagram-project'),  # Ajoutez l'icône ici
                                ' Projets'
                                ], id='projects'),
                                html.Div(
                                [
                                    # Premier bloc projet---------------------------------
                                    html.Div(
                                        [
                                            html.Img(src='assets\img\/vignetteP2.png', className='project-image'),
                                            html.H3('Application de Scrapping'),
                                            html.P('création d\'une application locale permettant le scrapping depuis le site Book to Scrape')
                                        ],
                                        className='project-block'
                                    ),
                                    
                                    # Deuxième bloc projet- -------------------------------
                                    html.Div(
                                        [
                                            html.Img(src='assets\img\justStreamit.png', className='project-image'),
                                            html.H3('JustStreamIt'),
                                            html.P('création d\'une interface utilisateur pour une application web Python')
                                        ],
                                        className='project-block'
                                    ),
                                    
                                    # Troisieme bloc projet---------------------------------
                                    html.Div(
                                        [
                                            html.Img(src='assets\img\/vignetteP7.png', className='project-image'),
                                            html.H3('ALGOINVEST&TRADE'),
                                            html.P('Réalisation d\'un algorithme optimisé pour le trading')
                                        ],
                                        className='project-block'
                                    ),
                                    
                                    # Quatrieme bloc projet---------------------------------
                                    html.Div(
                                        [
                                            html.Img(src='assets\img\gestion_echec.png', className='project-image'),
                                            html.H3('Outil de gestion de tournoi d\'échec'),
                                            html.P('Développement d\'un programme logiciel en Python')
                                        ],
                                        className='project-block'
                                    ),
                                    
                                    # Cinquieme bloc projet---------------------------------
                                    html.Div(
                                        [
                                            html.Img(src='assets\img\morpion.png', className='project-image'),
                                            html.H3('Jeu du morpion'),
                                            html.P('Developpement d\'un jeu du morpion en Python')
                                        ],
                                        className='project-block'
                                    ),
                                    
                                    # Sixiéme bloc projet---------------------------------
                                    html.Div(
                                        [
                                            html.Img(src='assets\img\dash_cv_template.png', className='project-image'),
                                            html.H3('Template CV -Framework Dash'),
                                            html.P('Réalisation d\'un template de CV avec le Framework Dash de Python.')
                                        ],
                                        className='project-block'
                                    ),# Ajoutez d'autres blocs projet ici
                                ],
                        className='project-container'
                    )
                ],
                    className='content-section'
                ),
                html.Section(
                    [
                        html.H2([
                                html.I(className='fa fa-graduation-cap'),  # Ajoutez l'icône ici
                                'Langues'
                                ], id='languages'),
                        html.P('Francais - Langue natale'),
                        html.P('Anglais - Niveau B2')
                    ],
                    className='content-section'
                ),
                
            ],
            className='content'
        )
    ],
    className='container'
)

if __name__ == "__main__":
    app.run_server(debug=True)
