import pandas as pd
import altair as alt
import plotly.express as px

def load_data(data_path):
    df = pd.read_csv(data_path, parse_dates=['Timestamp'])
    return df

def get_summary_statistics(df):
    return df.describe()

def plot_time_series(df, theme):
    chart = alt.Chart(df).mark_line().encode(
        x='Timestamp:T',
        y=alt.Y('GHI:Q', scale=alt.Scale(zero=False)),
        color=alt.Color('GHI:Q', scale=alt.Scale(scheme=theme))  # Apply the selected color theme
    ).properties(
        width=800,
        height=400
    )
    return chart

def plot_correlation_matrix(df, theme):
    correlation = df.corr()
    chart = alt.Chart(correlation.reset_index()).transform_fold(
        correlation.columns,
        as_=['column', 'correlation']
    ).mark_rect().encode(
        x='index:O',
        y='column:O',
        color=alt.Color('correlation:Q', scale=alt.Scale(scheme=theme))
    ).properties(
        width=800,
        height=400
    )
    return chart

def plot_wind_analysis(df, theme):
    chart = alt.Chart(df).mark_circle().encode(
        x='WS:Q',
        y='WD:Q',
        size='WSstdev:Q',
        color=alt.Color('WS:Q', scale=alt.Scale(scheme=theme))  # Apply the selected color theme
    ).properties(
        width=800,
        height=400
    )
    return chart

def plot_temperature_analysis(df, theme):
    chart = alt.Chart(df).mark_line().encode(
        x='Timestamp:T',
        y=alt.Y('Tamb:Q', scale=alt.Scale(zero=False)),
        color=alt.Color('Tamb:Q', scale=alt.Scale(scheme=theme))  # Apply the selected color theme
    ).properties(
        width=800,
        height=400
    )
    return chart

def plot_histograms(df, theme):
    # Handle theme validation
    valid_themes = px.colors.sequential.__dict__.keys()
    if theme not in valid_themes:
        theme = 'Viridis'  # Fallback to Viridis if theme is invalid

    fig = px.histogram(df, x='GHI', color_discrete_sequence=px.colors.sequential.__dict__[theme])
    return fig

def plot_bubble_chart(df, theme):
    # Handle theme validation
    valid_themes = px.colors.sequential.__dict__.keys()
    if theme not in valid_themes:
        theme = 'Viridis'  # Fallback to Viridis if theme is invalid

    fig = px.scatter(df, x='GHI', y='Tamb', size='WS', color='RH',
                     color_discrete_sequence=px.colors.sequential.__dict__[theme])
    return fig
