import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
from datetime import timedelta
import os
from typing import Optional
from statsmodels.tsa.statespace.sarimax import SARIMAXResultsWrapper

crop_name = [('Coffee', 'coffee'), ('Black Pepper', 'black pepper'), ('Durian', 'durian')]
nutrients = ['N', 'P', 'K']
env_features = ['Temperature', 'pH', 'Moisture (%)']

thresholds = {
    'coffee': {'N': 200, 'P': 190, 'K': 180},
    'durian': {'N': 255, 'P': 218, 'K': 155},
    'black pepper': {'N': 150, 'P': 190, 'K': 140},
}

@st.cache_data
def load_crop_data(crop):
    path = f"data/{crop}.csv"
    df = pd.read_csv(path, parse_dates=['Timestamp'])
    df = df.sort_values('Timestamp')
    return df

@st.cache_resource
def load_sarima_model(crop: str, nutrient: str) -> Optional[SARIMAXResultsWrapper]:
    model_path = f"model/best_sarima_model_{crop}_{nutrient.upper()}.pkl"
    if not os.path.exists(model_path):
        return None
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def build_next_exog(df_env: pd.DataFrame, exog_names: list) -> pd.DataFrame:
    exog_dict = {}
    latest = df_env.iloc[-1]

    for name in exog_names:
        if name == 'const':
            exog_dict[name] = 1
        elif name.endswith('_lag_1'):
            base_feat = name.replace('_lag_1', '')
            exog_dict[name] = df_env[base_feat].iloc[-1]
        elif name.endswith('_lag_12'):
            base_feat = name.replace('_lag_12', '')
            if len(df_env) >= 12:
                exog_dict[name] = df_env[base_feat].iloc[-12]
            else:
                exog_dict[name] = latest[base_feat]
        else:
            exog_dict[name] = latest.get(name, 0)

    exog_df = pd.DataFrame([exog_dict])
    return exog_df

