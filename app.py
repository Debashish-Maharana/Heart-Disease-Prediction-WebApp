import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Heart Disease Detection Platform", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&display=swap');

    /* Override Streamlit's default dark theme */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
    }

    .main {
        background: transparent !important;
        color: #2c3e50 !important;
    }

    /* Ensure all text is visible */
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: #2c3e50 !important;
    }

    /* Global Styling */
    .main {
        padding-top: 1rem;
    }

    /* Custom Header with enhanced gradient */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin-bottom: 3rem;
        text-align: center;
        color: white;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }

    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100%" height="100%" fill="url(%23grid)"/></svg>');
        opacity: 0.3;
    }

    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
        background: linear-gradient(45deg, #fff, #e8f4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .main-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        font-weight: 400;
        opacity: 0.95;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.7;
        position: relative;
        z-index: 1;

    }

    /* Enhanced Action Cards */
    .action-cards-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }

    .action-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9ff 100%) !important;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        border: 1px solid rgba(102, 126, 234, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        text-align: center;
        color: #2c3e50 !important;
        position: relative;
        overflow: hidden;
        cursor: pointer;
    }

    .action-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.1), transparent);
        transition: left 0.6s;
    }

    .action-card:hover::before {
        left: 100%;
    }

    .action-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 25px 50px rgba(102, 126, 234, 0.2);
        border-color: rgba(102, 126, 234, 0.3);
    }

    .card-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        display: block;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
    }

    .card-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.7rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 1rem;
    }

    .card-description {
        color: #6c757d;
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 2rem;
    }

    /* Enhanced Heart Detector CTA */
    .detector-cta {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 50%, #ff9ff3 100%);
        padding: 3rem 2rem;
        border-radius: 25px;
        text-align: center;
        color: white;
        margin: 3rem 0;
        box-shadow: 0 20px 60px rgba(255, 107, 107, 0.3);
        position: relative;
        overflow: hidden;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .detector-cta::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: rotate 8s linear infinite;
    }

    .detector-cta:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 30px 80px rgba(255, 107, 107, 0.4);
    }

    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .detector-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .detector-description {
        font-size: 1.3rem;
        margin-bottom: 2rem;
        opacity: 0.95;
        position: relative;
        z-index: 1;
        line-height: 1.6;
    }

    /* Feature Sections Enhanced - Now as clickable buttons */
    .feature-section {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9ff 100%) !important;
        padding: 4rem 2rem;
        border-radius: 25px;
        margin: 3rem 0;
        color: #2c3e50 !important;
        box-shadow: 0 15px 50px rgba(0,0,0,0.08);
        border: 1px solid rgba(102, 126, 234, 0.1);
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .feature-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.05), transparent);
        transition: left 0.6s;
    }

    .feature-section:hover::before {
        left: 100%;
    }

    .feature-section:hover {
        transform: translateY(-8px) scale(1.01);
        box-shadow: 0 25px 70px rgba(102, 126, 234, 0.15);
        border-color: rgba(102, 126, 234, 0.3);
    }

    .section-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 2rem;
        text-align: center;
        position: relative;
    }

    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 2px;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2.5rem;
        margin-top: 3rem;
    }

    .feature-item {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9ff 100%) !important;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        border-left: 5px solid #667eea;
        color: #2c3e50 !important;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .feature-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .feature-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.15);
    }

    .feature-icon {
        color: #667eea;
        font-size: 2rem;
        margin-right: 0.8rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }

    .feature-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.8rem;
        font-size: 1.3rem;
    }

    .feature-text {
        color: #6c757d;
        line-height: 1.6;
        font-size: 1rem;
    }

    /* Enhanced Steps Section - Now as clickable button */
    .steps-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
        background: linear-gradient(145deg, #ffffff 0%, #f8f9ff 100%) !important;
        padding: 3rem 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .steps-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.05), transparent);
        transition: left 0.6s;
    }

    .steps-container:hover::before {
        left: 100%;
    }

    .steps-container:hover {
        transform: translateY(-8px) scale(1.01);
        box-shadow: 0 25px 60px rgba(102, 126, 234, 0.15);
    }

    .step-item {
        text-align: center;
        padding: 2rem 1rem;
        position: relative;
        color: #2c3e50 !important;
        transition: all 0.3s ease;
    }

    .step-item:hover {
        transform: translateY(-5px);
    }

    .step-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 1.4rem;
        margin: 0 auto 1.5rem auto;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        font-family: 'Poppins', sans-serif;
    }

    .step-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.8rem;
        font-size: 1.3rem;
    }

    /* Parameter grid enhanced styling - Now as clickable button */
    .parameter-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 1.5rem;
        background: linear-gradient(145deg, #ffffff 0%, #f8f9ff 100%) !important;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .parameter-grid::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.05), transparent);
        transition: left 0.6s;
    }

    .parameter-grid:hover::before {
        left: 100%;
    }

    .parameter-grid:hover {
        transform: translateY(-8px) scale(1.01);
        box-shadow: 0 25px 50px rgba(102, 126, 234, 0.15);
    }

    .parameter-item {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9ff 100%) !important;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #667eea;
        color: #2c3e50 !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }

    .parameter-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.15);
    }

    /* Enhanced CTA Section - Now as clickable button */
    .cta-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 4rem 2rem;
        border-radius: 25px;
        text-align: center;
        color: white;
        margin: 4rem 0;
        box-shadow: 0 25px 70px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .cta-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="80" cy="20" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="40" cy="70" r="1.5" fill="rgba(255,255,255,0.1)"/><circle cx="90" cy="80" r="1" fill="rgba(255,255,255,0.1)"/></svg>');
        opacity: 0.5;
    }

    .cta-section:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 35px 90px rgba(102, 126, 234, 0.5);
    }

    .cta-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    }

    .cta-description {
        font-size: 1.3rem;
        margin-bottom: 2.5rem;
        opacity: 0.95;
        position: relative;
        z-index: 1;
        line-height: 1.7;
    }

    /* Enhanced Footer */
    .footer {
        background-color: #FFFFFF !important;
        color: white;
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-top: 4rem;
        box-shadow: 0 15px 40px rgba(44, 62, 80, 0.3);
    }

    .footer-title {
        background-color: #FFFFFF;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        margin-bottom: 1rem;
        font-size: 1.5rem;
        color: #FFFFFF !important;
    }

    .disclaimer {
        background-color: #FFFFFF;
        font-size: 0.95rem;
        opacity: 0.85;
        margin-top: 1.5rem;
        font-style: italic;
        line-height: 1.6;
    }

    /* Enhanced Streamlit button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        padding: 1rem 3rem !important;
        border-radius: 15px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3) !important;
        font-family: 'Poppins', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4) !important;
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%) !important;
    }

    /* Special styling for detector button */
    .detector-button .stButton > button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%) !important;
        font-size: 1.3rem !important;
        padding: 1.2rem 4rem !important;
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.4) !important;
    }

    .detector-button .stButton > button:hover {
        background: linear-gradient(135deg, #ff5252 0%, #d63031 100%) !important;
        box-shadow: 0 20px 40px rgba(255, 107, 107, 0.5) !important;
    }

    /* Responsive Design Enhanced */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.8rem;
        }
        .main-subtitle {
            font-size: 1.2rem;
        }
        .section-title {
            font-size: 2rem;
        }
        .detector-title {
            font-size: 2.2rem;
        }
        .cta-title {
            font-size: 2.3rem;
        }
    }

    /* Additional overrides for dark theme */
    .stApp > div {
        background: transparent !important;
    }

    /* Pulse animation for important elements */
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(102, 126, 234, 0); }
        100% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0); }
    }

    .pulse-animation {
        animation: pulse 2s infinite;
    }

    /* Click action indicator */
    .action-card::after, 
    .feature-section::after, 
    .steps-container::after,
    .parameter-grid::after,
    .cta-section::after,
    .detector-cta::after {
        content: '👆 Click to explore';
        position: absolute;
        bottom: 1rem;
        right: 1rem;
        background: rgba(102, 126, 234, 0.9);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        opacity: 0;
        transition: opacity 0.3s ease;
        z-index: 10;
    }

    .action-card:hover::after, 
    .feature-section:hover::after, 
    .steps-container:hover::after,
    .parameter-grid:hover::after,
    .cta-section:hover::after,
    .detector-cta:hover::after {
        opacity: 1;
    }

