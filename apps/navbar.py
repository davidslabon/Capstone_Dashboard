import dash_bootstrap_components as dbc

def navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Vizualisaton", href="/apps/dashboard"), id="page-1-link"),
            dbc.NavItem(dbc.NavLink("Background", href="/apps/scoring"), id="page-2-link")
        ],
        brand="SCORE2",
        brand_href="/",
        color="rgb(207, 219, 206)",
        light=True,
        fluid=True,
        brand_style= {"font-weight": "bold", "font-size": "larger"}
    )
    return navbar

