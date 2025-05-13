def get_intro_style(base64_logo):
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Albert+Sans:wght@800&display=swap');

    .phone {{
        width: 320px;
        height: 640px;
        margin: 50px auto;
        border-radius: 40px;
        background-color: #f9f9f9;
        box-shadow: 0 0 15px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        padding: 60px 20px 40px;
        position: relative;
        text-align: center;
    }}
    .logo {{
        width: 120px;
        height: auto;
        margin-top: 80px;
    }}
    .brand {{
        font-family: 'Albert Sans', sans-serif;
        font-weight: 800;
        font-size: 40px;
        color: #ff3b5c;
        margin-top: 20px;
    }}
    div.stButton > button {{
        background-color: #ff3b5c;
        color: white;
        padding: 14px 32px;
        font-family: 'Albert Sans', sans-serif;
        font-weight: 400;
        font-size: 18px;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        width: 200px; important! 
        justify-content: center;
        position: absolute;    
        top: -150px;            
        left: 250px;          
    }}
    div.stButton > button:hover {{
        background-color: white;
        color: #ff3b5c;
        border: 2px solid #ff3b5c;
    }}
    </style>

    <div class="phone">
        <div>
            <img src="data:image/png;base64,{base64_logo}" class="logo" />
            <div class="brand">Piboo</div>
        </div>
    """
