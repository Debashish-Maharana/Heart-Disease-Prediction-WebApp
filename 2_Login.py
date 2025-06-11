import streamlit as st
from utils.firebase_utils import login_user

# Configure page
st.set_page_config(
    page_title="Login - Heart Detector",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional black theme
st.markdown("""
<style>
    /* Hide Streamlit branding and menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 50%, #0f0f0f 100%);
        color: white;
    }
    
    /* Center container styling */
    .login-container {
        background: rgba(30, 30, 30, 0.9);
        padding: 3rem 2.5rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        max-width: 400px;
        margin: 0 auto;
        margin-top: 2rem;
    }
    
    /* Title styling */
    .login-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .login-subtitle {
        text-align: center;
        color: #b0b0b0;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* Logout message styling */
    .logout-message {
        text-align: center;
        color: #b0b0b0;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        background: rgba(40, 40, 40, 0.8) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #4CAF50 !important;
        box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.2) !important;
        background: rgba(50, 50, 50, 0.9) !important;
    }
    
    /* Label styling */
    .stTextInput > label {
        color: #e0e0e0 !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #4CAF50, #45a049) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        margin-top: 1rem !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #45a049, #3d8b40) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.3) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    /* Logout button styling */
    .logout-button > button {
        background: linear-gradient(135deg, #f44336, #d32f2f) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        margin-top: 1rem !important;
    }
    
    .logout-button > button:hover {
        background: linear-gradient(135deg, #d32f2f, #c62828) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(244, 67, 54, 0.3) !important;
    }
    
    /* Success/Error message styling */
    .stSuccess {
        background: rgba(76, 175, 80, 0.1) !important;
        border: 1px solid rgba(76, 175, 80, 0.3) !important;
        border-radius: 8px !important;
        color: #4CAF50 !important;
    }
    
    .stError {
        background: rgba(244, 67, 54, 0.1) !important;
        border: 1px solid rgba(244, 67, 54, 0.3) !important;
        border-radius: 8px !important;
        color: #f44336 !important;
    }
    
    /* Security icon */
    .security-icon {
        text-align: center;
        font-size: 4rem;
        margin-bottom: 1rem;
        opacity: 0.8;
    }
    
    /* Footer text */
    .login-footer {
        text-align: center;
        margin-top: 2rem;
        color: #808080;
        font-size: 0.9rem;
    }
    
    /* Navigation buttons styling */
    .nav-buttons {
        display: flex;
        gap: 1rem;
        margin-top: 2rem;
        justify-content: center;
        align-items: center;
        width: 100%;
    }
    
    /* Override Streamlit's button container styling for nav buttons */
    .nav-buttons .stButton {
        flex: 1;
        max-width: 150px;
    }
    
    .nav-buttons .stButton > button {
        background: rgba(40, 40, 40, 0.8) !important;
        color: #e0e0e0 !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        text-transform: none !important;
        letter-spacing: normal !important;
        margin-top: 0 !important;
    }
    
    .nav-buttons .stButton > button:hover {
        background: rgba(60, 60, 60, 0.9) !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
        transform: translateY(-1px) !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1) !important;
    }
    
    .register-link {
        text-align: center;
        margin-top: 1.5rem;
        color: #b0b0b0;
        font-size: 0.95rem;
    }
    
    .register-link a {
        color: #4CAF50;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    
    .register-link a:hover {
        color: #66BB6A;
        text-decoration: underline;
    }
    
    /* Animated background elements */
    .bg-animation {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .floating-circle {
        position: absolute;
        border-radius: 50%;
        background: rgba(76, 175, 80, 0.1);
        animation: float 6s ease-in-out infinite;
    }
    
    .circle-1 {
        width: 100px;
        height: 100px;
        top: 20%;
        left: 10%;
        animation-delay: 0s;
    }
    
    .circle-2 {
        width: 150px;
        height: 150px;
        top: 60%;
        right: 10%;
        animation-delay: 2s;
    }
    
    .circle-3 {
        width: 80px;
        height: 80px;
        bottom: 20%;
        left: 20%;
        animation-delay: 4s;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
</style>

<div class="bg-animation">
    <div class="floating-circle circle-1"></div>
    <div class="floating-circle circle-2"></div>
    <div class="floating-circle circle-3"></div>
</div>
""", unsafe_allow_html=True)

# Check if user is already logged in
if "user" in st.session_state and st.session_state["user"]:
    # User is logged in - show logout interface
    st.markdown('<div class="security-icon">👋</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="login-title">Welcome Back!</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="logout-message">You are logged in as: <strong>{st.session_state["user"].get("email", "User")}</strong></p>', unsafe_allow_html=True)

    # Create columns for better spacing
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Logout button with custom styling
        st.markdown('<div class="logout-button">', unsafe_allow_html=True)
        if st.button("🚪 Log Out"):
            # Clear session state and refresh page
            st.session_state.clear()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Button to go to Heart Detector
        if st.button("🩺 Go to Heart Detector"):
            st.switch_page("pages/4_Heart_Detector.py")

else:
    # User is not logged in - show login interface
    st.markdown('<div class="security-icon">🔐</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="login-title">Welcome Back</h1>', unsafe_allow_html=True)
    st.markdown('<p class="login-subtitle">Sign in to access Heart Detector</p>', unsafe_allow_html=True)

    # Create columns for better spacing
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Email input
        email = st.text_input("Email Address", placeholder="Enter your email")
        
        # Password input
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        # Login button
        if st.button("🚀 Log In"):
            if not email or not password:
                st.error("⚠️ Please fill in all fields")
            else:
                try:
                    with st.spinner("Authenticating..."):
                        user = login_user(email, password)
                        if not user:
                            raise ValueError("Invalid credentials")
                        
                        st.session_state["user"] = user
                        st.success("✅ Login successful! Redirecting...")
                        
                        # Add a small delay for better UX
                        import time
                        time.sleep(1)
                        
                        st.rerun()  # Refresh to show logged in state
                        
                except ValueError as ve:
                    st.error(f"🚫 Login failed: {ve}")
                except Exception as e:
                    st.error(f"❌ An unexpected error occurred: {str(e)}")

    # Register link (only shown when not logged in)
    st.markdown('''
    <div class="register-link">
        Don't have an account? <a href="http://localhost:8501/Register" onclick="window.location.href='Register'">Create one here</a>
    </div>
    ''', unsafe_allow_html=True)

# Footer
st.markdown('<p class="login-footer">Secure authentication powered by Firebase</p>', unsafe_allow_html=True)

# Navigation buttons
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)

# Create three columns; center column is wider
nav_col1, nav_col2, nav_col3 = st.columns([2, 1, 2])

# Place the button in the center column
with nav_col2:
    if st.button("🏠 Go To Home", key="home_btn", help="Go to Home Page"):
        st.switch_page("app.py")  # Adjust path if necessary

st.markdown('</div>', unsafe_allow_html=True)

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)