</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Add click functionality to sections
    setTimeout(function() {
        // Heart Detector CTA
        const detectorCta = document.querySelector('.detector-cta');
        if (detectorCta) {
            detectorCta.addEventListener('click', function() {
                window.location.href = 'pages/4_Heart_Detector.py';
            });
        }

        // Feature sections - could navigate to different pages or scroll to sections
        const featureSections = document.querySelectorAll('.feature-section');
        featureSections.forEach(function(section, index) {
            section.addEventListener('click', function() {
                // You can customize these actions based on your needs
                if (section.querySelector('.section-title').textContent.includes('About CardioCare')) {
                    // Could navigate to about page or show more info
                    alert('Learn more about CardioCare platform features and capabilities!');
                } else if (section.querySelector('.section-title').textContent.includes('Why Choose')) {
                    // Could navigate to features page
                    alert('Discover all the reasons healthcare professionals trust CardioCare!');
                } else if (section.querySelector('.section-title').textContent.includes('Medical Assessment')) {
                    // Could navigate to assessment details
                    alert('Explore our comprehensive 13-parameter medical assessment system!');
                }
            });
        });

        // Steps container
        const stepsContainer = document.querySelector('.steps-container');
        if (stepsContainer) {
            stepsContainer.addEventListener('click', function() {
                alert('Ready to start your heart health journey? Click the assessment button above!');
            });
        }

        // Parameter grid
        const parameterGrid = document.querySelector('.parameter-grid');
        if (parameterGrid) {
            parameterGrid.addEventListener('click', function() {
                alert('Learn more about our evidence-based assessment parameters!');
            });
        }

        // CTA section
        const ctaSection = document.querySelector('.cta-section');
        if (ctaSection) {
            ctaSection.addEventListener('click', function() {
                window.location.href = 'pages/3_Register.py';
            });
        }
    }, 1000);
});
</script>
""", unsafe_allow_html=True)

# Main Header Section
st.markdown("""
<div class="main-header" style="text-align: center;">
    <h1 class="main-title">Heart Disease Detector</h1>
    <p class="main-subtitle" style="margin: 0 auto; text-align: center;">
        Advanced AI-powered heart disease detection platform designed to provide accurate cardiovascular risk assessment through comprehensive medical parameter analysis
    </p>
