

# import Libraries
import pandas as pd
import dash  # !pip install dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, State, Output
import plotly.graph_objects as go
import plotly.express as px

import webbrowser

from dash.exceptions import PreventUpdate


app = dash.Dash()  # Creating your object


def load_data():
    dataset_name = 'global_terror.csv'
    # Global Variables

    global df

    df = pd.read_csv(dataset_name)

    month = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    global month_list
    month_list = [{"label": key, "value": values} for key, values in month.items()]
    # print(month_list)

    global date_list
    date_list = [x for x in range(1, 32)]
    # print(date_list)

    global region_list
    region_list = [{"label": str(i).strip(), "value": str(i).strip()} for i in
                   sorted(df['region_txt'].unique().tolist())]
    # print(region_list)

    # print(df.sample(5))
    temp_list = sorted(df['country_txt'].unique().tolist())

    global country_list
    country_list = [{"label": str(i), "value": str(i)} for i in temp_list]
    # print(country_list)

    global state_list
    state_list = [{"label": str(i), "value": str(i)} for i in df['provstate'].unique().tolist()]
    # print(state_list)

    global city_list
    city_list = [{"label": str(i), "value": str(i)} for i in df['city'].unique().tolist()]
    # print(city_list)

    global attack_type_list
    attack_type_list = [{"label": str(i), "value": str(i)} for i in df['attacktype1_txt'].unique().tolist()]
    # print(attack_type_list)

    global year_list
    year_list = sorted(df['iyear'].unique().tolist())
    # print(year_list)

    global year_dict
    year_dict = {str(year): str(year) for year in year_list}
    # print(year_dict)
    global chart_dropdown_values
    chart_dropdown_values = {
        'Country Attacked': 'country_txt',
        'Region': 'region_txt',
        'Target Nationality': 'natlty1_txt',
        'Target Type': 'targtype1_txt',
        'Terrorist Organisation': 'gname',
        'Type of Attack':'attacktype1_txt',
        'Weapon Type':'weaptype1_txt'
    }
    chart_dropdown_values = [{"label": key, "value": value} for key, value in chart_dropdown_values.items()]


def open_browser():
    # To open web browser with the specified URL
    webbrowser.open_new('http://127.0.0.1:8050/')


def create_app_ui():
    # Here comes Layout of the page
    # Main Div
    main_layout = html.Div(id="MainDiv",

        # Adding html to div

        children = [
            html.Div(id='heading', children = [ html.H1(id='main_title', children='Terrorism Analysis with Insights')
                    ]),


            html.Div(id='options', children = [
                    html.Br(),
                    dcc.Tabs(id="Tabs", value="tab-1", children=[
                        dcc.Tab(label="Map Tool", id="Map_tool", value="Map", children=[
                            dcc.Tabs(id="subtabs", value="tab-1", children=[
                                dcc.Tab(label="World Map Tool", id="World",  value="tab-1",
                            selected_className='custom-tab--selected', children=[


            dcc.Dropdown(id="month", options=month_list, placeholder="Select Month", multi=True),

            dcc.Dropdown(id="date", placeholder="Select Date", multi=True),

            dcc.Dropdown(id="region-dropdown", options=region_list, placeholder="Select Region", multi=True),

            dcc.Dropdown(id='country-dropdown', options=country_list, placeholder="Select Country", multi=True),

            dcc.Dropdown(id="state-dropdown", options=state_list, placeholder="Select Sate or Province", multi=True),

            dcc.Dropdown(id="city-dropdown", options=city_list, placeholder="Select City", multi=True),

            dcc.Dropdown(id="attacktype-dropdown", options=attack_type_list, placeholder="Select Attack Type",
                         multi=True),


                        ]),
                                dcc.Tab(label="India Map tool", id="India", value="tab-2", children=[html.Div(),

                        dcc.Dropdown(
                            id="month1",
                            options=month_list,
                            placeholder="Select Month",
                            multi=True),

                        dcc.Dropdown(
                            id="date1",
                            placeholder="Select Date",
                            multi=True),

                        dcc.Dropdown(
                            id="region-dropdown1",
                            options=region_list,
                            placeholder="Select Region",
                            multi=True),

                        dcc.Dropdown(
                            id='country-dropdown1',
                            options=country_list,
                            placeholder="Select Country",
                            multi=True),

                        dcc.Dropdown(
                            id="state-dropdown1",
                            options=state_list,
                            placeholder="Select Sate or Province",
                            multi=True),

                        dcc.Dropdown(
                            id="city-dropdown1",
                            options=city_list,
                            placeholder="Select City",
                            multi=True),

                        dcc.Dropdown(
                            id="attacktype-dropdown1",
                            options=attack_type_list,
                            placeholder="Select Attack Type",
                            multi=True),

                        ]),
                            ]
                                     )
                        ]),

                        dcc.Tab(label="Chart Tool", id="chart_tool", value="Chart", selected_className='custom-tab--selected', children=[
                            dcc.Tabs(id="subtabs2", value="WorldChart", children=[
                                dcc.Tab(label="World Chart tool", id="WorldC", value="WorldChart", children=[html.Br(),
                            dcc.Dropdown(id="chart_drop1",options=chart_dropdown_values, placeholder="Select option",
                                         value="region_txt"),
                            html.Hr(),
                            dcc.Input(id="search", placeholder="Search Filter"),
                            ]),


                                dcc.Tab(label="India Chart tool", id="IndiaC", value="IndiaChart", children=[
                            html.Br(),
                            dcc.Dropdown(id="chart_drop",options=chart_dropdown_values, placeholder="Select option",
                                         value="region_txt"),
                            html.Hr(),
                            dcc.Input(id="search1", placeholder="Search Filter"),
                   ]),

                        ]),


            html.Div(),

        ]),

                     ]),

                     ]),
            html.Hr(),
            html.H5(
                'Select Year',
                id='year_title'),
            dcc.RangeSlider(
                id='year-slider',
                min=min(
                    year_list),
                max=max(
                    year_list),
                value=[min(
                    year_list),
                    max(
                        year_list)],
                marks=year_dict,

            ),
            html.Div(
                dcc.Loading(
                    id='graph-object',
                    type="graph",
                    # children=html.Div(id="loading-output-1",)
                    children=[
                        " loading"]
                ),
            ),
                           ])



    return main_layout


