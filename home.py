import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

def show_home_page():
    """Display the home page of the Predictive Care application"""
    
    # Header Section
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h2 style="color: #2E8B57; font-size: 3em; margin-bottom: 10px;">🌱 Welcome to Predictive Care System</h2>
        <h3 style="color: #4A4A4A; font-weight: 300;">Smart Agriculture Monitoring & Forecasting System</h3>
        <hr style="border: 2px solid #2E8B57; width: 50%; margin: 20px auto;">
    </div>
    """, unsafe_allow_html=True)
    
    # Welcome Section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
                    padding: 30px; border-radius: 15px; text-align: center; margin: 20px 0;">
            <h4 style="color: #2E8B57; margin-bottom: 15px;">Welcome to the Future of Agriculture</h4>
            <p style="font-size: 1.1em; line-height: 1.6; color: #555;">
                Our advanced predictive system helps farmers make data-driven decisions by monitoring 
                environmental conditions and forecasting nutrient levels for optimal crop growth.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key Features Section
    st.markdown("## 🚀 Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 15px; border-radius: 10px; 
                    border-left: 5px solid #4ECDC4; box-shadow: 0 2px 10px rgba(0,0,0,0.1); height: auto;width:350px">
            <h4 style="color: #4ECDC4; margin-bottom: 15px;">📊 Real-time Monitoring</h4>
            <ul style="line-height: 1.8;">
                <li>Temperature tracking</li>
                <li>Soil moisture levels</li>
                <li>pH monitoring</li>
                <li>Environmental analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 15px; border-radius: 10px; 
                    border-left: 5px solid #4ECDC4; box-shadow: 0 2px 10px rgba(0,0,0,0.1); height: auto; width:350px">
            <h4 style="color: #4ECDC4; margin-bottom: 15px;">🔮 Predictive Analytics</h4>
            <ul style="line-height: 1.8;">
                <li>Prophet forecasting models</li>
                <li>Nutrient prediction (N, P, K)</li>
                <li>3-hour ahead forecasts</li>
                <li>Threshold alerts</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: white; padding: 15px; border-radius: 10px; 
                    border-left: 5px solid #4ECDC4; box-shadow: 0 2px 10px rgba(0,0,0,0.1); height: auto; width:350px">
            <h4 style="color: #4ECDC4; margin-bottom: 15px;">🌾 Multi-Crop Support</h4>
            <ul style="line-height: 1.8;">
                <li>Crop-specific analysis</li>
                <li>Customized thresholds</li>
                <li>Nutrient depletion forecasting</li>
                <li>Comparative insights</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Getting Started Section
    st.markdown("## 🎯 Getting Started")
    
    col1, col2 , col3= st.columns([1, 8, 1])
    
    with col2:
        st.markdown("""
        <div style="background: #F8F9FA; padding: 25px; border-radius: 10px; border: 1px solid #E9ECEF;">
            <h4 style="color: #2E8B57; margin-bottom: 20px;">How to Use This System</h4>
            <ol style="line-height: 2; font-size: 1.05em;">
                <li><strong>Navigate to Dashboard:</strong> Access real-time monitoring and predictions</li>
                <li><strong>Select Your Crop:</strong> Choose from available crop options</li>
                <li><strong>View Analytics:</strong> Monitor environmental conditions and nutrient forecasts</li>
                <li><strong>Take Action:</strong> Use threshold alerts for timely interventions</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <div style="background: linear-gradient(135deg,  #2E8B57); 
                        color: white; padding: 30px; border-radius: 15px;">
                <h4 style="margin-bottom: 15px;">Ready to Start?</h4>
                <p style="margin-bottom: 20px;">Explore your crop data and predictions</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced animated button with CSS
        st.markdown("""
        <style>
        .animated-button {
            background: linear-gradient(45deg, #ff6b6b, #ee5a24, #ff9ff3, #54a0ff);
            background-size: 400% 400%;
            border: none;
            border-radius: 50px;
            color: white;
            padding: 15px 30px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
            animation: gradientShift 3s ease infinite;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            width: 100%;
            margin: 10px 0;
        }
        
        .animated-button:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
            animation-duration: 1s;
        }
        
        .animated-button:active {
            transform: translateY(-1px) scale(1.02);
        }
        
        .animated-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
            transition: left 0.6s;
        }
        
        .animated-button:hover::before {
            left: 100%;
        }
        
        .rocket-icon {
            display: inline-block;
            margin-right: 8px;
            animation: rocketBounce 2s ease-in-out infinite;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        @keyframes rocketBounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0) rotate(0deg);
            }
            40% {
                transform: translateY(-5px) rotate(-10deg);
            }
            60% {
                transform: translateY(-3px) rotate(5deg);
            }
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(84, 160, 255, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(84, 160, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(84, 160, 255, 0); }
        }
        
        .animated-button:hover {
            animation: gradientShift 1s ease infinite, pulse 1.5s infinite;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Apply CSS styling to Streamlit button
        st.markdown("""
        <style>
        /* Target the specific button */
        .stButton > button {
            background: linear-gradient(45deg, #ff6b6b, #ee5a24, #ff9ff3, #54a0ff) !important;
            background-size: 400% 400% !important;
            border: none !important;
            border-radius: 50px !important;
            color: white !important;
            padding: 15px 30px !important;
            font-size: 18px !important;
            font-weight: bold !important;
            cursor: pointer !important;
            position: relative !important;
            overflow: hidden !important;
            transition: all 0.3s ease !important;
            animation: gradientShift 3s ease infinite !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
            width: 100% !important;
            margin: 10px 0 !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px) scale(1.05) !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3) !important;
            animation: gradientShift 1s ease infinite, pulse 1.5s infinite !important;
        }
        
        .stButton > button:active {
            transform: translateY(-1px) scale(1.02) !important;
        }
        
        .stButton > button::before {
            content: '' !important;
            position: absolute !important;
            top: 0 !important;
            left: -100% !important;
            width: 100% !important;
            height: 100% !important;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent) !important;
            transition: left 0.6s !important;
            z-index: 1 !important;
        }
        
        .stButton > button:hover::before {
            left: 100% !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # IMPORTANT: This button navigates to dashboard with animations
        if st.button("🚀 Go to Dashboard", type="primary", use_container_width=True, key="animated_dashboard_btn"):
            st.session_state.current_page = "Dashboard"
            st.rerun()
    
    # Recent Activity Section
    # st.markdown("## 📋 Recent System Activity")
    
    # # Sample activity data - replace with your actual data
    # activity_data = {
    #     "Time": [
    #         datetime.now().strftime("%H:%M"),
    #         (datetime.now().replace(hour=datetime.now().hour-1)).strftime("%H:%M"),
    #         (datetime.now().replace(hour=datetime.now().hour-2)).strftime("%H:%M"),
    #         (datetime.now().replace(hour=datetime.now().hour-3)).strftime("%H:%M")
    #     ],
    #     "Event": [
    #         "🌡️ Temperature reading updated",
    #         "⚠️ pH threshold alert for Crop A",
    #         "📊 Nutrient forecast completed",
    #         "💧 Moisture level normalized"
    #     ],
    #     "Status": ["✅ Normal", "⚠️ Alert", "✅ Completed", "✅ Normal"]
    # }
    
    # activity_df = pd.DataFrame(activity_data)
    # st.dataframe(activity_df, use_container_width=True, hide_index=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px; color: #888;">
        <p>🌱 Predictive Care System | Empowering Smart Agriculture | Version 1.0</p>
        <p>Last updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
    </div>
    """, unsafe_allow_html=True)