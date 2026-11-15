import streamlit as st
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, classification_report

def plot_series_interactive(df, columns, window=None, center=True, labels=None, title=None, ylabel=""):
    """Interactive line plot of monthly columns.

    window=None  -> raw monthly values
    window=12    -> rolling mean over 12 months
    """
    if isinstance(columns, str):
        columns = [columns]
    labels = labels or {}

    d = df.sort_values("month").copy()
    names = []
    for col in columns:
        base = labels.get(col, col)
        if window:
            name = f"{base} ({window}-month mean)"
            d[name] = d[col].rolling(window, center=center).mean()
        else:
            name = base
            d[name] = d[col]
        names.append(name)

    long = d.melt(id_vars="month", value_vars=names,
                  var_name="series", value_name="value")

    fig = px.line(long, x="month", y="value", color="series",
                  title=title, labels={"value": ylabel, "month": ""})
    fig.update_traces(hovertemplate="%{y:.2f}<extra>%{fullData.name}</extra>")
    fig.update_layout(hovermode="x unified", height=420, legend_title_text="")
    fig.update_xaxes(hoverformat="%b %Y", rangeslider_visible=True)
    fig.show()