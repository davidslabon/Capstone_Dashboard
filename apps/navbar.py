import dash_bootstrap_components as dbc

def navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(
                "Dashboard", 
                href="/apps/dashboard", 
                style={"font-weight": "bold", "font-size": "larger", "text-decoration": "none"}), 
                id="page-1-link"
                ),
            dbc.NavItem(dbc.NavLink(
                "Head2Head", 
                href="/apps/headtohead", 
                style={"font-weight": "bold", "font-size": "larger", "text-decoration": "none"}), 
                id="page-3-link"),               
            dbc.NavItem(dbc.NavLink(
                "Project", 
                href="/apps/project", 
                style={"font-weight": "bold", "font-size": "larger", "text-decoration": "none"}), 
                id="page-2-link"),
            dbc.NavItem(dbc.NavLink(
                "GitHub", 
                href="https://github.com/davidslabon/Capstone_UnlockingClimateSolutions", 
                style={"font-weight": "bold", "font-size": "larger", "text-decoration": "none"}), 
                id="page-3-link"),
            dbc.NavItem(dbc.NavLink(
                "Kaggle", 
                href="https://www.kaggle.com/c/cdp-unlocking-climate-solutions/", 
                style={"font-weight": "bold", "font-size": "larger", "text-decoration": "none"}), 
                id="page-4-link")
        ],
        brand="Home",
        brand_href="/",
        color="bg-primary",
        light=False,
        className = "bg-primary",
        dark=True,
        fluid=True,
        brand_style= {"font-weight": "bold", "font-size": "larger", "text-decoration": "none"},
        )
    return navbar

