import dash
import pandas
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
        #html.H2('ANIORT NICOLAS'),
        html.P('Développeur python indépendant',className ='job'),
        html.Div(
            [
                dcc.Link('Résumé', href='#resume', className='menu-item'),
                dcc.Link('Formations', href='#education', className='menu-item'),
                dcc.Link('Compétences', href='#skills', className='menu-item'),
                dcc.Link('Projets', href='#projects', className='menu-item'),
                dcc.Link('Langues', href='#languages', className='menu-item'),
                dcc.Link('Un peu + sur moi', href='#about', className='menu-item')
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
                            'Formations'
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
                            'Compétences'
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
                html.Section(
                    [
                        html.H2([
                                html.I(className='fa fa-graduation-cap'),  # Ajoutez l'icône ici
                                'Projets'
                                ], id='projects'),
                        html.P('Vos projets ici.')
                    ],
                    className='content-section'
                ),
                html.Section(
                    [
                        html.H2([
                                html.I(className='fa fa-graduation-cap'),  # Ajoutez l'icône ici
                                'Langues'
                                ], id='languages'),
                        html.P('Vos langues ici.')
                    ],
                    className='content-section'
                ),
                html.Section(
                    [
                        html.H2([
                                html.I(className='fa fa-graduation-cap'),  # Ajoutez l'icône ici
                                'Un peu + sur moi'
                                ], id='about'),
                        html.P('Informations additionnelles sur vous.')
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