# App call back for  date
@app.callback(
    dash.dependencies.Output('date', 'options'),
    [
        dash.dependencies.Input('month', 'value')
    ]
)
def update_app_date(month):
    option = []
    if month:
        option = [{'label': m, 'value': m} for m in date_list]
    return option


# App Callback for country
@app.callback(
    dash.dependencies.Output('country-dropdown', 'options'),
    [
        dash.dependencies.Input('region-dropdown', 'value')
    ]
)
def update_app_country(region_value):
    temp = []

    if region_value is None:
        raise PreventUpdate

    else:

        for region_value_x in region_value:
            temp = temp + [{'label': str(i), 'value': str(i)} for i in
                           df[df['region_txt'] == region_value_x]['country_txt'].unique().tolist()]

        return temp


# App Callback for state
@app.callback(
    dash.dependencies.Output("state-dropdown", "options"),
    [
        dash.dependencies.Input("country-dropdown", 'value')
    ]
)
def update_app_state(country_value):
    temp = []

    if country_value is None:
        raise PreventUpdate

    else:
        for country_value_x in country_value:
            temp = temp + [{'label': str(i), 'value': str(i)} for i in
                           df[df['country_txt'] == country_value_x]['provstate'].unique().tolist()]

        return temp


# App callback city
@app.callback(
    dash.dependencies.Output('city-dropdown', 'options'),
    [
        dash.dependencies.Input('state-dropdown', 'value')
    ]
)
def upate_app_city(state_value):
    temp = []

    if state_value is None:
        raise PreventUpdate
    else:
        for state_value_x in state_value:
            temp = temp + [{'label': str(i), 'value': str(i)} for i in
                           df[df['provstate'] == state_value_x]['city'].unique().tolist()]

        return temp

@app.callback(
        dash.dependencies.Output("date1", "options"),
        [dash.dependencies.Input("month1", "value")])
def update_date(month1):
    option = []
    if month1:
        option = [{'label': m, 'value': m} for m in date_list]
    return option
    # Callback of page for map

@app.callback(
    Output('country-dropdown1', 'options'),
    [Input('region-dropdown1', 'value')])
def set_country_options(region_value):
    temp = []

    if region_value is None:
        raise PreventUpdate

    else:

        for region_value_x in region_value:
            temp = temp + [{'label': str(i), 'value': str(i)} for i in
                           df[df['region_txt'] == region_value_x]['country_txt'].unique().tolist()]

        return temp
@app.callback(
    Output('city-dropdown1', 'options'),
    [Input('state-dropdown1', 'value')])
def set_city_options(state1):
    # Making the city Dropdown data
    temp = []

    if state1 is None:
        raise PreventUpdate
    else:
        for state_value_x in state1:
            temp = temp + [{'label': str(i), 'value': str(i)} for i in
                           df[df['provstate'] == state_value_x]['city'].unique().tolist()]

        return temp
