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
    
    # Background Section
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 60px 0; margin: 40px -50px; border-radius: 20px;">
        <div style="text-align: center; color: white; padding: 0 50px;">
            <h2 style="font-size: 2.5em; margin-bottom: 20px; font-weight: 300;">Revolutionizing Agriculture</h2>
            <p style="font-size: 1.3em; line-height: 1.8; max-width: 800px; margin: 0 auto;">
                Harness the power of artificial intelligence and advanced analytics to optimize your crop yield, 
                reduce resource waste, and make informed decisions that drive sustainable farming practices.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Features Section
    st.markdown("## 🚀 Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 15px; border-radius: 10px; 
                    border-left: 5px solid #FF6B6B; box-shadow: 0 2px 10px rgba(0,0,0,0.1); height: auto;width:350px">
            <h4 style="color: #FF6B6B; margin-bottom: 15px;">📊 Real-time Monitoring</h4>
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
                <li>SARIMA forecasting models</li>
                <li>Nutrient prediction (N, P, K)</li>
                <li>3-hour ahead forecasts</li>
                <li>Threshold alerts</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: white; padding: 15px; border-radius: 10px; 
                    border-left: 5px solid #45B7D1; box-shadow: 0 2px 10px rgba(0,0,0,0.1); height: auto; width:350px">
            <h4 style="color: #45B7D1; margin-bottom: 15px;">🌾 Multi-Crop Support</h4>
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
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
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
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        color: white; padding: 30px; border-radius: 15px;">
                <h4 style="margin-bottom: 15px;">Ready to Start?</h4>
                <p style="margin-bottom: 20px;">Explore your crop data and predictions</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # IMPORTANT: This button navigates to dashboard
        if st.button("🚀 Go to Dashboard", type="primary", use_container_width=True):
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