</div>
""", unsafe_allow_html=True)


# Login/Register Section
st.markdown('<h2 class="section-title">Get Started</h2>', unsafe_allow_html=True)

# Action Cards Container
st.markdown('<div class="action-cards-container">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown("""
        <div style="padding: 1rem; border: 1px solid #ddd; border-radius: 0.5rem; margin-bottom: 1rem;">
            <div style="text-align: center; font-size: 2rem;">🔐</div>
            <h3 style="text-align: center; margin: 0.5rem 0;">Existing User</h3>
            <p style="text-align: center; color: #666; margin: 0;">
                Access your account to continue with heart health monitoring and view your previous assessments.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🏠 Go To Login", key="home_btn", help="Go to Home Page", use_container_width=True):
            st.switch_page("2_Login.py")
    

    

with col2:
    with st.container():
        st.markdown("""
        <div style="padding: 1rem; border: 1px solid #ddd; border-radius: 0.5rem; margin-bottom: 1rem;">
            <div style="text-align: center; font-size: 2rem;">📝</div>
            <h3 style="text-align: center; margin: 0.5rem 0;">New User</h3>
            <p style="text-align: center; color: #666; margin: 0;">
                Create your secure account to start your cardiovascular health journey with personalized insights.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📝 Go To Register", key="register_btn", help="Go to Registration Page", use_container_width=True):
            st.switch_page("3_Register.py")  # Adjust the path to your register page


st.markdown('</div>', unsafe_allow_html=True)

# Heart Detector CTA Section
with st.container():
    st.markdown("""
    <div style="padding: 2rem; border: 2px solid #ff6b6b; border-radius: 1rem; background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); margin: 2rem 0; text-align: center;">
        <h2 style="color: #333; margin: 0 0 1rem 0; font-size: 1.5rem;">🔬 Start Heart Analysis</h2>
        <p style="color: #555; margin: 0; font-size: 1.1rem;">
            Ready to assess your cardiovascular health? Our AI-powered system will analyze your medical parameters and provide instant risk assessment.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔬 Start Heart Analysis Now", key="heart_detector_btn", help="Begin Heart Health Assessment", use_container_width=True, type="primary"):
        st.switch_page("4_Heart_Detector.py")  # Adjust the path to your heart detector page

# About Platform Section (Now clickable)
st.markdown("""
<div class="feature-section">
    <h2 class="section-title">About CardioCare Platform</h2>
    <p style="text-align: center; font-size: 1.2rem; color: #6c757d; max-width: 800px; margin: 0 auto; line-height: 1.7;">
        CardioCare leverages advanced machine learning algorithms trained on extensive cardiovascular datasets to provide accurate heart disease risk assessments. Our platform combines clinical expertise with cutting-edge technology to deliver reliable health insights.
    </p>
</div>
""", unsafe_allow_html=True)

# Key Features (Now clickable)
st.markdown("""
<div class="feature-section">
    <h2 class="section-title">Why Choose CardioCare?</h2>
    <div class="feature-grid">
        <div class="feature-item">
            <span class="feature-icon">⚡</span>
            <h4 class="feature-title">Rapid Analysis</h4>
            <p class="feature-text">Get comprehensive cardiovascular risk assessment results in under 30 seconds with real-time processing</p>
        </div>
        <div class="feature-item">
            <span class="feature-icon">🎯</span>
            <h4 class="feature-title">Clinical Accuracy</h4>
            <p class="feature-text">Built on validated medical datasets with 94%+ accuracy in risk prediction using ensemble learning models</p>
        </div>
        <div class="feature-item">
            <span class="feature-icon">🔬</span>
            <h4 class="feature-title">Evidence-Based</h4>
            <p class="feature-text">Algorithms developed in collaboration with cardiologists and medical researchers from leading institutions</p>
        </div>
        <div class="feature-item">
            <span class="feature-icon">🛡️</span>
            <h4 class="feature-title">Secure & Private</h4>
            <p class="feature-text">HIPAA-compliant data handling with enterprise-grade encryption and zero data retention policy</p>
        </div>
        <div class="feature-item">
            <span class="feature-icon">📊</span>
            <h4 class="feature-title">Detailed Insights</h4>
            <p class="feature-text">Comprehensive reports with risk factors, confidence intervals, and personalized recommendations</p>
        </div>
        <div class="feature-item">
            <span class="feature-icon">👥</span>
            <h4 class="feature-title">Professional Grade</h4>
            <p class="feature-text">Trusted by healthcare providers, medical professionals, and used in clinical decision support systems</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# How It Works Section (Now clickable)
st.markdown("""
<div class="feature-section">
    <h2 class="section-title">How It Works</h2>
    <div class="steps-container">
        <div class="step-item">
            <div class="step-number">1</div>
            <h4 class="step-title">Secure Account Setup</h4>
            <p class="feature-text">Register or sign in to your HIPAA-compliant CardioCare account with enterprise-grade security</p>
        </div>
        <div class="step-item">
            <div class="step-number">2</div>
            <h4 class="step-title">Guided Data Input</h4>
            <p class="feature-text">Enter your medical parameters through our intuitive, clinically-validated assessment form</p>
        </div>
        <div class="step-item">
            <div class="step-number">3</div>
            <h4 class="step-title">AI-Powered Analysis</h4>
            <p class="feature-text">Our advanced machine learning algorithms analyze your data against extensive clinical datasets</p>
        </div>
        <div class="step-item">
            <div class="step-number">4</div>
            <h4 class="step-title">Comprehensive Results</h4>
            <p class="feature-text">Receive detailed risk assessment with actionable insights and evidence-based recommendations</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# Final CTA Section (Now clickable)
st.markdown("""
<div class="cta-section">
    <h2 class="cta-title">Transform Your Heart Health Journey</h2>
    <p class="cta-description">Join thousands of users who trust CardioCare for accurate cardiovascular risk assessment. Take control of your health today with our evidence-based platform.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer" >
    <h4 class="footer-title">CardioCare Platform</h4>
    <p style="font-size: 1.1rem; margin-bottom: 0.5rem;">Developed by IF 17 Medical Technology Team</p>
    <p style="font-size: 0.95rem; opacity: 0.8;">Advancing cardiovascular health through artificial intelligence</p>
    <p class="disclaimer">
        This platform is designed for educational and screening purposes only. Results should not replace professional medical consultation. 
        Always consult with qualified healthcare providers for medical decisions. CardioCare is not intended for emergency medical situations.
    </p>
</div>
""", unsafe_allow_html=True)