@app.callback(
    Output('state-dropdown1', 'options'),
    [Input('country-dropdown1', 'value')])
def set_state_options(country_value):
    # Making the state Dropdown data
    temp = []

    if country_value is None:
        raise PreventUpdate

    else:
        for country_value_x in country_value:
            temp = temp + [{'label': str(i), 'value': str(i)} for i in
                           df[df['country_txt'] == country_value_x]['provstate'].unique().tolist()]

        return temp


@app.callback(
    dash.dependencies.Output('graph-object', 'children'),
    [
        dash.dependencies.Input('Tabs', 'value'),
        dash.dependencies.Input('month', 'value'),
        dash.dependencies.Input('date', 'value'),
        dash.dependencies.Input('region-dropdown', 'value'),
        dash.dependencies.Input('country-dropdown', 'value'),
        dash.dependencies.Input('state-dropdown', 'value'),
        dash.dependencies.Input('city-dropdown', 'value'),
        dash.dependencies.Input('attacktype-dropdown', 'value'),
        dash.dependencies.Input('year-slider', 'value'),
        dash.dependencies.Input('chart_drop', 'value'),
        dash.dependencies.Input('chart_drop1', 'value'),

        dash.dependencies.Input('search', 'value'),
        dash.dependencies.Input('search1', 'value'),

        dash.dependencies.Input('subtabs2', 'value'),
        dash.dependencies.Input('subtabs', 'value'),
        dash.dependencies.Input('month1', 'value'),
        dash.dependencies.Input('date1', 'value'),
        dash.dependencies.Input('region-dropdown1', 'value'),
        dash.dependencies.Input('country-dropdown1', 'value'),
        dash.dependencies.Input('state-dropdown1', 'value'),
        dash.dependencies.Input('city-dropdown1', 'value'),
        dash.dependencies.Input('attacktype-dropdown1', 'value'),

    ]
)
def update_app_ui(Tabs, month_value, date_value, region_value, country_value, state_value, city_value, attack_value,
                  year_value, chart_dp_value, chart_dp_value1, search, search1, subtabs2, subtabs, month1,date1, region1,country1,state1, city1, attack1 ):
    # figure = None

    global figure
    figure = go.Figure()
    year_range = range(year_value[0], year_value[1] + 1)
    df_new = df[df["iyear"].isin(year_range)]

    # month_filter
    if month_value is None or month_value == []:
        pass
    else:
        if date_value is None or date_value == []:
            new_df = df_new[df_new["imonth"].isin(month_value)]

        else:
            new_df = df_new[(df_new["imonth"].isin(month_value)) &
                            (df_new["iday"].isin(date_value))]

    if Tabs == "Map":
        if subtabs == 'tab-1':


            # Filter region country stare city
            if region_value is None:
                pass

            else:
                if country_value is None:
                    df_new = df_new[(df_new['region_txt'].isin(region_value))]

                else:
                    if state_value is None:
                        df_new = df_new[(df_new['region_txt'].isin(region_value)) & (df_new['country_txt'].isin(country_value))]
                    else:
                        if city_value is None:
                            df_new = df_new[(df_new['region_txt'].isin(region_value)) & (df_new['country_txt'].isin(country_value)) & (
                                df_new['provstate'].isin(state_value))]

                        else:

                            df_new = df_new[(df_new['region_txt'].isin(region_value)) & (df_new['country_txt'].isin(country_value)) & (
                                df_new['provstate'].isin(state_value)) & (df_new['city'].isin(city_value))]

            # Filtering Attack type
            if attack_value is None:
                pass
            else:
                df_new = df_new[df['attacktype1_txt'].isin(attack_value)]

            # Filter the Year value
            year_value = range(year_value[0], year_value[1] + 1)
            df_new = df_new[df_new['iyear'].isin(year_value)]

            # Show the map to a blank  map
            if df_new.shape[0]:
                pass
            else:
                df_new = pd.DataFrame(
                    columns=['iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'provstate', 'city', 'latitude',
                             'longitude', 'attacktype1_txt', 'nkill'])

                df_new.loc[0] = [0, 0, 0, None, None, None, None, None, None, None, None]

            wmap_figure = px.scatter_mapbox(
                df_new,
                lat="latitude",
                lon="longitude",
                hover_data=['region_txt', 'country_txt', 'provstate', 'city', 'attacktype1_txt', 'nkill', 'iyear'],
                zoom=1,
                color="attacktype1_txt",
                labels=attack_type_list,
            )

            wmap_figure.update_layout(mapbox_style="open-street-map",
                                 autosize=True,
                                 margin=dict(l=0, r=0, t=25, b=20))
            figure = wmap_figure

        elif subtabs == 'tab-2':
            df1 = df.loc[df["country_txt"] == 'India']
            df1_new = df1[df1["iyear"].isin(year_range)]

            figure = go.Figure()
            if region1 is None or region1 == []:
                pass
            else:
                if country1 is None or country1 == []:
                    df1_new = df1_new[df1_new["region_txt"].isin(region1)]
                else:
                    if state1 is None or state1 == []:
                        df1_new = df1_new[(df1_new["region_txt"].isin(region1)) &
                                          (df1_new["country_txt"].isin(country1))]
                    else:
                        if city1 is None or city1 == []:
                            df1_new = df1_new[(df1_new["region_txt"].isin(region1)) &
                                              (df1_new["country_txt"].isin(country1)) &
                                              (df1_new["provstate"].isin(state1))]
                        else:
                            df1_new = df1_new[(df1_new["region_txt"].isin(region1)) &
                                              (df1_new["country_txt"].isin(country1)) &
                                              (df1_new["provstate"].isin(state1)) &
                                              (df1_new["city"].isin(city1))]

                # Attack Type
                if attack1 is None or attack1 == []:
                    pass
                else:
                    df1_new = df1_new[df1_new["attacktype1_txt"].isin(attack1)]

                if df1_new.shape[0]:
                    pass
                else:
                    df1_new = pd.DataFrame(columns=['iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'provstate',
                                                    'city', 'latitude', 'longitude', 'attacktype1_txt', 'nkill'])

                    df1_new.loc[0] = [0, 0, 0, None, None, None, None, None, None, None, None]

                imapfigure = px.scatter_mapbox(df1_new,
                                           lat="latitude",
                                           lon="longitude",
                                           color="attacktype1_txt",
                                           hover_data=["region_txt", "country_txt", "provstate", "city",
                                                       "attacktype1_txt", "nkill", "iyear", "imonth", "iday"],
                                           zoom=1
                                           )
                imapfigure.update_layout(mapbox_style="open-street-map",
                                     autosize=True,
                                     margin=dict(l=0, r=0, t=25, b=20),
                                     )
                figure = imapfigure

    elif Tabs == 'Chart':
        figure = None

        year_range = range(year_value[0], year_value[1] + 1)
        chart_df = df[df['iyear'].isin(year_range)]

        if subtabs2 == 'WorldChart':
                pass

        elif subtabs2 == 'IndiaChart':
            figure = go.Figure()
            year_range = range(year_value[0], year_value[1] + 1)
            new_df = df[df["iyear"].isin(year_range)]

            chart_df = new_df[(new_df['region_txt'] == 'South Asia') & (new_df['country_txt'] == 'India')]
        if chart_dp_value1 is not None:
            if search1 is not None:
                chart_df = chart_df.groupby('iyear')[chart_dp_value1].value_counts().reset_index(name='count')
                chart_df = chart_df[chart_df[chart_dp_value1].str.contains(search1, case=False)]
            else:
                chart_df = chart_df.groupby('iyear')[chart_dp_value1].value_counts().reset_index(name='count')

        if chart_df.shape[0]:
            pass
        else:
            chart_df = pd.DataFrame(columns=['iyear', 'count', chart_dp_value1])
        # Chart Tool
        ichartFigure = px.area(
            chart_df,
            x='iyear',
            y='count',
            color=chart_dp_value1,
        )

        figure = ichartFigure
    return dcc.Graph(figure = figure)

@app.callback(
  [
  dash.dependencies.Output('region-dropdown1', 'value'),
  dash.dependencies.Output('region-dropdown1', 'disabled'),
  dash.dependencies.Output('country-dropdown1', 'value'),
  dash.dependencies.Output('country-dropdown1', 'disabled')
  ],
  [
  dash.dependencies.Input('India', 'value')
  ]
  )
def update_r(Tabs):
    region = None
    disabled_region = False
    country = None
    disabled_country = False
    if Tabs == 'WorldMap':
        pass
    elif Tabs =='tab-2':
        region = ['South Asia']
        disabled_region = True
        country = ['India']
        disabled_country = True
    return region, disabled_region, country, disabled_country

def main():
    print("Welcome to the Project Season 3 ")
    load_data()
    open_browser()

    global app

    app.layout = create_app_ui()  # blank Container Page
    # Change the title
    app.title = "Terrorism Analysis with Insights"

    # app.layout = create_app_ui()
    app.run_server()

    app = None
    df = None
    # figure = None

    print("Thanks for using my Project ")


if __name__ == '__main__':
    main()