def show_dashboard():
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #2E8B57, #228B22);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .crop-button {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        border: none;
        padding: 15px 25px;
        border-radius: 8px;
        margin: 5px;
        cursor: pointer;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .crop-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .home-button {
        background: linear-gradient(45deg, #FF6B6B, #FF5252);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .section-header {
        background: linear-gradient(90deg, #f8f9fa, #e9ecef);
        padding: 1rem;
        border-radius: 8px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border: 1px solid #e9ecef;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize selected_crop if not exists
    if 'selected_crop' not in st.session_state:
        st.session_state['selected_crop'] = None

    crop_key = st.session_state.get('selected_crop')

    # If no crop is selected, show crop selection page
    if not crop_key:
        show_crop_selection()
    else:
        show_crop_dashboard(crop_key)

def show_crop_selection():
    """Show the crop selection page"""
    # Header with navigation
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("🏠 Back to Home", key="home_btn_selection"):
            st.session_state.current_page = "home"
            st.session_state.page = "home"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="main-header">
            <h1>🌱 Crop Nutrient Monitoring Dashboard</h1>
            <p>Real-time monitoring and forecasting for optimal crop nutrition</p>
        </div>
        """, unsafe_allow_html=True)

    # Crop Selection Section
    st.markdown("""
    <div class="section-header">
        <h3>🌾 Select Your Crop</h3>
        <p>Choose a crop to view detailed nutrient analysis and forecasting</p>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(len(crop_name))
    for i, (label, key) in enumerate(crop_name):
        with cols[i]:
            if st.button(f"🌿 {label}", key=f"crop_{key}", use_container_width=True):
                st.session_state['selected_crop'] = key
                st.rerun()

    st.markdown("""
    <div class="info-card">
        <h4>📋 Welcome to the Crop Nutrient Dashboard</h4>
        <p>This dashboard provides:</p>
        <ul>
            <li>🌤️ Real-time environmental monitoring</li>
            <li>🧪 Nutrient level tracking and forecasting</li>
            <li>📊 Historical data analysis</li>
            <li>⚠️ Threshold alerts</li>
        </ul>
        <p><strong>👆 Please select a crop above to get started!</strong></p>
    </div>
    """, unsafe_allow_html=True)

def show_crop_dashboard(crop_key):
    """Show the actual dashboard with graphs for selected crop"""
    # Header with navigation - different buttons for dashboard view
    col1, col2= st.columns([1, 3])
    
    # with col1:
    #     if st.button("🏠 Home", key="home_btn_dashboard"):
    #         st.session_state.page = "home"
    #         st.session_state.selected_crop = None
    #         st.rerun()
    
    with col1:
        if st.button("🔙 Change Crop", key="back_to_selection"):
            st.session_state.selected_crop = None
            st.rerun()
    
    with col2:
        st.markdown(f"""
        <div class="main-header">
            <h1>📊 {crop_key.capitalize()} Dashboard</h1>
            <p>Real-time data and predictions for your {crop_key} crop</p>
        </div>
        """, unsafe_allow_html=True)

    # Load dataset
    try:
        df = load_crop_data(crop_key)
        
        # Display summary metrics
        latest_data = df.iloc[-1]
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h4>📅 Last Update</h4>
                <p>{latest_data['Timestamp'].strftime('%Y-%m-%d %H:%M')}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h4>🌡️ Temperature</h4>
                <p>{latest_data['Temperature']:.1f}°C</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h4>🧪 pH Level</h4>
                <p>{latest_data['pH']:.2f}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h4>💧 Moisture</h4>
                <p>{latest_data['Moisture (%)']:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"❌ Error loading data for {crop_key}: {e}")
        return

    # Filter last 24 hours for environment plots
    df_env = df[df['Timestamp'] >= df['Timestamp'].max() - timedelta(days=1)]

    # Environmental graphs (last 24 hours) - UNCHANGED
    st.markdown("""
    <div class="section-header">
        <h3>🌤 Environmental Conditions (Last 24 Hours)</h3>
        <p>Monitor key environmental factors affecting crop growth</p>
    </div>
    """, unsafe_allow_html=True)
    
    env_cols = st.columns(3)
    for i, feature in enumerate(env_features):
        with env_cols[i]:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df_env['Timestamp'], y=df_env[feature], mode='lines', name=feature))
            fig.update_layout(
                title=f'{feature.replace("_", " ").capitalize()} (Last 24 Hours)',
                xaxis_title='Time', yaxis_title=feature.capitalize()
            )
            st.plotly_chart(fig, use_container_width=True)

    # Nutrient forecasting - last 1 day history + next 3 hours - UNCHANGED
    st.markdown("""
    <div class="section-header">
        <h3>🧪 Nutrient Forecast (Last 24h + Next 3 Hours)</h3>
        <p>Predictive analysis for optimal nutrient management</p>
    </div>
    """, unsafe_allow_html=True)

    nutrient_cols = st.columns(3)
    forecast_horizon = 3  # 3 hours ahead
    df_nutrient = df[df['Timestamp'] >= df['Timestamp'].max() - timedelta(days=1)]

    for i, nutrient in enumerate(nutrients):
        model = load_sarima_model(crop_key, nutrient)
        with nutrient_cols[i]:
            if model is None:
                st.warning(f"⚠️ No model for {nutrient}")
                continue

            try:
                model_exog_names = getattr(model.model, "exog_names", [])
                forecast_vals = []
                future_times = []

                temp_df_env = df_env.copy()

                for step in range(1, forecast_horizon + 1):
                    exog = build_next_exog(temp_df_env, model_exog_names) if model_exog_names else None
                    forecast = model.forecast(steps=1, exog=exog) if exog is not None else model.forecast(steps=1)
                    forecast_val = forecast.iloc[0] if hasattr(forecast, "iloc") else forecast[0]
                    forecast_vals.append(forecast_val)
                    future_time = df_nutrient["Timestamp"].iloc[-1] + timedelta(hours=step)
                    future_times.append(future_time)

                    # Simulate next row for exog input
                    next_row = temp_df_env.iloc[-1:].copy()
                    next_row["Timestamp"] = future_time
                    for feat in env_features:
                        if feat in next_row.columns:
                            next_row[feat] = next_row[feat].values[0]
                    temp_df_env = pd.concat([temp_df_env, next_row], ignore_index=True)

                # Plot nutrient + forecast
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=df_nutrient["Timestamp"], y=df_nutrient[nutrient],
                                        mode="lines", name="Historical"))
                fig.add_trace(go.Scatter(x=future_times, y=forecast_vals,
                                        mode="lines+markers", name="Forecast (3h)",
                                        line=dict(color="red", dash="dash")))

                threshold = thresholds[crop_key][nutrient]
                fig.add_trace(go.Scatter(x=df_nutrient["Timestamp"], y=[threshold]*len(df_nutrient),
                                        mode="lines", name="Threshold",
                                        line=dict(color="orange", dash="dot")))

                fig.update_layout(title=f"{nutrient}", xaxis_title="Time", yaxis_title=nutrient)
                st.plotly_chart(fig, use_container_width=True)

                # Alert if any forecast value is below threshold
                if any(val < threshold for val in forecast_vals):
                    st.warning(f"⚠️ {nutrient} levels may drop below threshold in the next 3 hours!")

            except Exception as e:
                st.error(f"❌ Forecast error for {nutrient}: {e}")

    # Footer
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #666; border-top: 1px solid #eee; margin-top: 2rem;">
        <p>🌱 Crop Nutrient Monitoring System | Real-time Agricultural Intelligence</p>
    </div>
    """, unsafe_allow_html=True)